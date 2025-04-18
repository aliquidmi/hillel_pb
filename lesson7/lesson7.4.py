def common_elements():
    first = list(range(0, 101, 3))
    second = list(range(0, 101, 5))
    set1 = set(first)
    set2 = set(second)
    res = set1.intersection(set2)
    return res

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
