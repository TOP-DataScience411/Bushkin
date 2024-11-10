list_nums = []
while True:
    num = input()
    if int(num) % 7 != 0:
        break
    list_nums.append(num)
print(*list_nums[::-1])   
	
# 7
# 7
# 14
# 21
# 13
# 21 14 7 7