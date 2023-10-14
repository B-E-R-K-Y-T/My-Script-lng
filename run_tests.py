import os

from interpreter import Interpreter


def files_in_folder_on_pattern(path, file_name):
    """
   Возвращает список определенных файлов в директории.

    :param path:
        Путь до директории, где мы проверяем кол - во файлов.
    :param file_name:
        Строка, которая должна содержаться в имени файла.
    :return:
        Возвращает список таких файлов в директории.
    """

    file_name, count_file = str(file_name), 0
    res = []
    for i in range(len(os.listdir(path))):
        if str(os.listdir(path)[i]).startswith(file_name):
            res.append(str(os.listdir(path)[i]))

    return res


if __name__ == '__main__':
    tests = sorted(files_in_folder_on_pattern('/home/berkyt/PycharmProjects/MyScriptLanguage', 'test'))

    for i in range(1, len(tests)+1):
        TEST = f'test{i}.txt'
        interpreter = Interpreter(TEST)
        interpreter.run()
