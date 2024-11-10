chess_sq_1 = input()
chess_sq_2 = input()
if (int(chess_sq_1[1]) - int(chess_sq_2[1])) % 2 == \
    (ord(chess_sq_1[0]) - ord(chess_sq_2[0])) % 2:
	print('да')
else:
	print('нет')

# a1
# c3
# да