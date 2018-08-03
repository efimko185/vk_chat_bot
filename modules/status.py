from datetime import timedelta
from modules import f, commands as c
import time
from memory_profiler import memory_usage
import options as o

command = ['/status', 'Бот, статус']
messagesSend = 0
messages = 0
c.admin += '\n"/status" или "Бот, статус" -- команда, необходимая для отладки.'


start_time = time.monotonic()
def status():
	if event.user_id in o.admins:
		global messagesSend
		messagesSend += 1

		global stat
		end_time = time.monotonic()
		uptime = str(timedelta(seconds=round(end_time - start_time)))
		stat = ('Uptime: '+uptime+ '\nИспользовано памяти ботом: '+str(memory_usage())[1:3]+' MB' +'\nПолучено сообщений: '+str(messages) +'\nПолучено команд: '+str(messagesSend))
		if event.from_chat:
			f.write_msg_chat(event.chat_id, stat)
			f.date()   
			print('{}[Status, to chat {} (user {})]'.format(f.dat, event.chat_id, event.user_id))
		else:
			f.write_msg(event.user_id, stat)
			f.date()   
			print('{}[Status, to user {}]'.format(f.dat, event.user_id))
	else:
		if event.from_chat:
			f.write_msg_chat(event.chat_id, 'Хмм... Но ведь ты не админ!')
			f.date()   
			print('{}[Status, to chat {} (user {})]'.format(f.dat, event.chat_id, event.user_id))
		else:
			f.write_msg(event.user_id, 'Хмм... Но ведь ты не админ!')
			f.date()   
			print('{}[Status, to user {}]'.format(f.dat, event.user_id))
