def numbers_strip(list_number: list, n: int = 1,*, copy: bool = False) -> list:
    """ Возвращает исходный измененный обьект списка или измененную копию """
    if not copy:
        while n > 0:
            n -= 1
            list_number.remove(min(list_number))
            list_number.remove(max(list_number))
			
        return list_number
    else:
        list_number_copy = list_number.copy()
        while n > 0:
            n -= 1
            list_number_copy.remove(min(list_number_copy))
            list_number_copy.remove(max(list_number_copy))
			
        return list_number_copy

# >>> sample = [10, 20, 30, 40, 50]
# >>> sample_stripped = numbers_strip(sample, 2, copy=True)
# >>> sample_stripped
# [30]
# >>> sample is sample_stripped
# False
# >>> ^Z

# S>>> sample = [1, 2, 3, 4]
# S>>> sample_stripped = numbers_strip(sample)
# S>>> sample_stripped
# S[2, 3]
# S>>> sample is sample_stripped
# STrue