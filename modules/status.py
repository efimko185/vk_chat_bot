from datetime import timedelta
from modules import f, commands as c
import time, psutil

command = ['/status', 'Бот, статус']
messagesSend = 0
messages = 0
c.commands += '\n"/status" или "Бот, статус" -- команда, необходимая для отладки.'


start_time = time.monotonic()
def status():

	global messagesSend
	messagesSend += 1

	global stat
	end_time = time.monotonic()
	mem = psutil.virtual_memory()
	uptime = str(timedelta(seconds=round(end_time - start_time)))
	stat = ('Uptime: '+uptime+ '\nИспользовано памяти ботом: '+str(int(psutil.Process().memory_info().vms / 10000000))+' MB' +'\nПолучено сообщений: '+str(messages) +'\nПолучено команд: '+str(messagesSend))
	if event.from_chat:
		f.write_msg_chat(event.chat_id, stat)
		f.date()   
		print('{}[Status, to chat {} (user {})]'.format(f.dat, event.chat_id, event.user_id))
	else:
		f.write_msg(event.user_id, stat)
		f.date()   
		print('{}[Status, to user {}]'.format(f.dat, event.user_id))
