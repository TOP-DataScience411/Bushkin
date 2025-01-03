from pathlib import Path
def list_files(path_dir: str):
	""" Возвращает кортеж  с именами файлов в каталоге по переданному пути."""
	file_name = ()
	path_dir_l = Path(path_dir)
	for pat in path_dir_l.iterdir():
		if pat.is_file():
			file_name = file_name + (pat.name,)
	print(file_name)
	
	
	
# 	d:\Bushkin\2024.12.14>tree /f
# Структура папок тома Диск
# Серийный номер тома: 3E63-9648
# D:.
# │   # HW 2024.12.14.txt
# │   1.py
# │
# └───data
#     │   7MD9i.chm
#     │   conf.py
#     │   E3ln1.txt
#     │   F1jws.jpg
#     │   le1UO.txt
#     │   q40Kv.docx
#     │   questions.quiz
#     │   r62Bf.txt
#     │   vars.py
#     │   xcD1a.zip
#     │
#     ├───c14KE
#     │       5vsIh.dat
#     │       P2a91.dat
#     │
#     ├───mXbd9
#     │       RoBjg.pt
#     │       z03EN.pt
#     │
#     └───names
#             женские_имена.txt
#             мужские_имена_отчества.txt
#             фамилии.txt
# 			

# >>> list_files(r'd:\Bushkin\2024.12.14\data')
# ('7MD9i.chm', 'conf.py', 'E3ln1.txt', 'F1jws.jpg', 'le1UO.txt', 'q40Kv.docx',        'questions.quiz', 'r62Bf.txt', 'vars.py', 'xcD1a.zip')