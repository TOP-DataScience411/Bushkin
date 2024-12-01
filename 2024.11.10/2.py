def taxi_cost(lenght: int, waiting: int=0) -> int|None:
	''' Вычисляет стоимость поездки на такси '''
	if lenght < 0 or waiting < 0:
		return None
	else:
		cost = 80 + lenght/150*6 + waiting*3  if lenght > 0 else 160 + waiting * 3
		return round(cost)
	
# >>> taxi_cost(1500)
# 140
# >>> taxi_cost(2560)
# 182
# >>> taxi_cost(0, 5)
# 175
# >>> taxi_cost(42130, 8)
# 1789
# >>> print(taxi_cost(-300))
# None	