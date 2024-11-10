chess_sq_1 = input()
chess_sq_2 = input()

list_tru = [-1, 0, 1]

if (
        (ord(chess_sq_1[0]) - ord(chess_sq_2[0])) in list_tru and
        (int(chess_sq_1[1]) - int(chess_sq_2[1])) in list_tru 
):
    print('да')	
else:
	 print('нет')

# g3
# f2
# да
# 
# c6
# d4
# нет