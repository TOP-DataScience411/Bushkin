def deck():
	""" 
	    создаёт упорядоченную колоду карт.
	"""
	masti = ['черви', 'бубны', 'пики', 'трефы']
	nominali = [2,3,4,5,6,7,8,9,10,11,12,13,14]
	rez = ((nominal,mast) for mast in masti for nominal in nominali)
	return rez
	
	
#  deck()
# <generator object deck.<locals>.<genexpr> at 0x0000016D780033E0>
 
# list(deck())[10::13]
# [(12, 'черви'), (12, 'бубны'), (12, 'пики'), (12, 'трефы')]