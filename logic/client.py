import asyncio

from telethon import TelegramClient
from telethon import events
from threading import Thread
from functools import partial


class Client:
    def __init__(self, api_id, api_hash, session):
        self.api_id = api_id
        self.api_hash = api_hash
        self.session = session
        self.loop = None
        self.client = None

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

    async def message_handler(self, event):
        print("event:", event)
        user_id = event.from_id
        message = event.message.message
        print(f"user_id: {user_id} message: {message}")

        if user_id == 862518887:
            x = await self.client.send_message(user_id, message)
            print("x:", x)

        # if event.media is not None:
        #     task = client.loop.create_task(event.download_media("1.pem"))
        #     await task
        #     print("RAW: ")

    async def _async_run(self):
        print("started client")
        try:
            await self.client.start(
                phone=lambda: input("Enter phone: "),
                password=lambda: input("Enter password: "),
                code_callback=lambda: input("Enter code: ")
            )
        except Exception as e:
            print(e)
        print("end client")

    def _run(self):
        # создаём новый евент луп
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

        self.make_client()

        # запускаем корутину
        self.loop.create_task(self._async_run())
        # запускаем луп
        self.loop.run_forever()
