num = int(input())
list_num = [ int(input()) for i in range(num) ]
print(  sum([ j for j in list_num if j >0 ]))

# 6
# 10
# 10
# -20
# 15
# -15
# 88
# 123