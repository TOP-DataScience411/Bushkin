divid = int(input())
divis = int(input())

if divid % divis == 0:
	
	print(f'{divid} делится на {divis} нацело\n'
	      f'частное: {int(divid / divis)}')
else:
	print(f'{divid} не делится на {divis} нацело\n'
	      f'неполное частное: {divid // divis}\n'
		  f'остаток: { divid % divis }')
		  
# 8
# 2
# 8 делится на 2 нацело
# частное: 4

# 10
# 3
# 10 не делится на 3 нацело
# неполное частное: 3
# остаток: 1