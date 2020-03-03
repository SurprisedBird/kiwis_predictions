import random
import bot

PREDICTION_1 = "Лапа"
PREDICTION_2 = "Клюв"
PREDICTION_3= "Крылышко"
PREDICTION_4 = "Перья"

prediction_list = [PREDICTION_1, PREDICTION_2, PREDICTION_3, PREDICTION_4]
prediction_list_len = len(prediction_list)

def make_prediction(number):
    random.shuffle(prediction_list)
    prediction = prediction_list[number-1]
    print(prediction)

def process_input():
	while True:
	    messege = input(f"Введите число от 1 до {prediction_list_len} \n")
	    pred_number = bot.message_text
	    if not pred_number.isdigit():
	        print("Введите число, не расстраивайте птичку киви")
	    elif not 0 < int(pred_number) <= prediction_list_len:
	        print(f"Птички киви живут до 60-ти лет. И она навсегда запомнит, что введенное вами число не входит в интервал от 1 до {prediction_list_len}")
	    else:
	        return int(pred_number)

pred_number = process_input()
make_prediction(pred_number)