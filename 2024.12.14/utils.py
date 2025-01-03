#from path import Path
from shutil import copy2

def load_file(file_path):
	copy2(file_path,'conf.py')
	return 