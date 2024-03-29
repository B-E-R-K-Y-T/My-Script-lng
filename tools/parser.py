import re

from data.operators import EQUAL
from tools.exceptions.object_exceptions import ObjectException, TypeException, FunctionException
from tools.types import Int, Line, Array, Type, Boolean

_tree_variables = {}
_tree_functions = {}
_tree_try_catch = {}
_tree_if = {}
CONVERT_TABLE = {
    Int.__name__: Int,
    Line.__name__: Line,
    Boolean.__name__: Boolean,
}


def replace_dict(line: str, dict_words: dict) -> str:
    for old_word, new_word in dict_words.items():
        line = line.replace(str(old_word), str(new_word))

    return line


def get_vars():
    return _tree_variables


def get_name_and_index_indexing_array(value: str) -> tuple[str, int]:
    arr = re.findall(pattern=r'[ ]*[\w\d]+\[[\d]+\]', string=value)

    name, index = re.findall(pattern=r'[\w\d]+', string=arr[0])

    return name, int(index)


def get_var(key: str):
    if not is_var_exists(key):
        raise ObjectException(f'This variable "{key}" not exist!')
    else:
        return _tree_variables[key]


def set_var(key: str, value: Type):
    _tree_variables[key] = value


def delete_var(key: str):
    del _tree_variables[key]


def is_var_exists(key: str) -> bool:
    var = _tree_variables.get(key)

    return False if var is None else True


def get_try_catchs() -> dict:
    return _tree_try_catch


def get_num_try_by_key(key: str) -> int:
    if _tree_try_catch.get(key) is not None:
        if '_' not in key:
            return 0

        idx_end = key.rfind('_')

        return int(key[idx_end + 1:])
    else:
        raise KeyError


def set_try_catch(key: str, value):
    _tree_try_catch[key] = value


def get_ifs() -> dict:
    return _tree_if


def get_if(key: str):
    return _tree_if[key]


def set_if(key, value):
    _tree_if[key] = value


def get_func(key: str) -> dict:
    if not is_func_exists(key):
        raise FunctionException(f'This function: "{key}" not exist!')
    else:
        return _tree_functions[key]


def get_table_functions() -> dict:
    return _tree_functions


def set_func(key, borders: tuple[int, int], args: dict = ...):
    _tree_functions[key] = {'borders': borders, 'args': args}


def delete_func(key: str):
    del _tree_functions[key]


def is_func_exists(key: str) -> bool:
    func = _tree_functions.get(key)

    return False if func is None else True


class Var:
    def __init__(self, line_var: str):
        self.key, self.value = self.split_str_to_key_value(line_var)

    @staticmethod
    def split_str_to_key_value(line_var: str):
        line_var = line_var.replace(' ', '')
        index_var = line_var.find(EQUAL) + 1
        key, value = line_var[3:index_var - 1], line_var[index_var:-2]

        return key, value

    def get_key(self):
        return self.key

    def get_str_literal_value(self):
        return self.value

    @staticmethod
    def get_type(value):
        for t in [Int, Line, Array, Boolean]:
            if t.check_type(value):
                return t

        raise TypeException(f'Invalid type! {value=}')

    def save_var(self, key, value):
        # if is_var_exists(key):
        #     raise ObjectException(f'This variable "{key}" already exist!')
        # else:
        if self.get_type(value) == Int:
            _tree_variables[key] = Int(value)
        elif self.get_type(value) == Line:
            _tree_variables[key] = Line(value)
        elif self.get_type(value) == Array:
            _tree_variables[key] = Array(value)
        elif self.get_type(value) == Boolean:
            _tree_variables[key] = Boolean(value)
        else:
            raise TypeException(f'Error type!')


class Function:
    def __init__(self, line_var: str):
        self.line_var = line_var

    def get_name_func(self):
        name = self.line_var.split('func', 1)
        idx_end = name[1].find('(')

        return ''.join(name[1][:idx_end]).replace(' ', '')

    def get_name_call_func(self):
        idx_end = self.line_var.find('(')

        return self.line_var[:idx_end].replace(' ', '')

    def get_args(self):
        idx_start = self.line_var.find('(')
        idx_end = self.line_var.find(')')

        args = self.line_var[idx_start + 1:idx_end].split(',')
        args = [arg.replace(' ', '') if arg.replace(' ', '').isdigit() else arg for arg in args]

        for index, arg in enumerate(args):
            if '"' in arg:
                if arg.count('"') == 2:
                    _idx_start = arg.find('"')
                    _idx_end = arg.rfind('"')

                    args[index] = arg[_idx_start:_idx_end + 1]

        if len(args) == 1 and not args[0]:
            return []

        return args

    def get_name_args(self):
        idx_start = self.line_var.find('(')
        idx_end = self.line_var.find(')')

        args = self.line_var[idx_start + 1:idx_end].split(',')
        args = [arg.replace(' ', '') for arg in args]

        return args


