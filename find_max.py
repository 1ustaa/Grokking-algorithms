def find_max(arr):
    """
    Выводит наибольшое число из массива
    :param arr: Массив чисел
    :return: Наибольшое число из массива
    """
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    else:
        sub_max = find_max(arr[1:])
        return arr[0] if arr[0] > sub_max else sub_max


def test_find_max(algorith):
    print("Тестируем: ", algorith.__doc__)

    arr = [10001, 4, 3, 100, -111, 10, 1000]
    res = algorith(arr)
    print("test case #1: ", end="")
    print("Ok" if res == max(arr) else "False")

    arr = [1, 3, -100, -111, 10]
    res = algorith(arr)
    print("test case #2: ", end="")
    print("Ok" if res == max(arr) else "False")

    arr = [1, 3, 100, -111, 10, 11]
    res = algorith(arr)
    print("test case #3: ", end="")
    print("Ok" if res == max(arr) else "False")


test_find_max(find_max)


