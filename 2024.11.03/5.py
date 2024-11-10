text = input()
price = 30
len_text = sum([len(word) for word in text.split()])
price_text = len_text*price
print(f'{price_text // 100} руб. {price_text % 100} коп.')

# грузите апельсины бочках братья карамазовы
# 11 руб. 40 коп.