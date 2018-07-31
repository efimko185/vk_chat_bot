from modules import f, commands as c, status
import options as o
import sys

c.admin += '\n"/kill" или "Бот, умри" -- выключить бота.' 
command = ['/kill', 'Бот, умри']

def kill():
	status.messagesSend += 1
	if event.user_id in o.admins:
		if event.from_chat:
			f.write_msg_chat(event.chat_id, 'Ня. Пока')
			f.date()   
			print('{}[Admin][Kill, to chat {} (user {})]'.format(f.dat, event.chat_id, event.user_id))
			sys.exit()
		else:
			f.write_msg(event.user_id, 'Ня. Пока')
			f.date()   
			print('{}[Admin][Kill, to user {}]'.format(f.dat, event.user_id))
			sys.exit()
	else:
		if event.from_chat:
			f.write_msg_chat(event.chat_id, 'Хмм... Но ведь ты не админ!')
			f.date()   
			print('{}[Kill, to chat {} (user {})]'.format(f.dat, event.chat_id, event.user_id))
		else:
			f.write_msg(event.user_id, 'Хмм... Но ведь ты не админ!')
			f.date()   
			print('{}[Kill, to user {}]'.format(f.dat, event.user_id))