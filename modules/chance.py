from modules import f, commands as c, status
import random

command = ['бот, инфа ', 'Бот, инфа ']
c.commands += '\n"Бот, инфа <определение>" -- определяет шанс вашего определения.'

def chance():
	status.messagesSend += 1	
	chan = event.text[10:]
	chanc = ('Вероятность, что '+ chan + ' составляет ' + str(random.randint(0, 100)) + '%')
	if event.from_chat:
		f.write_msg_chat(event.chat_id, chanc)
		f.date()   
		print('{}[Chance, to chat {} (user {})]'.format(f.dat, event.chat_id, event.user_id))
	else:
		f.write_msg(event.user_id, chanc)
		f.date()   
		print('{}[Chance, to user {}]'.format(f.dat, event.user_id))
