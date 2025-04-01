def find(search_list, value):
    """Find the index of a value in a sorted list using binary search.

    :param search_list: list - A sorted list of elements to search.
    :param value: int - The value to find in the list.
    :return: int - The index of the value in the list.
    :raises ValueError: If the value is not in the list.
    """
    left, right = 0, len(search_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if search_list[mid] == value:
            return mid
        if search_list[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    raise ValueError("value not in array")
