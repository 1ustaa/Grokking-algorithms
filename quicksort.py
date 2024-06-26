def quicksort(arr):
    """
    Сортирует элементыт в массиве от большего к меньшему
    :param arr: Массив чисел
    :return: Выводит отсортированный массив
    """
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        greater = [i for i in arr if i > pivot]
        less = [i for i in arr if i < pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


def test_quicksort(algorithm):
    print("Тестируем: ", algorithm.__doc__)

    print("test case #1: ", end="")
    arr = [10, 1, 3, 2, 9]
    res = algorithm(arr)
    print("Ok" if res == [1, 2, 3, 9, 10] else "False")

    print("test case #2: ", end="")
    arr = [1, 11, 3, -2, 9]
    res = algorithm(arr)
    print("Ok" if res == [-2, 1, 3, 9, 11] else "False")

    print("test case #3: ", end="")
    arr = [10, 0, -5, 4]
    res = algorithm(arr)
    print("Ok" if res == [-5, 0, 4, 10] else "False")


test_quicksort(quicksort)