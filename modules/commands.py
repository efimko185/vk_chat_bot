from modules import f, status

command = ['/help', 'Бот, помощь']
admin = '\n\n[Команды админа]'
commands = 'Список команд: '
chat = '\n\n[Команды для бесед]'

def com():
	status.messagesSend += 1
	if event.from_chat:
		f.write_msg_chat(event.chat_id, commands+chat+admin)
		f.date()   
		print('{}[Help, to chat {} (user {})]'.format(f.dat, event.chat_id, event.user_id))
	else:
		f.write_msg(event.user_id, commands+chat+admin)
		f.date()   
		print('{}[Help, to user {}]'.format(f.dat, event.user_id))