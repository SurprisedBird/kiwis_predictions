import config
from predict import Predictions
import requests
import json

from flask import Flask
from flask import request
from flask import jsonify

from flask_sslify import SSLify

app = Flask(__name__)
predictions = Predictions()

# sslify = SSLify(app)

def send_message(chat_id, text):
	if type(text) == int:
		sended_text = predictions.make_prediction(text)
	else:
		sended_text = text

	url = config.MAIN_URL + '/sendMessage'
	payload = {"chat_id": str(chat_id), "text": sended_text}
	headers = {'Content-type': 'application/json'}
	
	r = requests.post(url, json=payload, headers=headers)

	return r

def convert_input(text):
	if text == '/start':
		message_text = f"Введите номер предсказания от 1 до {predictions.prediction_list_len}"
		predictions.shuffle_predictions()
	elif text =="Птичка киви хочет цифру":
		message_text = text
	else:
		message_text = predictions.process_input(text)

	return message_text
	

@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		r = request.get_json()
		#print(json.dumps(r, indent = 4))
		if 'text' in r['message']:
			message_text = r['message']['text']
		else:
			message_text = "Птичка киви хочет цифру"
		chat_id = r['message']['chat']['id']
		
		message_text = convert_input(message_text)
		send_message(chat_id, message_text)

		return "!", 200

	return request.method

def main():
	print('Main was runed')

if __name__ == '__main__':
	app.run()
