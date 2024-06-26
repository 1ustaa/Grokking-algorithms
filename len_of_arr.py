def len_of_arr(arr):
    """
    Выводит колличество элементов в списке
    :param arr: Список
    :return: Колличесвто элементов в массиве
    """
    if not arr:
        return 0
    else:
        return 1 + len_of_arr(arr[1:])


def test_len_of_arr(algorithm):
    print("Тестируем: ", algorithm.__doc__)

    arr = [0] * 10
    res = algorithm(arr)
    print("test case #1: ", end="")
    print("Ok" if res == len(arr) else "False")

    arr = [0] * 125
    res = algorithm(arr)
    print("test case #2: ", end="")
    print("Ok" if res == len(arr) else "False")

    arr = [0] * 100
    res = algorithm(arr)
    print("test case #3: ", end="")
    print("Ok" if res == len(arr) else "False")


test_len_of_arr(len_of_arr)
