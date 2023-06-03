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
