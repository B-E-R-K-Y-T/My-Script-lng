import sys

from data.operators import ALL_OPERATORS
from tools.debug import print_debug, DEBUG
from tools.exceptions.object_exceptions import FunctionException, TypeException, ObjectException
from tools.exceptions.syntax_exceptions import SyntaxException
from tools.parser import (Parser, set_try_catch, get_try_catchs, Function, set_func, get_func, get_table_functions,
                          set_var, delete_var, Var, CONVERT_TABLE, is_var_exists, get_var, get_vars)
from tools.types import Int, Line
from tools.exceptions.main_exception import MainException
from tools.try_catch import Catch, StateCatch
from colorama import init
from colorama import Fore
from tools.convert_python_func_to_msl import call_standard_func, find_func, is_func_accepts_inf_args

init()


class Interpreter:
    def __init__(self, path: str, jump_to_num_line: int = 0, end_line: int = ...,
                 is_loop: bool = False, init_calls: bool = True, **flags):
        self.file = open(path)
        self.path = path
        self.jump_to_num_line = jump_to_num_line
        self.end_line = end_line
        self.is_loop = is_loop
        self.init_calls = init_calls
        if init_calls:
            self.save_funcs()
            self.save_try_catch()

    def save_try_catch(self):
        try_num = 0

        for num_line, line in enumerate(open(self.path)):
            par = Parser(line)

            if par.is_commentary():
                continue

            if par.is_try():
                try_num = num_line
                try_obj = {f'try_{num_line}': {'catchs': [{'num_line': ..., 'obj_exc': ...}]}}
                set_try_catch(f'try_{num_line}', try_obj[f'try_{num_line}'])
            elif par.is_catch():
                try_obj = get_try_catchs()
                try_obj[f'try_{try_num}']['catchs'].append({'num_line': num_line, 'obj_exc': par.get_exception()})
            elif par.is_end_try():
                try_obj = get_try_catchs()
                try_obj[f'try_{try_num}']['end'] = num_line
                break
            print_debug(get_try_catchs())

    def save_funcs(self):
        name_func = ''

        for num_line, line in enumerate(open(self.path)):
            par = Parser(line)

            if par.is_func():
                func = Function(line)
                name_func = func.get_name_func()

                args = {'func_' + name: ... for name in func.get_name_args() if name}

                set_func(name_func, borders=(num_line + 1, 0), args=args)
            elif par.is_end_func():
                func = get_func(name_func)

                set_func(name_func, (func['borders'][0], num_line), func['args'])

    @staticmethod
    def is_border(num_line):
        num_line = int(num_line)
        for attrs in get_table_functions().values():
            borders = attrs['borders']

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
                _interpreter = Interpreter(self.path, start_line, end_loop, is_loop=True, init_calls=False)
                _interpreter.run(False)

            delete_var(name_var)
        return end_loop

    @staticmethod
    def save_args_for_call_func(args, name_args):
        for arg, name_arg in zip(args, name_args):
            var = Var(arg)
            if var.get_type(arg) not in [Int, Line]:
                raise TypeException(f'{arg} is invalid!')
            else:
                set_var(name_arg, CONVERT_TABLE[var.get_type(arg).__name__](arg))

    @staticmethod
    def count_send_args_is_valid(to_args, from_args):
        if len(to_args) == len(from_args):
            return True
        return False

    def handler_exception(self, num_line_exc: int, exc: MainException):
        exceptions = get_try_catchs()
        for exc_key in exceptions:
            start, end = int(exc_key[4:]), int(exceptions[exc_key]['catchs'][1]['num_line'])

            if start <= num_line_exc <= end:
                e = Catch(exc)
                exc_name = str(exc.__class__.__name__)

                if exc_name not in e.get_handlers(exceptions):
                    return StateCatch.FAILED

                start, end, jump = e.handler_error(e.get_handlers(exceptions))

                _interpreter = Interpreter(self.path, start, end, init_calls=False)
                _interpreter.run(check_border=False)

                self.jump_to_num_line = jump

                return StateCatch.PROCESSED

        return StateCatch.FAILED

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

                        if res is None:
                            raise ObjectException(f'The expression returned None.')

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
                    func_name = par.get_name_call_func()

                    print_debug(num_line, line)
                    print_debug('CALL_FUNCTION', line)
                    print_debug(get_table_functions())

                    func_args = Function(line).get_args()

                    if find_func(func_name):
                        if not is_func_accepts_inf_args(find_func(func_name)['args']):
                            if not self.count_send_args_is_valid(func_args, list(find_func(func_name)['args'])):
                                raise SyntaxException(f'{func_args}({len(func_args)}) arguments were passed, and '
                                                      f'{list(find_func(func_name)["args"])}'
                                                      f'({len(list(find_func(func_name)["args"]))})'
                                                      f'were expected')
                        call_standard_func(func_name, *func_args)
                        continue

                    func = get_func(Function(line).get_name_call_func())

                    if not self.count_send_args_is_valid(func_args, list(func['args'].keys())):
                        raise SyntaxException(f'{func_args}({len(func_args)}) arguments were passed, and '
                                              f'{list(func["args"].keys())}({len(list(func["args"].keys()))}) '
                                              f'were expected')

                    self.save_args_for_call_func(func_args, func['args'].keys())

                    _interpreter = Interpreter(self.path, func['borders'][0], func['borders'][1])
                    _interpreter.run(check_border=False)
                elif par.is_func():
                    func_name = par.get_name_defined_func()
                    if find_func(func_name):
                        raise FunctionException(f'This function: "{func_name}" is standard! It cannot be overridden!')
                elif par.is_catch():
                    continue
                else:
                    if not self.is_loop and line.replace('\n', '') not in ALL_OPERATORS:
                        raise SyntaxException(f'Invalid syntax: {line=}')
            except MainException as e:
                if DEBUG:
                    raise

                res = self.handler_exception(num_line, e)

                if res == StateCatch.FAILED:
                    print(Fore.RED + f'{num_line=}, {line=}\n\t{e}')
                    sys.exit()

                continue

        print_debug(get_vars())


if __name__ == '__main__':
    commands = input('Enter path to script >>>').split(' ')

    TEST = f'/home/berkyt/PycharmProjects/MyScriptLanguage/test7.txt'

    interpreter = Interpreter(commands[0])
    interpreter.run()
