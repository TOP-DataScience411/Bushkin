dict_code = {}
while True:
	cod = input()
	if cod != '':
		dict_code[(cod).split(' ')[0]] = (cod).split(' ')[1]
	else:
		break
value_cod = input()
for key in dict_code:
	if dict_code[key] == value_cod:
		print(key)
		break
else:
	print('! value error !')

# 1004 ER_CANT_CREATE_FILE
# 1005 ER_CANT_CREATE_TABLE
# 1006 ER_CANT_CREATE_DB
# 1007 ER_DB_CREATE_EXISTS
# 1008 ER_DB_DROP_EXISTS
# 
# ER_CANT_CREATE_DB
# 1006	

# 4107 ER_SRS_UNUSED_PROJ_PARAMETER_PRESENT
# 4108 ER_GIPK_COLUMN_EXISTS
# 4111 ER_DROP_PK_COLUMN_TO_DROP_GIPK
# 4113 ER_DA_EXPIRE_LOGS_DAYS_IGNORED
# 
# ER_CANT_OPEN_FILE
# ! value error !