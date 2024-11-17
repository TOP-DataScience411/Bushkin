list_1 = [int(digit) for digit in input().split(' ')]
list_2 = [int(digit) for digit in input().split(' ')]
n = len(list_2)
for i in range(len(list_1) - len(list_2) + 1):
	if list_2 == list_1[i:i+n]:
		print('да')
		break
else:
	print('нет')

# 1 2 3 4
# 1 2
# да	
 
# 1 2 3 4
# 2 4
# нет