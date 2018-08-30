import vk_api
from modules import f, status, commands as c
from modules import bash, kill, admin, anime, who, chance, wiki, wf, pyth
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
	anime.vk_session = vk_session
	who.vk_session = vk_session

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

				if event.text in anime.commandNaruto:
					anime.event = event
					anime.naruto()

				if event.text in anime.commandAnime:
					anime.event = event
					anime.anime()

				if event.text in anime.commandHentai:
					anime.event = event
					anime.hentai()

				if event.text[:9] in who.command:
					who.event = event
					who.who()

				if event.text[:10] in chance.command:
					chance.event = event
					chance.chance()

				if event.text[:10] in wiki.command:
					wiki.event = event
					wiki.wiki()

				if event.text in who.commandLove:
					who.event = event
					who.love()

				if event.text[:8] in wf.command:
					wf.event = event
					wf.wf()

				if event.text[:4] in pyth.command:
					pyth.event = event
					pyth.pyth()

			except Exception as error_msg:
				f.date()
				print('{}[Ошибка отправки сообщения!][{}]'.format(f.dat, error_msg))

if __name__ == '__main__':
	main()