DEBUG = False


def print_debug(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)


def log(func):
    def wrapper(*args, **kwargs):
        print_debug(f'INTERPRETER:\n\tCALL FUNCTION:\n\t\t{func.__name__}')
        res = func(*args, **kwargs)

        return res

    return wrapper
