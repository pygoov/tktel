from logic.cryptor import Cryptor


class Message:
    def __init__(text, is_user, out_time, meta):
        self.out_time = out_time
        self.text = text
        self.is_user = is_user
        self.meta = meta


class MessageStore:
    def __init__(self, user_id, cryptor: Cryptor):
        self.user_id = user_id
        self.cryptor = cryptor
        self.messages = []

    def addMessage(self, msg):
        self.messages.append(msg)
