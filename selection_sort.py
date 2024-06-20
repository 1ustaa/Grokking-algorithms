def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    """
    Алгоритм сортировки выбором
    :param arr: Массив чисел
    :return: Возвращает отсортирпованный массив от меньшего к большему
    """
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


def test_selection_sort(algorithm):
    print("Тестируем:", algorithm.__doc__)

    print("test case #1 ", end="")
    arr = [2, 4, 5, 1, 0, 3]
    res = algorithm(arr)
    print("Ok" if res == [0, 1, 2, 3, 4, 5] else "False")

    print("test case #2 ", end="")
    arr = [1000, -3000, 20, -1]
    res = algorithm(arr)
    print("Ok" if res == [-3000, -1, 20, 1000] else "False")

    print("test case #3 ", end="")

test_selection_sort(selection_sort)
