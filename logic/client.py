import asyncio
import time

from telethon import TelegramClient
from telethon import events
from threading import Thread
from functools import partial


class Client:
    def __init__(self, api_id, api_hash, session, send_message_callback):
        self.api_id = api_id
        self.api_hash = api_hash
        self.session = session
        self.loop = None
        self.client = None
        self.tasks = None
        self.send_message_callback = send_message_callback

        # запускаем новый поток
        self.th = Thread(target=self._run, daemon=True)
        self.th.start()

    def make_client(self):
        self.client = TelegramClient(
            self.session,
            self.api_id,
            self.api_hash
        )
        self.client.add_event_handler(
            self.message_handler,
            events.newmessage.NewMessage()
        )

    async def _task_solver_loop(self):
        """
        функция для выполнения задач из очереди.
        Необходим для связи между клиентом telethon(его евентлупом) и главным потоком в котором вертиться tkinter
        """
        print("run task solver loop")
        while True:
            task = await self.tasks.get()
            method = getattr(self.client, task["method"])
            try:
                task["result"] = await method(*task["args"], **task["kwargs"])
            except Exception as e:
                print(f"Error({type(e)}):{e}")
                task["error"] = e
            finally:
                task["done"] = True

    async def message_handler(self, event):
        # print("event:", event)
        # user_id = event.from_id
        # message = event.message.message
        # print(f"user_id: {user_id} message: {message}")

        self.send_message_callback(event)

    async def _async_run(self):
        print("started client")
        try:
            await self.client.start(
                phone=lambda: input("Enter phone: "),
                password=lambda: input("Enter password: "),
                code_callback=lambda: input("Enter code: ")
            )
            await self._task_solver_loop()
        except Exception as e:
            print(e)
        print("end client")

    def _run(self):
        # создаём новый евент луп
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

        self.tasks = asyncio.Queue()
        self.make_client()

        # запускаем корутину
        self.loop.create_task(self._async_run())
        # запускаем луп
        self.loop.run_forever()

    # ====================================
    # ============= Sync api =============
    # ====================================

    def _make_task(self, method, args, kwargs):
        task = {
            "method": method,
            "args": args,
            "kwargs": kwargs,
            "done": False,
            "result": None,
            "error": None
        }
        self.loop.call_soon_threadsafe(lambda: self.tasks.put_nowait(task))

        # waiting done task
        while not task["done"]:
            time.sleep(0.01)  # sleep 10ms

        if task["error"] is not None:
            raise Exception(task["error"])

        return task["result"]

    def send_message(self, *args, **kwargs):
        return self._make_task("send_message", args, kwargs)
