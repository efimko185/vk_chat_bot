from modules import f, commands as c, status
import options as o

c.admin += '\n"/py <команда>" -- выполнить python-команду.' 
command = ['/py ', '/Py ']

def txt(txt):
	txt = str(txt)
	if event.from_chat:
		f.write_msg_chat(event.chat_id, txt)   
	else:
		f.write_msg(event.user_id, txt)

def pyth():
	status.messagesSend += 1
	if event.user_id in o.admins:
		text = event.text[4:]
		try:
			exec(text)
			if event.from_chat:
				f.date()   
				print('{}[Admin][Python, to chat {} (user {})][{}]'.format(f.dat, event.chat_id, event.user_id, text))
			else:
				f.date()  
				print('{}[Admin][Python, to user {}][{}]'.format(f.dat, event.user_id, text))
		except Exception as error_msg:
			if event.from_chat:
				f.write_msg_chat(event.chat_id, error_msg) 
				f.date()   
				print('{}[Admin][Python, to chat {} (user {})][{}]'.format(f.dat, event.chat_id, event.user_id, text))
			else:
				f.write_msg(event.user_id, error_msg)
				f.date()  
				print('{}[Admin][Python, to user {}][{}]'.format(f.dat, event.user_id, text))

	else:
		if event.from_chat:
			f.write_msg_chat(event.chat_id, 'Хмм... Но ведь ты не админ!')
			f.date()   
			print('{}[Python, to chat {} (user {})]'.format(f.dat, event.chat_id, event.user_id))
		else:
			f.write_msg(event.user_id, 'Хмм... Но ведь ты не админ!')
			f.date()   
			print('{}[Python, to user {}]'.format(f.dat, event.user_id))
