def binary_search(list, item):
    """
    Функция бинарного поиска
    :param list: Отсортированный массив
    :param item: Искомый элемент массива
    :return: Возвращает id элемента в массиве
    """
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) //  2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
        else:
            return None


def test_binary_search(sort_algorithm):
    print("Тестируем:", sort_algorithm.__doc__)
    print("tastecase #1:", end="")
    list = [1, 2, 3, 4, 5]
    item = 2
    res = sort_algorithm(list, item)
    print("Ok" if res == 1 else "Fail")

    print("tastecase #2:", end="")
    list = [1, 2, 3, 4, 5]
    item = 100
    res = sort_algorithm(list, item)
    print("Ok" if res is None else "Fail")

    print("tastecase #3:", end="")
    list = [11, 12, 13, 14, 15]
    item = 15
    res = sort_algorithm(list, item)
    print("Ok" if res == 4 else "Fail")


test_binary_search(binary_search)
