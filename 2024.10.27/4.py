num = int(input())
num1 = num // 100
num2 = num // 10 % 10
num3 = num % 10
print( f'Сумма цифр = { num1 + num2 + num3 }')
print( f'Произведение цифр = { num1 * num2 * num3 }')

# 333
# Сумма цифр = 9
# Произведение цифр = 27