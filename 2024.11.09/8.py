list_input = [name_f for name_f in input().split('; ')]
list_out = []
count = 0
for elem in list_input:
	if elem in list_out:
		continue
	count = list_input.count(elem)
	if count > 1:
		list_out.append(elem)
		for i in range(2,count+1):
			elem_next = elem.split('.', maxsplit=1)[0] + '_' + str(i)+ '.' + elem.split('.',maxsplit=1)[1]
			list_out.append(elem_next)
	else:
		list_out.append(elem)
print(*list_out,sep = '\n')
	
	
# 1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.cpp; src.tar.gz
# 1.py
# 1_2.py
# 1_3.py
# src.tar.gz
# src_2.tar.gz
# aux.h
# main.cpp
# main_2.cpp
# main_3.cpp
# functions.h