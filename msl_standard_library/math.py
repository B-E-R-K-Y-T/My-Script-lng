def Sum(a, b, c):
    print(sum([a, b, c]))


def Add(a, b):
    print(a + b)


def Len(seq):
    print(len(seq))


def Max(*args):
    """

    :param args: Принимает неограниченное кол-во параметров.
    :return:
        Возвращает максимальный элемент.
    """
    print(max(args))


if __name__ == '__main__':
    Sum(1, 2, 3)

