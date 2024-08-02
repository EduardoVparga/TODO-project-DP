from abc import ABC, abstractmethod
from datetime import datetime

class Publisher(ABC):
    @abstractmethod
    def register_listener(self, listener):
        pass

    @abstractmethod
    def remove_listener(self, listener):
        pass

    @abstractmethod
    def notify_listeners(self):
        pass


class Logger(Publisher):
    def __init__(self):
        self.listeners = []
        self.datetime = None
        self.source = None
        self.level = None
        self.message = None

    def activity(self, source, level, message):
        self.date = datetime.now()
        self.source = source
        self.level = level
        self.message = message
        self.notify_listeners()

    def register_listener(self, listener):
        if listener not in self.listeners:
            self.listeners.append(listener)
        else:
            print(f'listener {listener} already registered!')

    def remove_listener(self, listener):
        self.listeners.remove(listener)

    def notify_listeners(self):
        for listener in self.listeners:
            listener.update(self.date, self.source, self.level, self.message)
