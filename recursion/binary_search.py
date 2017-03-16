def binary_search(data, target, low, high):
    """
    Return True if target is found in indicated portion of a Python list.

    The search only considers the portion from data[low] to data[high] inclusive.
    """
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target > data[mid]:
            return binary_search(data, target, mid + 1, high)
        else:
            return binary_search(data, target, low, mid - 1)


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if binary_search(l, 11, 0, len(l) - 1):
        print("There is 11 in the list")
    else:
        print("There isn't 11 in the list")

    if binary_search(l, 7, 0, len(l) - 1):
        print("There is 7 in the list")
    else:
        print("There isn't 7 in the list")





