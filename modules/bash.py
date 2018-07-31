from modules import f, commands as c, status
from lxml import html
import requests as req

command = ['/bash', 'Бот, анекдот']
c.commands += '\n"/bash" или "Бот, анекдот" -- отправляет случайную цитату с bаsh.im.'

def bash():
	status.messagesSend += 1
	r = req.get('http://bash.im/random')
	doc = html.document_fromstring(r.text)
	bash = '\n'.join(doc.xpath('/html/body/div[2]/div[3]/div[2]/text()'))
	if event.from_chat:
		f.write_msg_chat(event.chat_id, bash)
		f.date()   
		print('{}[Bash, to chat {} (user {})]'.format(f.dat, event.chat_id, event.user_id))
	else:
		f.write_msg(event.user_id, bash)
		f.date()   
		print('{}[Bash, to user {}]'.format(f.dat, event.user_id))