class Parser:
    def __init__(self, line: str):
        self.line = line.replace('\n', '')

    def is_if(self) -> bool:
        if re.findall(pattern=r'^[ ]*if[ ]+\([ ]*\w+[ ]*\)[ ]+then', string=self.line):
            return True
        return False

    def is_else(self) -> bool:
        if re.findall(pattern=r'^[ ]*else', string=self.line):
            return True
        return False

    def is_elseif(self) -> bool:
        if re.findall(pattern=r'^[ ]*elseif[ ]+\([ ]*\w+[ ]*\)[ ]+then', string=self.line):
            return True
        return False

    def is_try(self) -> bool:
        if re.findall(pattern=r'^[ ]*try[ ]+do', string=self.line) and self.line.endswith('do'):
            return True
        return False

    def is_end_try(self) -> bool:
        if re.findall(pattern=r'^[ ]*end_try', string=self.line):
            return True
        return False

    def is_end_if(self) -> bool:
        if re.findall(pattern=r'^[ ]*end_if', string=self.line):
            return True
        return False

    def get_exception(self) -> bool:
        return re.findall(pattern=r'[ ]*(?<=catch)[ ]*[\w\d]+[ ]*(?=do)', string=self.line)[0].replace(' ', '')

    def is_catch(self) -> bool:
        if re.findall(pattern=r'[ ]*catch[ ]*[\w\d]+[ ]*do', string=self.line) and self.line.endswith('do'):
            return True
        return False

    def is_variable(self) -> bool:
        if re.findall(pattern=r'[ ]*var[ ]+\w+[ ]+=[ ]+[\w\d\"{,}]+;', string=self.line):
            return True
        return False

    def is_calculated_variable(self) -> bool:
        if re.findall(pattern=r'[ ]*var[ ]+\w+[ ]+=[ ]+[\w\d]+[ ]*\+[ ]*[\w\d]+;', string=self.line):
            return True
        return False

    def is_added(self) -> bool:
        if re.findall(pattern=r'[\w\d]+[ ]*\+[ ]*[\w\d]+', string=self.line):
            return True
        return False

    def is_start_loop(self) -> bool:
        if re.findall(pattern=r'[ ]*for[ ]+\w+=\(-?\d+,-?\d+\)[ ]+do', string=self.line):
            return True
        return False

    def is_end_loop(self) -> bool:
        if re.findall(pattern=r'[ ]*end_loop', string=self.line):
            return True
        return False

    def is_commentary(self) -> bool:
        if re.findall(pattern=r'[ ]*#.+', string=self.line):
            return True
        return False

    def count_repeat_in_loop(self) -> tuple:
        start, stop = re.findall(pattern=r'-?\d+,-?\d+', string=self.line)[0].split(',')

        return int(start), int(stop)

    def get_var_in_loop(self) -> str:
        return 'loop_' + re.findall(pattern=r'\w+=', string=self.line)[0].replace('=', '')

    def is_func(self) -> bool:
        if re.findall(pattern=r'[ ]*func[ ]+[\w_]+', string=self.line):
            return True
        return False

    def get_name_call_func(self) -> str:
        func = self.line.replace(' ', '')
        idx_end = func.rfind('(')

        return func[:idx_end]

    def get_name_defined_func(self) -> str:
        name_func = replace_dict(re.findall(pattern=r'[ ]*func[ ]+[\w_]+', string=self.line)[0], {'func': '', ' ': ''})
        return name_func

    def is_end_func(self) -> bool:
        if re.findall(pattern=r'[ ]*end_func', string=self.line):
            return True
        return False

    def is_call_func(self) -> bool:
        if re.findall(pattern=r'[ ]*[\w_]+\([\w_\d, "-]*\);', string=self.line):
            return True
        return False

    def is_print(self) -> bool:
        if re.findall(pattern=r'[ ]*print[ ]+[\w,\" !№;%:?*()_+]+;', string=self.line):
            return True
        return False

    def is_indexing(self) -> bool:
        if re.findall(pattern=r'[ ]*[\w\d]+\[[\d]+\]', string=self.line):
            return True
        return False

    def get_if_expr(self):
        expr = re.findall(pattern=r'\([\d\w]+\)', string=self.line)[0]

        return expr[1:-1]

    def get_data_from_print(self) -> list:
        args = self.line[:-1].split('print')
        args = [arg for arg in args if not arg.isspace() and arg][0].split(',')

        res = []

        for r in args:
            if '"' not in r:
                r = r.replace(' ', '')

                var = get_var(r).get_str_literal_value()

                if isinstance(var, str):
                    var = var.replace('"', '')

                res.append(var)
            else:
                idx_l = r.find('"')
                idx_r = r.rfind('"')

                r = r[idx_l + 1:idx_r]

                res.append(r)

        return res


if __name__ == '__main__':
    p = Parser('var x = 1;')
    p = Parser('var x = "sd";')
    p = Parser('var        x          = 1;')

    test = 'var        xsdsdsdawes          = 2343241;'

    print(p.is_variable())

    v = Var(test)
    print(v.get_str_literal_value())
    print(v.get_key())
    v = Var('var d = x + y;')
    print(v.get_str_literal_value())
    print(v.get_key())

    p = Parser('1+ +1')
    print(p.is_added())
    p = Parser('for     idf=(1,100)      do')
    print(*p.count_repeat_in_loop())
    print(p.get_var_in_loop())

    test = 'var arr = {1,2,3};'

    v = Var(test)
    print(v.get_str_literal_value())
    print(v.get_key())
