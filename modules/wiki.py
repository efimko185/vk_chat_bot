from modules import f, commands as c, status
import wikipedia

wikipedia.set_lang("ru")#русский язык в википедии

c.commands += '\n"Бот, вики <запрос>" - Поиск в Википедии по Вашему запросу.' 
command = ['бот, вики ', 'Бот, вики '] 

def wiki():
	status.messagesSend += 1
	search = event.text[10:]
	try:
		info = wikipedia.summary(search, sentences=3)
	except Exception:
		if event.from_chat:
			f.write_msg_chat(event.chat_id, 'Ошибка запроса!')
			f.date() 
			print('{}[Wiki, to chat {} (user {})][Error!]'.format(f.dat, event.chat_id, event.user_id ))
		else:
			f.write_msg(event.user_id, 'Ошибка запроса!')
			f.date() 
			print('{}[Wiki, to user {}][Error!]'.format(f.dat, event.user_id))
	if event.from_chat:
		f.write_msg_chat(event.chat_id, info)
		f.date()   
		print('{}[Wiki, to chat {} (user {})][{}]'.format(f.dat, event.chat_id, event.user_id, search))
	else:
		f.write_msg(event.user_id, info)
		f.date()   
		print('{}[Wiki, to user {}][{}]'.format(f.dat, event.user_id, search))