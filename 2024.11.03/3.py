num = int(input())
print(sum([j for j in range(1,num // 2 +1) if num % j == 0 ]) + num )

# 50
# 93