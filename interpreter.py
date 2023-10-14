from data.operators import ALL_OPERATORS, END_TRY, CATCH
from tools.debug import print_debug, DEBUG, log
from tools.exceptions.object_exceptions import FunctionException, TypeException, ObjectException
from tools.exceptions.syntax_exceptions import SyntaxException
from tools.parser import (Parser, set_try_catch, get_try_catchs, Function, set_func, get_func, get_table_functions,
                          set_var, delete_var, Var, CONVERT_TABLE, is_var_exists, get_var, get_vars,
                          get_name_and_index_indexing_array, get_num_try_by_key, replace_dict, get_ifs, set_if, get_if)
from tools.token_parser import TokenParser, TokenReader
from tools.types import Int, Line, Boolean
from tools.exceptions.main_exception import MainException, kill_process
from tools.try_catch import Catch, StateCatch
from tools.convert_python_func_to_msl import call_standard_func, find_func, is_func_accepts_inf_args


class Interpreter:
    def __init__(self, path: str, jump_to_num_line: int = 0, end_line: int = ...,
                 is_loop: bool = False, init_calls: bool = True, is_elseif_mode: bool = False, **flags):
        self.file = open(path)
        self.path = path
        self.jump_to_num_line = jump_to_num_line
        self.end_line = end_line
        self.is_loop = is_loop
        self.init_calls = init_calls
        self.is_elseif_mode = is_elseif_mode
        self.tokens = self.get_tokens()

        if init_calls:
            self.save_funcs()
            self.save_ifs()

    def save_ifs(self, jump_line: int = 1, def_if_num: int = 0, flag_is_if: bool = False):
        if_num = def_if_num
        is_if = flag_is_if

        for num_line, line in enumerate(open(self.path)):
            if num_line < jump_line:
                continue

            par = Parser(line)

            if par.is_commentary():
                continue

            if par.is_if():
                if is_if:
                    jump_line = self.save_ifs(num_line, def_if_num=num_line, flag_is_if=False)
                    is_if = False
                    continue
                else:
                    is_if = True

                if_num = num_line
                set_if(f'if_{if_num}', {'if': num_line, 'elseif': [], 'else': ..., 'end_if': ...})
            elif par.is_elseif():
                if_obj = get_ifs()
                if_obj[f'if_{if_num}']['elseif'].append(num_line)
            elif par.is_else():
                if_obj = get_ifs()
                if_obj[f'if_{if_num}']['else'] = num_line
            elif par.is_end_if():
                if_obj = get_ifs()
                if_obj[f'if_{if_num}']['end_if'] = num_line

                if is_if:
                    print_debug(get_ifs())
                    return num_line + 1

    def save_try_catch(self, jump_line: int = 1, def_try_num: int = 0, flag_is_try: bool = False):
        try_num = def_try_num
        is_try = flag_is_try

        for num_line, line in enumerate(open(self.path)):
            if num_line < jump_line:
                continue

            par = Parser(line)

            if par.is_commentary():
                continue

            if par.is_try():
                if is_try:
                    jump_line = self.save_try_catch(num_line, def_try_num=num_line, flag_is_try=False)
                    is_try = False
                    continue
                else:
                    is_try = True

                try_num = num_line
                try_obj = {f'try_{num_line}': {'catchs': [{'num_line': ..., 'obj_exc': ...}]}}
                set_try_catch(f'try_{num_line}', try_obj[f'try_{num_line}'])
            elif par.is_catch():
                try_obj = get_try_catchs()
                try_obj[f'try_{try_num}']['catchs'].append({'num_line': num_line, 'obj_exc': par.get_exception()})
            elif par.is_end_try():
                try_obj = get_try_catchs()
                try_obj[f'try_{try_num}']['end'] = num_line

                if is_try:
                    print_debug(get_try_catchs())
                    return num_line + 1

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
    def is_border(num_line: int) -> bool:
        for attrs in get_table_functions().values():
            borders = attrs['borders']

            if borders[0] < num_line < borders[1] + 1:
                return True

        return False

    def if_worker(self, start_line, end_line=...):
        end_if = None

        for num_line, line in enumerate(open(self.path)):

            if num_line < start_line:
                continue

            par = Parser(line)

            if par.is_commentary():
                continue

            if par.is_end_if():
                end_if = num_line
                break

        if end_if is None:
            raise SyntaxException(f'Not found end if!')
        else:
            if end_line is not ...:
                end_if = end_line

            _interpreter = Interpreter(self.path, start_line, end_if,
                                       is_loop=False, init_calls=False, is_elseif_mode=True)
            _interpreter.run(False)

        return end_if

    def loop_worker(self, start_line: int, start_num: int, end_num: int, name_var: str) -> int:
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
    def save_args_for_call_func(args: list, name_args: list):
        for arg, name_arg in zip(args, name_args):
            var = Var(arg)
            if var.get_type(arg) not in [Int, Line, Boolean]:
                raise TypeException(f'{arg} is invalid!')
            else:
                set_var(name_arg, CONVERT_TABLE[var.get_type(arg).__name__](arg))

    @staticmethod
    def count_send_args_is_valid(to_args: list, from_args: list) -> bool:
        if len(to_args) == len(from_args):
            return True
        return False

    @staticmethod
    def check_valid_exception(num_line: int, line: str, exceptions: dict):
        for name_try in exceptions:
            if exceptions[name_try].get('end') is None:
                kill_process(num_line, line, SyntaxException(f'Not found "{END_TRY}" operator!'))
            elif len(exceptions[name_try].get('catchs')) == 1:
                kill_process(num_line, line, SyntaxException(f'Not found "{CATCH}" operator!'))

    def handler_exception(self, num_line_exc: int, exc: MainException) -> StateCatch:
        exceptions = get_try_catchs()

        for exc_key in exceptions:

            start = int(exc_key[4:])
            end = int(exceptions[exc_key]['catchs'][1]['num_line'])
            jump = int(exceptions[exc_key]['end'])

            print_debug('DEBUG: ', start, end, jump)

            if start <= num_line_exc <= end:
                print_debug('DEBUG: ', exc_key)
                print_debug('DEBUG: ', f'{num_line_exc=}', f'{start=}, {end=}, {jump=}', start <= num_line_exc <= end)
                e = Catch(exc)
                exc_name = str(exc.__class__.__name__)

                print_debug(exc_name not in e.get_handlers(exceptions, exc_key))

                if exc_name not in e.get_handlers(exceptions, exc_key):
                    for _e in exceptions:
                        if get_num_try_by_key(exc_key) > get_num_try_by_key(_e):
                            continue

                        if exceptions[_e]['end'] < exceptions[exc_key]['end']:
                            if exc_name not in e.get_handlers(exceptions, _e):
                                return StateCatch.FAILED
                            else:
                                end = int(exceptions[_e]['catchs'][1]['num_line'])
                                jump = int(exceptions[exc_key]['end'])
                else:
                    end = int(exceptions[exc_key]['catchs'][1]['num_line'])
                    jump = int(exceptions[exc_key]['end'])

                _interpreter = Interpreter(self.path, end + 1, end + 2, init_calls=False)
                _interpreter.run(check_border=False)

                self.jump_to_num_line = jump + 1

                return StateCatch.PROCESSED

        return StateCatch.FAILED

    def get_tokens(self):
        tokens = []

        for num_line, line in enumerate(open(self.path)):
            if line.isspace():
                continue

            for token in line.split(' '):
                tokens.append([token, line, num_line])

        return tokens

    # TODO: Доделать!
    @log
    def get_expressions(self):
        expressions = []

        tr = TokenReader(self.tokens)

        print(tr.get_all_values_arrays())

    @staticmethod
    def bool_expr_handler(expr: str) -> bool:
        var = get_var(expr)

        if var.get_real_value():
            return True
        else:
            return False

    def run(self, check_border: bool = True):
        for num_line, line in enumerate(self.file):
            vars_in_line = []
            num_line += 1

            if num_line < self.jump_to_num_line:
                continue

            print_debug(f'Interpreter ID: {"".join(s for s in str(self) if s.isdigit())}, {num_line=}')

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

                print_debug(num_line, line)

                if par.is_variable():
                    var = Var(line)
                    var.save_var(var.get_key(), var.get_str_literal_value())
                elif par.is_try():
                    self.save_try_catch(num_line - 1, def_try_num=num_line - 1, flag_is_try=False)
                    self.check_valid_exception(num_line, line, get_try_catchs())
                # TODO: Доделать
                elif par.is_indexing():
                    name, index = get_name_and_index_indexing_array(line)

                    var = get_var(name)[index]
                    print(var)
                    vars_in_line.append(var)
                elif par.is_calculated_variable():
                    var = Var(line)
                    _par = Parser(var.get_str_literal_value())

                    if _par.is_added():
                        _line = var.get_str_literal_value().replace(' ', '')
                        a, b = _line.split('+')

                        res = None

                        if is_var_exists(a) and is_var_exists(b):
                            if isinstance(get_var(a), Int) and isinstance(get_var(b), Int):
                                res = int(get_var(a).get_str_literal_value()) + int(get_var(b).get_str_literal_value())

                        if res is None:
                            raise ObjectException(f'The expression returned None.')

                    var.save_var(var.get_key(), str(res))
                elif par.is_added():
                    _line = line.replace(' ', '')
                    a, b = _line.split('+')

                    res = None

                    if Int.check_type(a) and Int.check_type(b):
                        res = int(get_var(a)) + int(get_var(b))
                elif par.is_start_loop():
                    start, stop = par.count_repeat_in_loop()
                    var_in_loop = par.get_var_in_loop()

                    self.jump_to_num_line = self.loop_worker(num_line + 1, start, stop, var_in_loop) + 2
                elif par.is_print():
                    print(*par.get_data_from_print())
                elif par.is_call_func():
                    func_name = par.get_name_call_func()

                    print_debug(num_line, line)
                    print_debug('RUN_TIME:\n\tCALL_FUNCTION\n\t\t', line)
                    print_debug(get_table_functions())

                    func_args = Function(line).get_args()

                    if find_func(func_name):
                        if not is_func_accepts_inf_args(find_func(func_name)['args']):
                            if not self.count_send_args_is_valid(func_args, list(find_func(func_name)['args'])):
                                raise FunctionException(f'{func_args}({len(func_args)}) arguments were passed, and '
                                                        f'{list(find_func(func_name)["args"])}'
                                                        f'({len(list(find_func(func_name)["args"]))})'
                                                        f'were expected')
                        call_standard_func(func_name, *func_args)
                        continue

                    func = get_func(Function(line).get_name_call_func())

                    if not self.count_send_args_is_valid(func_args, list(func['args'].keys())):
                        raise FunctionException(f'{func_args}({len(func_args)}) arguments were passed, and '
                                                f'{list(func["args"].keys())}({len(list(func["args"].keys()))}) '
                                                f'were expected')

                    self.save_args_for_call_func(func_args, func['args'].keys())

                    _interpreter = Interpreter(self.path, func['borders'][0], func['borders'][1])
                    _interpreter.run(check_border=False)

                    print_debug(get_vars())

                    for arg in func['args'].keys():
                        delete_var(arg)

                    print_debug(get_vars())
                elif par.is_func():
                    func_name = par.get_name_defined_func()
                    if find_func(func_name):
                        raise FunctionException(f'This function: "{func_name}" is standard! It cannot be overridden!')
                elif par.is_catch():
                    continue
                elif par.is_end_try():
                    continue
                elif par.is_elseif():
                    if self.is_elseif_mode:
                        expr = par.get_if_expr()
                        res = self.bool_expr_handler(expr)

                        if res:
                            self.jump_to_num_line = self.if_worker(num_line + 1, end_line=self.end_line) + 2
                            return True
                        else:
                            return False
                    else:
                        continue
                elif par.is_else():
                    continue
                elif par.is_if():
                    expr = par.get_if_expr()
                    res = self.bool_expr_handler(expr)
                    elseif = get_ifs()[f'if_{num_line - 1}']['elseif']
                    _else = get_ifs()[f'if_{num_line - 1}']['else']
                    end_if = get_ifs()[f'if_{num_line - 1}']['end_if']

                    default_end_line_elif = _else if _else is not ... else end_if

                    if res:
                        self.jump_to_num_line = self.if_worker(num_line + 1) + 2
                    elif elseif:
                        res_elseif = False

                        for idx, border in enumerate(elseif):
                            # print(border+1, elseif, num_line, line)
                            if not res_elseif:
                                _interpreter = Interpreter(self.path,
                                                           border+1,
                                                           elseif[idx+1] if len(elseif) < idx+1 else default_end_line_elif+1,
                                                           is_loop=False,
                                                           init_calls=False,
                                                           is_elseif_mode=True)
                                res_elseif = _interpreter.run(False)
                        self.jump_to_num_line = get_if(f'if_{num_line - 1}')['end_if'] + 1
                    else:
                        self.jump_to_num_line = get_if(f'if_{num_line - 1}')['end_if'] + 1

                    if _else is not ...:
                        _interpreter = Interpreter(self.path,
                                                   _else+1,
                                                   end_if+1,
                                                   is_loop=False,
                                                   init_calls=False)
                        _interpreter.run(False)
                        self.jump_to_num_line = get_if(f'if_{num_line - 1}')['end_if'] + 1

                elif par.is_end_if():
                    continue
                else:
                    if replace_dict(line, {'\n': '', ' ': ''}) not in ALL_OPERATORS:
                        raise SyntaxException(f'Invalid syntax: {line=}')
            except MainException as e:
                if DEBUG:
                    raise

                res = self.handler_exception(num_line, e)

                if res == StateCatch.FAILED:
                    kill_process(num_line, line, e)

                continue

        print_debug(get_vars())
        print_debug(get_table_functions())
        print_debug(get_try_catchs())


if __name__ == '__main__':
    # commands = input('Enter path to script >>>').split(' ')

    TEST = 'test14.txt'

    interpreter = Interpreter(TEST)
    interpreter.run()
