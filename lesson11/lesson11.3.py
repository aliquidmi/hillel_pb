def is_even(number: int) -> bool:
    n = str(number)
    n_list = ['0', '2', '4', '6', '8']
    return n[-1] in n_list

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
