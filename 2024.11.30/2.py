from utils import important_message
def main():
    message = input( 'Текст сообщения: ')
    message_out = important_message(message)
    print(message_out)
    
	
#  	>>> main()
#  Текст сообщения: ЗАГОЛОВОК ПРОГРАММЫ
#  #========================================================================================#
#  #                                                                                        #
#  #                                  ЗАГОЛОВОК ПРОГРАММЫ                                   #
#  #                                                                                        #
#  #========================================================================================#
#  >>> text = 'Обратите внимание на очень важное сообщение от команды разработчиков этой великолепной программы'
#  >>> msg = important_message(text)
#  >>> print(msg)
#  #========================================================================================#
#  #                                                                                        #
#  #       Обратите внимание на очень важное сообщение от команды разработчиков этой        #
#  #                                великолепной программы                                  #
#  #                                                                                        #
#  #========================================================================================#
	