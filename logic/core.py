from logic.view import View
from logic.client import Client
from logic.cryptor import Cryptor


class Core:
    def __init__(self, api_id, api_hash, session, user_id):
        self.current_user_id = user_id
        self.client = Client(api_id, api_hash, session, self.client_message_handler)
        self.view = View(self.view_message_handler)

        self.cryptor = Cryptor()

    def view_message_handler(self, text):
        """
        Функция колбэк в которую приходят все сообщения написанные пользователем с формы
        """
        print("view text:", text)
        self.client.send_message(
            self.current_user_id,
            self.cryptor.encode(text)
        )
        self.view.add_message(text, True)

    def client_message_handler(self, event):
        """
        Функция колбэк в которую приходят все сообщения из телеграмм
        """
        print("client_message_handler")
        if event.from_id != self.current_user_id:
            print("failed event user")
            return
        text = event.message.message
        text = self.cryptor.decode(text)
        print("client text:", text)
        self.view.add_message(text, False)

    def run(self):
        self.view.run()
