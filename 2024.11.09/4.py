dict_code = {}
while True:
	cod = input()
	if cod != '':
		dict_code[(cod).split(' ')[0]] = (cod).split(' ')[1]
	else:
		break
value_cod = input()
for key in dict_code:
	if dict_code[key] == value_cod:
		print(key)
		break
else:
	print('! value error !')

	