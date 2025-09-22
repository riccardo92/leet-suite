def nested_list_comparator(l1: list, l2: list) -> bool:
    """Are a and b equal in anything but order?

    Args:
        a (list): A list of lists
        b (list): A list of lists

    Returns:
        bool: whether the lists are equal
    """
    return sorted([sorted(a) for a in l1]) == sorted([sorted(b) for b in l2])
