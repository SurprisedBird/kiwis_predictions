import config
import requests
import json
from time import sleep

global last_update_id
last_update_id = 0

prediction_list = config.prediction_list

def get_updates():
	bot_request = requests.get(f'{config.MAIN_URL}/getUpdates')
	chat_info = bot_request.json()['result']
	return chat_info

def get_message():
	chat_info = get_updates()
	last_chat_info = chat_info[-1]
	current_update_id = last_chat_info['update_id']

	global last_update_id
	if last_update_id != current_update_id:
		last_update_id = current_update_id

		chat_id = last_chat_info['message']['chat']['id']
		message_text = last_chat_info['message']['text']

		message_info = {
			'chat_id': chat_id,
			'text': message_text
		}
		return message_info

	return None


def send_message(answer):
	chat_id = answer['chat_id']
	text = answer['text']
	message = requests.get(f'{config.MAIN_URL}/sendMessage?chat_id={chat_id}&text={text}')
	# print(message.json())

def main():
	while True:
		answer = get_message()

		if answer != None:
			send_message(answer)
		else:
			continue

if __name__ == '__main__':
	main()