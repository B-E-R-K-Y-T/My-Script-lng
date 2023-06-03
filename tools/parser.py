import re

from data.operators import *
from tools.exceptions.object_exceptions import ObjectException
from tools.exceptions.syntax_exceptions import SyntaxException
from tools.types import *

_tree_variables = {}


def get_vars():
    return _tree_variables


def get_var(key):
    if not is_var_exists(key):
        raise ObjectException(f'This variable "{key}" not exist!')
    else:
        return _tree_variables[key]


def set_var(key, value):
    key = key
    _tree_variables[key] = value


def delete_var(key):
    del _tree_variables[key]


def is_var_exists(key):
    var = _tree_variables.get(key)

    return False if var is None else True


class Var:
    def __init__(self, line_var: str):
        self.key, self.value = self.split_str_to_key_value(line_var)

    @staticmethod
    def split_str_to_key_value(line_var: str):
        line_var = line_var.replace(' ', '')
        index_var = line_var.find(EQUAL) + 1
        key, value = line_var[3:index_var-1], line_var[index_var:-2]

        return key, value

    def get_key(self):
        return self.key

    def get_value(self):
        return self.value

    @staticmethod
    def get_type(value):
        if Int.is_int(value):
            return Int
        elif Line.is_line(value):
            return Line
        raise TypeException(f'Invalid type! {value=}')

    def save_var(self, key, value):
        if is_var_exists(key):
            raise ObjectException(f'This variable "{key}" already exist!')
        else:
            if self.get_type(value) == Int:
                _tree_variables[key] = Int(value)
            elif self.get_type(value) == Line:
                _tree_variables[key] = Line(value)
            else:
                raise TypeException(f'Error type!')


class Parser:
    def __init__(self, line: str):
        self.line = line

    def is_variable(self):
        if re.findall(pattern=r'[ ]*var[ ]+\w+[ ]+=[ ]+[\w\d\"]+;', string=self.line):
            return True
        return False

    def is_calculated_variable(self):
        if re.findall(pattern=r'[ ]*var[ ]+\w+[ ]+=[ ]+[\w\d]+[ ]*\+[ ]*[\w\d]+;', string=self.line):
            return True
        return False

    def is_added(self):
        if re.findall(pattern=r'[\w\d]+[ ]*\+[ ]*[\w\d]+', string=self.line):
            return True
        return False

    def is_start_loop(self):
        if re.findall(pattern=r'[ ]*for[ ]+\w+=\(\d+,\d+\)[ ]+do', string=self.line):
            return True
        return False

    def is_end_loop(self):
        if re.findall(pattern=r'[ ]*end_loop', string=self.line):
            return True
        return False

    def is_commentary(self):
        if re.findall(pattern=r'[ ]*#.+', string=self.line):
            return True
        return False

    def count_repeat_in_loop(self):
        start, stop = re.findall(pattern=r'\d+,\d+', string=self.line)[0].split(',')

        return int(start), int(stop)

    def get_var_in_loop(self):
        return 'loop_' + re.findall(pattern=r'\w+=', string=self.line)[0].replace('=', '')

    def is_print(self):
        if re.findall(pattern=r'[ ]*print[ ]+[\w,\" !№;%:?*()_+]+;', string=self.line):
            return True
        return False

    def get_data_from_print(self):
        args = self.line[:-2].split('print')
        args = [arg.replace('\n', '') for arg in args if not arg.isspace() and arg][0].split(',')

        res = []

        for r in args:
            if '"' not in r:
                r = r.replace(' ', '')

                res.append(get_var(r).get_value())
            else:

                idx_l = r.find('"')
                idx_r = r.rfind('"')

                r = r[idx_l+1:idx_r]

                res.append(r)

        return res


if __name__ == '__main__':
    p = Parser('var x = 1;')
    p = Parser('var x = "sd";')
    p = Parser('var        x          = 1;')

    test = 'var        xsdsdsdawes          = 2343241;'

    print(p.is_variable())

    v = Var(test)
    print(v.get_value())
    print(v.get_key())
    v = Var('var d = x + y;')
    print(v.get_value())
    print(v.get_key())

    p = Parser('1+ +1')
    print(p.is_added())
    p = Parser('for     idf=(1,100)      do')
    print(*p.count_repeat_in_loop())
    print(p.get_var_in_loop())
