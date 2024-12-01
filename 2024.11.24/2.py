def product(numbers) -> float:
    """ 
            Возвращает произведение чисел. 
 
    """
    if len(numbers) == 1:
        return abs(numbers[0])
    return float(abs(numbers[0] * product(numbers[1:])))
	
	
	
# >>> product((0.12, 0.05, -0.09, 0.0, 0.21))
# 0.0
# >>> product(range(10, 60, 10))
# 12000000.0