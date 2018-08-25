from modules import f, commands as c, status
import vk_api, random

command = ['бот, кто ', 'Бот, кто ']
c.commands += '\n"Бот, кто <определение>" -- узнайте, кто является носителем вашего определения.'

def who():
	status.messagesSend += 1
	whois = event.text[9:]
	if event.from_chat:
		users = vk_session.method('messages.getChatUsers',{'chat_id':event.chat_id, 'fields':'name'})
		user = random.choice(users)
		hypertext = '[id{}|{}]'.format((user['id']), (user['first_name'])+' '+(user['last_name']))
		whos = ('Кто {}? Я думаю, это {}'.format(whois, hypertext))
		f.write_msg_chat(event.chat_id, whos)
		f.date()   
		print('{}[Who, to chat {} (user {})]'.format(f.dat, event.chat_id, event.user_id))
	else:
		f.write_msg(event.user_id, 'Ошибка! Данную команду можно использовать только в беседе!')
		f.date()   
		print('{}[Who, to user {}]'.format(f.dat, event.user_id))