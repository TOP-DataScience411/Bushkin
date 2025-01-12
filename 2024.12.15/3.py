class ChessKing:
	
	files: dict[str, int] = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
	ranks: dict[str, int] = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8}
	
	def __init__(self,color: str = 'white',square: str = None):
		if square == None:
			square = 'e1' if color == 'white' else 'e8'
		self.color = color
		self.square = square
		
	def is_turn_valid(self,new_square: str):
		''' Принимает на вход строку нового поля и проверяет, возможен ли для данной фигуры ход с текущего поля на новое. '''
		
		if (abs(self.files[self.square[0]] - self.files[new_square[0]]) <= 1 and
			abs(self.ranks[self.square[1]] - self.ranks[new_square[1]])	<=1) :
			return True
		return False
		
	def turn(self,new_square:str):
		''' Принимает на вход строку нового поля и выполняет ход, выбрасывает ValueError в случае невозможности выполнить ход. '''
		if self.is_turn_valid(new_square):
			self.square = new_square
		else: 
			raise ValueError 
			
	def __repr__(self):
		''' машиночитаемое строковое представление '''
		return "'{}K: {}'".format(self.color[0].upper(),self.square)
		
		
	def __str__(self):
		''' человекочитаемое строковое представление '''
		return '{}K: {}'.format(self.color[0].upper(),self.square)
		
		
		
# >>> wk = ChessKing()
# >>> wk
# 'WK: e1'
# >>> bk = ChessKing('black')
# >>> print(bk)
# BK: e8
# >>> wk.turn('d4')
# 
# ValueError
# >>> wk.turn('e2')
# >>> wk
# 'WK: e2'