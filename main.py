import vk_api
from modules import f, status, commands as c
from modules import bash, kill, admin
from vk_api.longpoll import VkLongPoll, VkEventType
import options as o

def main():
	#авторизация
	try:
		vk_session = vk_api.VkApi(o.login, o.password)
		f.date()
		print('{}[Попытка авторизации...]'.format(f.dat)) 
		vk_session.auth()
		print('{}[Авторизация прошла успешно!]'.format(f.dat)) 
	except vk_api.AuthError as error_msg:
		f.date()
		print('{}[Ошибка авторизации!][{}]'.format(f.dat, error_msg))
		return

	f.vk_session = vk_session
	admin.vk_session = vk_session

	longpoll = VkLongPoll(vk_session)#подключаем лонгпулл

	for event in longpoll.listen():

		if event.type == VkEventType.MESSAGE_NEW:
			status.messages += 1
			#сюда добавляем команды
			try:
				if event.text in status.command:
					status.event = event
					status.status()

				if event.text in c.command:
					c.event = event
					c.com()

				if event.text in bash.command:
					bash.event = event
					bash.bash()

				if event.text in kill.command:
					kill.event = event
					kill.kill()

				if event.text in admin.command:
					admin.event = event
					admin.admins()

			except Exception as error_msg:
				f.date()
				print('{}[Ошибка отправки сообщения!][{}]'.format(f.dat, error_msg))

if __name__ == '__main__':
	main()