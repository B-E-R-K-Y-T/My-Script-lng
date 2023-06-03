from msl_standard_library.math import Sum, Add, Len, Max
from msl_standard_library.utils import Print
from msl_standard_library.operation_system import OS_command
from tools.types import Int, Line
from tools.parser import Var


_tree_standard_functions = {
    Add.__name__: {'func': Add, 'args': ['a', 'b']},
    Sum.__name__: {'func': Sum, 'args': ['a', 'b', 'c']},
    Len.__name__: {'func': Len, 'args': ['seq']},
    Max.__name__: {'func': Max, 'args': [-1]},
    OS_command.__name__: {'func': OS_command, 'args': ['command']},
    Print.__name__: {'func': Print, 'args': [-1]},
}
MSL_CONVERT_TABLE = {
    Int.__name__: int,
    Line.__name__: str,
}


def call_standard_func(name: str, *args):
    res = []

    for arg in args:
        var = Var(arg)
        if var.get_type(arg) in [Int, Line]:
            _var = MSL_CONVERT_TABLE[var.get_type(arg).__name__](arg)

            if isinstance(_var, str):
                _var = _var.replace('"', '')

            res.append(_var)

    _tree_standard_functions[name]['func'](*res)


def find_func(name: str):
    return _tree_standard_functions.get(name)


def is_func_accepts_inf_args(args_signature: list) -> bool:
    if len(args_signature) == 1 and args_signature[0] == -1:
        return True
    return False
