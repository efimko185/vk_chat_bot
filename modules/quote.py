from modules import f, commands as c, status
import vk_api
from PIL import Image, ImageDraw, ImageFont
import requests
from vk_api import VkUpload


title = 'Цитаты великих людей'
copyr = '©'
photos = 'quote.png'

command = ['бот, цитата', 'Бот, цитата']
c.commands += '\n"Бот, цитата" -- генерирует цитату из пересланного сообщения.'

def img_upload(photos, upload):
	photo_list = upload.photo_wall(photos)
	attachment = ','.join('photo{owner_id}_{id}'.format(**item) for item in photo_list)
	return (attachment)

def quote():
	upload = VkUpload(vk_session) 
	status.messagesSend += 1
	json = f.vk_session.method('messages.getById', {'message_ids': event.message_id})
	qt_id = json['items'][0]['fwd_messages'][0]['from_id']
	text = '«'+json['items'][0]['fwd_messages'][0]['text']+'»'
	user = f.vk_session.method('users.get', {'user_ids':qt_id, 'fields':'photo_max'})
	name = user[0]['first_name'] + ' ' + user[0]['last_name'] 
	avatar = user[0]['photo_max']
	p = requests.get(avatar)
	out = open("avatar.jpg", "wb")
	out.write(p.content)
	out.close()
	avatar = Image.open('avatar.jpg')
	avatar = avatar.resize([250,250],resample=Image.BILINEAR)
	color = (0, 0, 0)
	img = Image.new('RGB', (900, 250), color)
	fnt = ImageFont.truetype('font.ttf', 37)
	fntname = ImageFont.truetype('font.ttf', 25)
	fnttext = ImageFont.truetype('font_italic.ttf', 30)
	img.paste(avatar,[0,0,250,250])
	imgDrawer = ImageDraw.Draw(img)
	imgDrawer.text((380, 2), title, font=fnt)
	imgDrawer.text((683, 210), name, font=fntname)
	imgDrawer.text((660, 210), copyr, font=fnt)
	imgDrawer.text((320, 100), text, font=fnttext)
	img.save('quote.png')
	attach = img_upload(photos, upload)
	if event.from_chat:
		vk_session.method('messages.send', {'chat_id':event.chat_id, 'attachment':attach})
		print('{}[Quote, to chat {} (user {})]'.format(f.dat, event.chat_id, event.user_id))
	else:
		vk_session.method('messages.send', {'user_id':event.user_id, 'attachment':attach})
		print('{}[Quote, to user {}]'.format(f.dat, event.user_id))
