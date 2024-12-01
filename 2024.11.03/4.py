count = 0
n = int(input())
for i in range(10**(n-1),10**n):
    for j in range(2,i // 2 +2):
        if i % j == 0:
            break
        else:
            if j == i // 2 +1:
                count += 1
print(count)

# 3
# 143	