from tools.exceptions.main_exception import kill_process, MainException


def Print(*args):
    print(*args)


def Kill():
    kill_process(num_line=-1, line='unknown')
