list_1 = [int(digit) for digit in input().split(' ')]
list_2 = [int(digit) for digit in input().split(' ')]
n = len(list_2)
for i in range(len(list_1) - len(list_2) + 1):
	if list_2 == list_1[i:i+n]:
		print('да')
		break
else:
	print('нет')

	