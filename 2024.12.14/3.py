from pathlib import Path
from utils import load_file
def ask_for_file():
	a = 1
	while a:
		file = Path(input('путь: '))
		if file.is_file():
			a = 0
			load_file(file)
			
		else:
			print('! по указанному пути отсутствует необходимый файл ! ')
	import conf	
	return conf
	
#  config_module = ask_for_file()
#  путь: conf.py
#  ! по указанному пути отсутствует необходимый файл !
#  путь: data/conf.py
#  config_module.defaults
#  {'parameter1': 'value1', 'parameter2': 'value2', 'parameter3': 'value3', 'parameter4': 'value4'}