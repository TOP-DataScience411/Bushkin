int_mile = input()
fract_mile = input()
mile = float( int_mile + '.' + fract_mile)
print( f'{mile} миль = { round(mile * 1.61,1) } км')