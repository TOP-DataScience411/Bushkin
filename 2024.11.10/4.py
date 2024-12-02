def countable_nouns(age: int, a: tuple['str','str','str']) -> str:
    """ Возвращает существительное, согласованное с числом """
    if not (age - 21)%10 and age - 21 >= 0 or age == 1:
        return a[0]
    elif (age != 11 and age != 12 and age != 13 ) and (age%10 == 2 or age%10 == 3 or age%10 ==4):
        return a[1]
    else:
        return a[2]
        
        
# >>> countable_nouns(1, ("год", "года", "лет"))
# 'год'
# >>> countable_nouns(2, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(10, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(22, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(12, ("год", "года", "лет"))
# 'лет'