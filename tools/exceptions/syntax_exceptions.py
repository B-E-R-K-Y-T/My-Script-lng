from tools.exceptions.main_exception import MainException


class SyntaxException(MainException):
    def __init__(self, *args):
        super().__init__(*args, default='Syntax error!')
