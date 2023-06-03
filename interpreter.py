from tools.debug import print_debug
from tools.parser import *
from tools.types import Int, Line
from tools.exceptions.main_exception import MainException


class Interpreter:
    def __init__(self, path: str, jump_to_num_line: int = 0, end_line: int = ..., is_loop: bool = False, **flags):
        self.file = open(path)
        self.path = path
        self.jump_to_num_line = jump_to_num_line
        self.end_line = end_line
        self.is_loop = is_loop

    def run(self):
        for num_line, line in enumerate(self.file):

            if num_line < self.jump_to_num_line:
                continue

            if self.end_line is not ...:
                if num_line > self.end_line:
                    return

            try:
                if line.isspace():
                    continue

                par = Parser(line)

                if par.is_commentary():
                    continue

                print_debug(line)

                if par.is_variable():
                    var = Var(line)
                    var.save_var(var.get_key(), var.get_value())
                elif par.is_calculated_variable():
                    var = Var(line)
                    _par = Parser(var.get_value())

                    if _par.is_added():
                        _line = var.get_value().replace(' ', '')
                        a, b = _line.split('+')

                        res = None

                        if is_var_exists(a) and is_var_exists(b):
                            if isinstance(get_var(a), Int) and isinstance(get_var(b), Int):
                                res = int(get_var(a).get_value()) + int(get_var(b).get_value())

                    var.save_var(var.get_key(), str(res))
                elif par.is_added():
                    _line = line.replace(' ', '')
                    a, b = _line.split('+')

                    res = None

                    if Int.is_int(a) and Int.is_int(b):
                        res = int(get_var(a)) + int(get_var(b))
                elif par.is_start_loop() and not self.is_loop:
                    start, stop = par.count_repeat_in_loop()
                    var_in_loop = par.get_var_in_loop()

                    end_loop = None

                    for _num_line, _line in enumerate(self.file):
                        _par = Parser(_line)

                        if par.is_commentary():
                            continue

                        if _par.is_end_loop():
                            end_loop = _num_line + num_line
                            break

                    if end_loop is None:
                        raise SyntaxException(f'Not found end loop!')
                    else:
                        for i in range(start, stop+1):
                            set_var(var_in_loop, Int(str(i)))
                            _interpreter = Interpreter(self.path, num_line, end_loop, is_loop=True)
                            _interpreter.run()

                elif par.is_print():
                    print(*par.get_data_from_print())
                else:
                    if not self.is_loop:
                        raise SyntaxException(f'Invalid syntax: {line=}')

            except MainException as e:
                print(f'{num_line=}\n\t{e}')
                break

        print_debug(get_vars())


if __name__ == '__main__':
    commands = input('>>>').split(' ')

    TEST = '/home/berkyt/PycharmProjects/MyScriptLanguage/test.txt'

    interpreter = Interpreter(commands[0])
    interpreter.run()
