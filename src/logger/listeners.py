from abc import ABC, abstractmethod

colors = {
    'INFO': '\033[92m',
    'WARN': '\033[93m',
    'ERR': '\033[91m',
    'ENDC': '\033[0m',
    'BOLD': '\033[1m',
}

def c(level, string):
    return f"{colors[level]}{string}{colors['ENDC']}" 

class Observer(ABC):
    @abstractmethod
    def update(self, date, source, level, message):
        pass

class ConsoleLogger(Observer):
    def update(self, date, source, level, message):
        print(f"{c('BOLD', date)} - {c(level, level)} - {c(level, source)} - {message}")

class FileLogger(Observer):
    def update(self, date, source, level, message):
        with open("app.log", "a") as file:
            file.write(f"{date} - {level} - {source} - {message}\n")