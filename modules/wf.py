from modules import f, commands as c, status
import wolframalpha

app_id = 'YTJTWV-PRUUTP939W'
client = wolframalpha.Client(app_id)

c.commands += '\n"Бот, wf <запрос>" - отправляет ваш запрос на WolframAlpha.' 
command = ['бот, wf ', 'Бот, wf '] 

def wf():
	status.messagesSend += 1
	wf = event.text[8:]
	try:
		res = client.query(wf)
		answer = next(res.results).text
	except Exception:
		if event.from_chat:
			f.write_msg_chat(event.chat_id, 'Ошибка запроса!')
			f.date() 
			print('{}[Wf, to chat {} (user {})][Error!]'.format(f.dat, event.chat_id, event.user_id ))
		else:
			f.write_msg(event.user_id, 'Ошибка запроса!')
			f.date() 
			print('{}[Wf, to user {}][Error!]'.format(f.dat, event.user_id))
	if event.from_chat:
		f.write_msg_chat(event.chat_id, answer)
		f.date()   
		print('{}[Wf, to chat {} (user {})][{}]'.format(f.dat, event.chat_id, event.user_id, answer))
	else:
		f.write_msg(event.user_id, answer)
		f.date()   
		print('{}[Wf, to user {}][{}]'.format(f.dat, event.user_id, answer))

