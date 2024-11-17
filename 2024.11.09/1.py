email = input()
if '@' in email and '.' in email.split('@')[1][2:]:
	print('да')
else:
	print('нет')
	
# sgd@ya.ru
# да
#	
# abcde@fghij
# нет	