def fact(num):
    """
    Факторил
    :param num: Целое, натуральное число
    :return:Возвращает факториал числа
    """
    if num == 1:
        return num
    else:
        return num * fact(num-1)


def test_fact(algorithm):
    print("Тестируем: ", algorithm.__doc__)

    print("test case #1 ", end="")
    num = 1
    res = algorithm(num)
    print("Ok" if res == 1 else "False")

    print("test case #2 ", end="")
    num = 5
    res = algorithm(num)
    print("Ok" if res == 120 else "False")

    print("test case #3 ", end="")
    num = 3
    res = algorithm(num)
    print("Ok" if res == 6 else "False")


test_fact(fact)
