
import asyncio
import time
import tkinter as tk

from datetime import datetime
from telethon import events
from telethon import TelegramClient


class View:
    """
    Класс отвечающий за визуализацию и поведение визуальных компонентов
    """
    def __init__(self, send_message_callback):
        self.send_message_callback = send_message_callback

        self.window = tk.Tk()

        self.messages = tk.Text(self.window)
        self.messages.pack()

        self.input_user = tk.StringVar()
        self.input_field = tk.Entry(self.window, text=self.input_user)
        self.input_field.pack(side=tk.BOTTOM, fill=tk.X)
        self.input_field.bind("<Return>", self._enter_pressed)

    def _enter_pressed(self, event):
        """
        Функция для обработки события нажатия Enter
        """
        # send message
        self.send_message_callback(
            self.input_user.get()
        )
        # clear input
        self.input_user.set('')
        return "break"

    def run(self):
        """
        Функция запуска окна tkinter
        """
        self.window.mainloop()

    def add_message(self, text, is_user=True):
        """
        Функция добовления сообщения на экран
        """
        self.messages.insert(
            tk.INSERT,
            f'{datetime.now()}{">>" if is_user else "<<"} {text}\n'
        )
        # TODO: добавить скролинг в конец

    def clear_messages(self):
        self.messages.set("")
