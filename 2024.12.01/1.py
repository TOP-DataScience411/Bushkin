
from datetime import date,time,timedelta


def vacant(vacations):
	''' Создаем список дат которые не входят в график '''
	list_vac=[]
	for vacation in vacations:
		date2 = vacation[0]
		for i in range(vacation[1].days):
			list_vac.append(date2)
			date2 += timedelta(days=1) 			
	return list_vac
	
	
def schedule(date1,*days,total_days,format_str='%d/%m/%Y'):
	'''Генерирует график '''
	list_vac = vacant(vacations)
	listd=[]
	while total_days:
		if date1.isoweekday() in days and date1 not in list_vac:
			listd.append(date1)
			total_days -= 1
		date1 += timedelta(days=1)
	return [data.strftime(format_str) for data in listd]
	
	
	    # vacations = [ (date(2023, 5, 1), timedelta(weeks=1)),(date(2023, 7, 17), timedelta(weeks=1))]
		# 
        # py321 = schedule(date(2023, 4, 1), 6, 7, total_days=70)
		# 
        # len(py321)
		# 70
		# 
        # py321[28:32]
        # ['15/07/2023', '16/07/2023', '29/07/2023', '30/07/2023']