# modules/memory_manager.py

class ConversationMemory:

    def __init__(self):
        self.data = {}

    def save(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)

    def get_all(self):
        return self.data

    def clear(self):
        self.data = {}