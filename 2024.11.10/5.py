def central_tendency(number_one: float, number_two: float, /, *numbers: float) -> dict[str,float]:
    """ Вычисляет основные меры центральной тенденции """
    central_tendency_dict = {
        'median': 0.0,
        'arithmetic': 0.0,
        'geometric': 0.0,
        'harmonic': 0.0
    }
    list = sorted((number_one,number_two,*numbers), reverse=True )
    leng = len(list)
    product = 1
    for num in list:
        product *= num
    if leng%2 != 0:
        central_tendency_dict['median'] = list[int((leng -1) / 2)]
    else:
        central_tendency_dict['median'] = (list[int(leng // 2)] + list[int(leng //2 -1)]) / 2
    central_tendency_dict['arithmetic'] = sum(list) / leng
    central_tendency_dict['geometric'] =product**(1/leng)
    central_tendency_dict['harmonic'] = leng / sum([ 1/a for a in list])
    return print(central_tendency_dict)
    
    
# >>> central_tendency(1, 2, 3, 4)
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.2133638394006434, 'harmonic': 1.9200000000000004}
# >>> sample = [1, 2, 3, 4, 5]
# >>> central_tendency(*sample)
# {'median': 3, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}