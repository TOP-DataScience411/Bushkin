ticket = input()
sum_left_ticket = sum([int(i) for i in ticket[:3]])
sum_righ_ticket = sum([int(i) for i in ticket[3:]])
if sum_left_ticket == sum_righ_ticket:
	print('да')
else:
	print('нет')
	
# 183534
# да	
# 
# 401367
# нет