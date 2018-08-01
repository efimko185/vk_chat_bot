from modules import commands as c, status, f
from random import randint
import vk_api

commandNaruto = ['Бот, наруто', 'Бот, Наруто', 'бот, наруто', 'бот, Наруто']
c.commands += '\n"Бот, наруто" -- отправляет случайный арт с Наруто.'

commandAnime = ['Бот, аниме', 'бот, аниме', 'бот,аниме', 'Бот,аниме', 'бот аниме']
c.commands += '\n"Бот, аниме" -- отправляет случайный аниме-арт.'

def naruto():
	status.messagesSend += 1
	pic = vk_session.method('photos.get', {'owner_id':-34269876, 'album_id':239149054, 'offset':randint(1, 405), 'count':1})
	attachment = 'photo-34269876_{}'.format(pic['items'][0]['id'])
	if event.from_chat:
		vk_session.method('messages.send', {'chat_id':event.chat_id, 'attachment':attachment})
		print('{}[Naruto, to chat {} (user {})]'.format(f.dat, event.chat_id, event.user_id))
	else:
		vk_session.method('messages.send', {'user_id':event.user_id, 'attachment':attachment})
		print('{}[Naruto, to user {}]'.format(f.dat, event.user_id))

def anime():
	status.messagesSend += 1
	pic = vk_session.method('photos.get', {'owner_id':-47, 'album_id':159938259, 'offset':randint(1, 5060), 'count':1})
	attachment = 'photo-47_{}'.format(pic['items'][0]['id'])
	if event.from_chat:
		vk_session.method('messages.send', {'chat_id':event.chat_id, 'attachment':attachment})
		print('{}[Anime, to chat {} (user {})]'.format(f.dat, event.chat_id, event.user_id))
	else:
		vk_session.method('messages.send', {'user_id':event.user_id, 'attachment':attachment})
		print('{}[Anime, to user {}]'.format(f.dat, event.user_id))


