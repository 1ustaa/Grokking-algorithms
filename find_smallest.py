def find_smallest(arr: list):
    """
    Алгоритм поиска наименьшего числа
    Функция берет массив чисел и возвращает индекс наименьшего элемента
    :param arr: Массив чисел
    :return: Возвращает индекс наименьшего числа в массиве
    """
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def test_find_smallest(algorithm):
    print(f"Тестируем: {algorithm.__doc__}")

    print("tastecase #1:", end="")
    arr = [0, 100, -100, 21, 12, -99]
    res = algorithm(arr)
    print("Ok" if res == 2 else "Fail")

    print("tastecase #2:", end="")
    arr = [-1010, 100, -100, 21, 12, -99]
    res = algorithm(arr)
    print("Ok" if res == 0 else "Fail")

    print("tastecase #3:", end="")
    arr = [1, 100, 101, 21, 12, -99]
    res = algorithm(arr)
    print("Ok" if res == 5 else "Fail")


test_find_smallest(find_smallest)
