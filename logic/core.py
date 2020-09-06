from logic.view import View
from logic.client import Client


class Core:
    def __init__(self, api_id, api_hash, sessio):
        self.client = Client(api_id, api_hash, sessio)
        self.view = View()

    def run(self):
        self.view.run()
