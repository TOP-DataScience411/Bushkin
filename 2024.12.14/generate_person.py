from datetime import date,timedelta,datetime
from random import randint

second_name = []
otchestva = []
list_names = []


def load_data():
	""" Считываем данные и формируем три списка 1:фамилии[[муж,жен],  ]  2:отчества[[муж,жен],  ]  3:имена[[муж,жен],  ]"""
	global second_name, otchestva, list_names

	with open(r'D:\Bushkin\2024.12.14\data\names\фамилии.txt',encoding = ' utf-8') as file:
		content = file.readlines()
		second_name = [line.strip().split(', ') for line in content]
		second_name = [elem if len(elem)==2 else [elem[0],elem[0]]  for elem in second_name]
		
		
		#second_name = [line.strip().split(', ') for line in content]   		
	
	with open(r'D:\Bushkin\2024.12.14\data\names\мужские_имена_отчества.txt',encoding = ' utf-8') as file:
		content = file.readlines()
		name_m = [line.strip().split(' ',maxsplit=1)[0] for line in content] 
		otchestva =	[line.strip().split(' ',maxsplit=1)[1].strip('()').split(', ') for line in content] 
	
	with open(r'D:\Bushkin\2024.12.14\data\names\женские_имена.txt',encoding = ' utf-8') as file:
		content = file.readlines()
		name_w = [line.strip() for line in content] 
	
	list_names = []
	count = 0
	
	for ind_n in range(len(name_w)):
		ind_n_m = ind_n
		#print([name_m[ind_n_m],name_w[ind_n]])
		if ind_n > len(name_m)-1:
			ind_n_m = count
			count += 1
			list_names.append([name_m[ind_n_m],name_w[ind_n]])
		else:
			list_names.append([name_m[ind_n_m],name_w[ind_n]])
	
	return	


def generate_person():
	""" Генерирует анкету человека со случайными данными."""
	data_start = date(1900,1,1)
	data_end = date(1999,12,31)
	data = data_start + timedelta(days = randint(0,(data_end - data_start).days))
	n = randint(0,1)
	dict_pers = {'имя':list_names[randint(0,len(list_names))][n],
	             'отчество': otchestva[randint(0,len(otchestva))][n],
				 'фамилия': second_name[randint(0,len(second_name))][n],
			     'пол': ['мужской','женский'][n],
				 'дата рождения': data,
				  'мобильный': '+79'+ str(randint(0,999999999))}
	
	return dict_pers
	
def rand_date(from_year = 2000):
	data_today = date.today()
	data_start = date(from_year,1,1)
	data = data_start + timedelta(days = randint(0,(data_today - data_start).days))
	return data
	
load_data()	