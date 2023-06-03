import re

from tools.exceptions.object_exceptions import TypeException


class Int:
    def __init__(self, value: str):
        if not self.is_int(value):
            raise TypeException(f'This object "{value}" is not {Int.__name__}!')

        self.value = int(value)

    @staticmethod
    def is_int(value: str):
        if re.fullmatch(pattern=r'-?\d+', string=value):
            return True
        return False

    def add(self, other: int):
        return self.value + other

    def get_value(self):
        return self.value


class Line:
    def __init__(self, value: str):
        if not self.is_line(value):
            raise TypeException(f'This object "{value}" is not {Line.__name__}!')

        self.value = value.replace('"', '')

    @staticmethod
    def is_line(value: str):
        if value.startswith('"') and value.endswith('"'):
            return True
        return False

    def get_value(self):
        return self.value


if __name__ == '__main__':
    i = Int('1')
    print(i.add(1))

    l = Line('"TETS"')
    # l = Line('TETS"')
    # l = Line('"TETS')
