list_of_dicts = [
    {
        'Владивосток': 6,
        'Воронеж': 1,
        'Екатеринбург': 1,
        'Иркутск': 5,
        'Москва': 3,
        'Новокузнецк': 4,
        'Оренбург': 1,
        'Саратов': 2,
        'Уфа': 9,
        'Ярославль': 7
    },
    {
        'Волгоград': 5,
        'Екатеринбург': 3,
        'Иркутск': 2,
        'Москва': 4,
        'Нижний Новгород': 5,
        'Новокузнецк': 2,
        'Ростов-на-Дону': 6,
        'Тольятти': 1,
        'Тюмень': 3
    },
    {
        'Владивосток': 5,
        'Казань': 4,
        'Москва': 6,
        'Нижний Новгород': 8,
        'Новосибирск': 7,
        'Пермь': 3,
        'Челябинск': 3},
    {
        'Воронеж': 4,
        'Екатеринбург': 5,
        'Иркутск': 9,
        'Нижний Новгород': 2,
        'Санкт-Петербург': 7,
        'Ярославль': 8
    }
]

dict_rez = {}
for dict_list in list_of_dicts:
	for key, value in dict_list.items():
		if key in dict_rez:
			dict_rez[key] |= {value}
		else:
			dict_rez[key] = {value}
for key,value in dict_rez.items():
	print(f"'{key}': {value}")