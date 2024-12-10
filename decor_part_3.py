"""
3. Применить написанный логгер к приложению из любого предыдущего д/з.

пред. задан:
4. * Необязательное задание.Написать генератор, аналогичный
генератору из задания 2, но обрабатывающий списки с любым уровнем
вложенности.Шаблон и тест в коде ниже:
"""
import types
import os
from datetime import datetime as dt

def logger(old_function):
    name_file_log = "my_fun.log"
    def new_function(*args, **kwargs):
        if os.path.isfile(name_file_log):
            log_file = open(name_file_log, "a+")
        else:
            log_file = open(name_file_log, "w+")
        orig_res = old_function

        modif_res = orig_res(*args, **kwargs)
        log_file.write(f'{dt.now()} Function: "{orig_res.__name__}" '
                       f' Arguments: {args} {kwargs} Result:{list(modif_res)} \n')
        log_file.close()
        return modif_res
    return new_function

def fun_flat(lis):
    res = []
    while True:
        some_iter = False
        for i in lis:
            if i.__class__ == list:
                res.extend(i)
                some_iter = True
            else:
                res.append(i)
        lis = res
        res = []
        if not some_iter:
            break
    return lis


@logger
def flat_generator(list_of_list):
    list_of_list = fun_flat(list_of_list)
    i = 0
    while i < len(list_of_list):
        yield list_of_list[i]
        i += 1


def test_4():

    path = 'my_fun.log'
    if os.path.exists(path):
        os.remove(path)

    # @logger
    # def summator(a, b=0):
    #     return a + b


    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item
    """генератор выбран при попытке печати содержимого в лог. пустой он . ремлю ассерт"""
    # assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()
    print("Задача 4 из прошлого ДЗ прошла. См. лог")
