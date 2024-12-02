def strong_password(password: str) -> bool:
    """Проверяет надежность пароля"""
    char_lower = 0
    char_upper = 0
    char_digit = 0 
    char_enothe = 0
    if len(password) >= 8:
        for char in password:
            char_ord = ord(char)
            if 64 < char_ord < 91:
                char_upper += 1
            elif 96 < char_ord < 123:
                char_lower +=1
            elif 47 < char_ord < 58:
                char_digit +=1
            elif (767 < char_ord < 880 or 
                31 < char_ord < 48 or 
                57 < char_ord < 65
                ):
                char_enothe +=1
        if ( char_upper > 0 and char_lower > 0 and 
            char_digit > 1 and char_enothe > 0 and
            sum([char_digit, char_enothe, char_lower, char_upper]) == len(password) 
            ):
            return True
        else:
            return False
    else:
        return False
        
        # >>> strong_password('SDas12!@ы')
        # False
        # >>> strong_password('SDas12!@')
        # True
        # >>> strong_password('password')
        # False
        # >>> strong_password('sdfASD123#$')
        # True
        # >>> strong_password('ASDF1asd!@')
        # False
        # >>> strong_password('sd123@#')
        # False
        # >>> strong_password('ASD123!@')
        # False
		