n = int(input())
fibo = [1,1]
list_fibo = [1]
for i in range(1,n):
	fibo[0], fibo[1] = fibo[1],fibo[1] + fibo[0]
	list_fibo.append(fibo[0])
print(*list_fibo)


# 1
# 1
# 
# 5
# 1 1 2 3 5
# 
# 17
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597	