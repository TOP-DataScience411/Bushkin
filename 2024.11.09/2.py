list_fruit = []
str_fruit = ''


while True:
    fruit = input()
    if fruit == '':
        break
    list_fruit.append(fruit)
	

for i in range(len(list_fruit)):
	if i == len(list_fruit) - 1:
		str_fruit += list_fruit[i]
	elif i == len(list_fruit) -2:
		str_fruit += list_fruit[i] + ' и '
	else:
		str_fruit += list_fruit[i] + ', '
		

print(str_fruit)
 		
# яблоко
# груша
# 
# яблоко и груша
# 
# яблоко
# груша
# апельсин
# 
# яблоко, груша и апельсин
# 
# яблоко
# груша
# апельсин
# лимон
# 
# яблоко, груша, апельсин и лимон		