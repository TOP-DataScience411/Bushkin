import shutil
def important_message(message_in:str)->str:
    """ Генерирует строку """
    width = shutil.get_terminal_size().columns
    up_down_str = '#'+'='*(width -2)+'#'
    line= '#'+' '*(width -2)+'#\n'
    if len(message_in) <= width - 6:
        return up_down_str +'\n' + line + '#'+ message_in.center(width-2)+'#\n' + line + up_down_str
    else:
        message_in_str = up_down_str +'\n' + line 
        str_line =('')
        str_line_list = []
        for in_str in message_in.split():
            if len(str_line + in_str) <= width-6:
                str_line = str_line + in_str +' '
                if in_str== message_in.split()[-1]:
                    str_line_list.append(str_line)
            else:
                str_line_list.append(str_line)
                str_line = in_str + ' '
        for i in str_line_list:
            message_in_str = message_in_str + '#' + i.center(width-2) +'#\n'
        message_in_str = message_in_str + line + up_down_str
        return message_in_str