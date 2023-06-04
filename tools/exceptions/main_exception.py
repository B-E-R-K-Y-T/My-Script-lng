import sys

from colorama import init
from colorama import Fore

init()


class MainException(Exception):
    def __init__(self, *args, default):
        self.default = default

        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        return self.__generate_error_message()

    def __generate_error_message(self):
        if self.message:
            return f'{self.__class__.__name__}: {self.message}'
        else:
            return f'{self.__class__.__name__}: {self.default}'


class KillProcess(Exception):
    pass


def kill_process(num_line: int, line: str, exception: MainException = KillProcess):
    print(Fore.RED + f'{num_line=}, {line=}\n\t{exception}')
    sys.exit()
