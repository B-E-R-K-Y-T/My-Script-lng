from tools.debug import print_debug, DEBUG
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
        self.save_funcs()

    def save_funcs(self):
        name_func = ''

        for num_line, line in enumerate(open(self.path)):
            par = Parser(line)

            if par.is_func():
                func = Function(line)
                name_func = func.get_name_func()
                set_func(name_func, (num_line+1, 0))
            elif par.is_end_func():
                func = get_func(name_func)
                set_func(name_func, (func[0], num_line))

    @staticmethod
    def is_border(num_line):
        num_line = int(num_line)
        for borders in get_table_functions().values():
            if borders[0] < num_line < borders[1] + 1:
                return True

    def loop_worker(self, start_line, start_num, end_num, name_var):
        end_loop = None

        for num_line, line in enumerate(open(self.path)):

            if num_line < start_line:
                continue

            par = Parser(line)

            if par.is_commentary():
                continue

            if par.is_end_loop():
                end_loop = num_line
                break

        if end_loop is None:
            raise SyntaxException(f'Not found end loop!')
        else:
            for i in range(start_num, end_num + 1):
                set_var(name_var, Int(str(i)))
                _interpreter = Interpreter(self.path, start_line, end_loop, is_loop=True)
                _interpreter.run(False)

            delete_var(name_var)
        return end_loop

    def run(self, check_border: bool = True):
        for num_line, line in enumerate(self.file):
            num_line += 1

            if num_line < self.jump_to_num_line:
                continue

            if self.end_line is not ...:
                if num_line > self.end_line:
                    return

            if self.is_border(num_line) and check_border:
                continue

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

                    self.jump_to_num_line = self.loop_worker(num_line, start, stop, var_in_loop) + 2
                elif par.is_print():
                    print(*par.get_data_from_print())
                elif par.is_call_func():
                    print_debug(num_line, line)
                    print_debug('CALL_FUNCTION', line)
                    print_debug(get_table_functions())

                    func = get_func(Function(line).get_name_call_func())

                    _interpreter = Interpreter(self.path, func[0], func[1])
                    _interpreter.run(check_border=False)
                elif par.is_func():
                    continue
                else:
                    if not self.is_loop and line.replace('\n', '') not in ALL_OPERATORS:
                        raise SyntaxException(f'Invalid syntax: {line=}')
            except MainException as e:
                print(f'{num_line=}\n\t{e}')
                if DEBUG:
                    raise
                break

        print_debug(get_vars())


if __name__ == '__main__':
    # commands = input('>>>').split(' ')

    TEST = '/home/berkyt/PycharmProjects/MyScriptLanguage/test3.txt'

    interpreter = Interpreter(TEST)
    interpreter.run()
