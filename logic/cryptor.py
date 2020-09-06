

class Cryptor:
    """
    Клас для шифрования и дешифрования текста
    """
    def __init__(self, offset=3):
        self.offset = offset

    def decode(self, text):
        return ''.join([chr(ord(x) - self.offset) for x in text])

    def encode(self, text):
        return ''.join([chr(ord(x) + self.offset) for x in text])
