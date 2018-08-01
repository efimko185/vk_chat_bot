from modules import f, commands as c, status
import options as o

c.admin += '\n"/admins" или "Бот, админы" -- cписок админов.'
command = ['/admins', 'Бот, админы']

def admins():
	admins = 'Список админов:'
	status.messagesSend += 1
	if event.user_id in o.admins:
		for i in o.admins:
			info = vk_session.method('users.get',{'user_ids':i})
			adminName = ('\n{} {}').format(info[0]['first_name'], info[0]['last_name'])
			admins += adminName
		if event.from_chat:
			f.write_msg_chat(event.chat_id, admins)
			f.date()   
			print('{}[Admin][Admins, to chat {} (user {})]'.format(f.dat, event.chat_id, event.user_id))
		else:
			f.write_msg(event.user_id, admins)
			f.date()   
			print('{}[Admin][Admins, to user {}]'.format(f.dat, event.user_id))

	else:
		if event.from_chat:
			f.write_msg_chat(event.chat_id, 'Хмм... Но ведь ты не админ!')
			f.date()   
			print('{}[Admins, to chat {} (user {})]'.format(f.dat, event.chat_id, event.user_id))
		else:
			f.write_msg(event.user_id, 'Хмм... Но ведь ты не админ!')
			f.date()   
			print('{}[Admins, to user {}]'.format(f.dat, event.user_id))