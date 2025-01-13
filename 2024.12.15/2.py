from datetime import date,time,datetime
from decimal import *
import numbers

class PowerMeter:
	def __init__(
		self,
	    tariff1: numbers.Number = 6.5,
        tariff2: numbers.Number = 3.0,
        tariff2_starts: time = time(23,0),
        tariff2_ends: time = time(6,0)
		):
			
		self.tariff1: Decimal(str(tariff1))
        self.tariff2: Decimal(str(tariff2)) 
        self.tariff2_starts = tariff2_starts 
        self.tariff2_ends = tariff2_ends 
		self.power: = Decimal('0,0')
		self.charges = {}
		
	def meter(self,power):
		
		''' Принимает значение потреблённой мощности, вычисляет и возвращает стоимость согласно тарифному плану, действующему в текущий момент '''
		
		# вычисляем актуальный тариф
		
		time_now = datetime.now().time()
		if self.tariff2_ends < time_now < self.tariff2_starts:
			tarif = self.tariff1 
		else:
			tarif = self.tariff2 
		
		key_dict_charges = date(date.today().year,date.today().month,1) 
		
		if key_dict_charges not in self.charges:
			self.charges[key_dict_charges] = tarif*power
		
		else:
			self.charges[key_dict_charges] 
			
			