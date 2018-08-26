from modules import f, commands as c, status
import vk_api, random

command = ['бот, кто ', 'Бот, кто ']
c.commands += '\n"Бот, кто <определение>" -- узнайте, кто является носителем вашего определения.'

commandLove = ['Бот, кого кто', 'бот, кого кто']
c.commands += '\n"Бот, кого кто" -- узнайте, кто кого любит:)'

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

def love():
	status.messagesSend += 1
	if event.from_chat:
		users = vk_session.method('messages.getChatUsers',{'chat_id':event.chat_id, 'fields':'name'})
		love1, love2 = random.sample(users, 2)
		love = ('[id{}|{} {}] - любит - [id{}|{} {}]'.format(love1['id'], love1['first_name'], love1['last_name'], love2['id'], love2['first_name'], love2['last_name']))
		vk_session.method('messages.send', {'chat_id':event.chat_id, 'message':love, 'attachment':'photo494918759_456239057'})
		f.date()  
		print('{}[Love, to chat {} (user {})]'.format(f.dat, event.chat_id, event.user_id))
	else:
		f.write_msg(event.user_id, 'Ошибка! Данную команду можно использовать только в беседе!')
		f.date()   
		print('{}[Love, to user {}]'.format(f.dat, event.user_id))
