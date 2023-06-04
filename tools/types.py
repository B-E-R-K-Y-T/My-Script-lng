import re

from abc import ABC, abstractmethod
from tools.exceptions.object_exceptions import TypeException, IndexException


class Type(ABC):
    @staticmethod
    @abstractmethod
    def check_type(value: str) -> bool:
        raise NotImplemented

    @abstractmethod
    def get_value(self):
        raise NotImplemented


class Int(Type):
    def __init__(self, value: str):
        if not self.check_type(value):
            raise TypeException(f'This object "{value}" is not {Int.__name__}!')

        self.value = int(value)

    @staticmethod
    def check_type(value: str) -> bool:
        if re.fullmatch(pattern=r'[ ]?-?\d+', string=value):
            return True
        return False

    def add(self, other: int):
        return self.value + other

    def get_value(self) -> int:
        return self.value


class Array(Type):
    def __init__(self, value: str):
        if not self.check_type(value):
            raise TypeException(f'This object "{value}" is not {Array.__name__}!')

        self.value = value

    @staticmethod
    def check_type(value: str) -> bool:
        if re.findall(pattern=r'[ ]*{[\w\d,\" ]+}', string=value):
            return True
        return False

    @staticmethod
    def convert_str_to_array(value: str) -> list:
        idx_start = value.find('{')
        idx_end = value.rfind('}')
        array = value[idx_start+1:idx_end].split(',')

        res = []

        for t in [Line, Int]:
            for item in array:
                if t.check_type(item):
                    res.append(t(item).get_value())

        return res

    def get_value(self) -> list:
        return self.convert_str_to_array(self.value)

    def __getitem__(self, item):
        try:
            return self.get_value()[item]
        except IndexError as e:
            raise IndexException(e)


class Line(Type):
    def __init__(self, value: str):
        if not self.check_type(value):
            raise TypeException(f'This object "{value}" is not {Line.__name__}!')

        self.value = value.replace('"', '')

    @staticmethod
    def check_type(value: str) -> bool:
        if value.startswith('"') and value.endswith('"'):
            return True
        return False

    def get_value(self) -> str:
        return self.value


if __name__ == '__main__':
    i = Int('1')
    print(i.add(1))

    l = Line('"TETS"')
    # l = Line('TETS"')
    # l = Line('"TETS')
