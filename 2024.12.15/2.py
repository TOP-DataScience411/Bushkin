from datetime import date,time,datetime
from decimal import *
import numbers

class PowerMeter:
	def __init__(self,
				tariff1: numbers.Number = 6.5,
				tariff2: numbers.Number = 3.0,
				tariff2_starts: time = time(23,0),
				tariff2_ends: time = time(6,0)
				):
		self.tariff1 = Decimal(tariff1)
		self.tariff2 = Decimal(tariff2) 
		self.tariff2_starts = tariff2_starts 
		self.tariff2_ends = tariff2_ends 
		self.power = Decimal(str(0.0))
		self.charges = {}
		
	def meter(self,power):
		
		''' Принимает значение потреблённой мощности, вычисляет и возвращает стоимость согласно тарифному плану, действующему в текущий момент '''
		
		
		time_now = datetime.now().time()
		if self.tariff2_ends < time_now < self.tariff2_starts:
			tarif = self.tariff1 
		else:
			tarif = self.tariff2 
		
		key_dict_charges = date(date.today().year,date.today().month,1) 
		cost = tarif*Decimal(str(power))
		self.power += Decimal(str(power))
		
		if key_dict_charges not in self.charges:
			self.charges[key_dict_charges] = cost
		
		else:
			self.charges[key_dict_charges] += cost
			
		return cost
		
	def __str__(self):
		
		''' человекочитаемое строковое представление '''
		
		cost = [cos for mon,cos in self.charges.items() if mon == date(date.today().year,date.today().month,1)]
		return  f'({datetime.now().strftime('%b')}) {cost[0].quantize(Decimal('0.01'))}'
		
	def __repr__(self):
		
		''' машиночитаемое строковое представление '''
		
		return f'<PowerMeter: {self.power.quantize(Decimal('0.01'))} кВт/ч>'
		
		
		
#  >>> pm1 = PowerMeter()
#  >>> pm1.meter(2)
#  Decimal('13.0')
#  >>> pm1.meter(1.2)
#  Decimal('7.80')
#  >>> pm1
#  <PowerMeter: 3.20 кВт/ч>
#  >>> print(pm1)
#  (Jan) 20.80