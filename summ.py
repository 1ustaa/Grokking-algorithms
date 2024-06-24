def summ(arr):
    """
    Принимает массив чисел и выводит их сумму
    :param arr: массив чисел
    :return: выводит сумму чисел
    """
    if not arr:
        return 0
    else:
        num = arr.pop()
        return num + summ(arr)


def test_summ(algorithm):
    print("Тестируем ", algorithm.__doc__)

    print("test case #1: ", end="")
    arr = [0, 2, 3, 5]
    res = algorithm(arr)
    print("Ok" if res == 10 else "False")

    print("test case #2: ", end="")
    arr = [-1, -2, 3, 50]
    res = algorithm(arr)
    print("Ok" if res == 50 else "False")

    print("test case #3: ", end="")
    arr = [0, 1, 1, 1]
    res = algorithm(arr)
    print("Ok" if res == 3 else "False")


test_summ(summ)
