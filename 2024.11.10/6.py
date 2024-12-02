def orth_triangle(*,cathetus1: float = 0, cathetus2: float = 0, hypotenuse: float = 0) -> float | None:
    """ Вычисляет третью сторону прямоугольного треугольника """
    if ( cathetus1 == cathetus2 == 0 or 
        cathetus1 == hypotenuse == 0 or 
        cathetus2 == hypotenuse == 0 or
        cathetus1 > hypotenuse  or 
        cathetus2 > hypotenuse  or
        cathetus1 != 0 and cathetus2 != 0 and hypotenuse != 0 
        ):
        return None
    if cathetus1 == 0:
        return (hypotenuse**2 - cathetus2**2)**0.5
    elif cathetus2 == 0:
        return (hypotenuse**2 - cathetus1**2)**0.5
    elif hypotenuse == 0:
        return (cathetus2**2 + cathetus1**2)**0.5
        
        
# >>> orth_triangle(cathetus1=3, hypotenuse=5)
# 4.0
# >>> orth_triangle(cathetus1=8, cathetus2=15)
# 17.0
# >>>  print(orth_triangle(cathetus2=9, hypotenuse=3))
# None