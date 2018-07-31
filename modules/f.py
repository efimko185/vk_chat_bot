from datetime import datetime
def date():
	global dat
	dat = datetime.strftime(datetime.now(), "[%Y.%m.%d][%H:%M:%S]")

def write_msg(user_id, s):
	vk_session.method('messages.send', {'user_id':user_id,'message':s})

def write_msg_chat(chat_id, s):
	vk_session.method('messages.send', {'chat_id':chat_id,'message':s})