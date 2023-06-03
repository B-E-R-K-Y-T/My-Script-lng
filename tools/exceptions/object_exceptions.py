from tools.exceptions.main_exception import MainException


class ObjectException(MainException):
    def __init__(self, *args):
        super().__init__(*args, default='Object error!')


class TypeException(MainException):
    def __init__(self, *args):
        super().__init__(*args, default='Type error!')


class FunctionException(MainException):
    def __init__(self, *args):
        super().__init__(*args, default='Function error!')

