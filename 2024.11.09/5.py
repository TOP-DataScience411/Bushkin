scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}

leter_score = {}
for key,value in scores_letters.items():
	leter_score |= {}.fromkeys(value,key)
score = sum([leter_score[char] for char in input().upper()])
print(score)

 