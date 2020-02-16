import random

PREDICTION_1 = "Лапа"
PREDICTION_2 = "Клюв"
PREDICTION_3= "Крылышко"
PREDICTION_4 = "Перья"

prediction_list = [PREDICTION_1, PREDICTION_2, PREDICTION_3, PREDICTION_4]
prediction_list_len = len(prediction_list)

def make_prediction(number):
    number = int(number)

    random.shuffle(prediction_list)
    prediction = prediction_list[number-1]
    print(prediction)

def process_input():
	while True:
	    pred_number = input(f"Введите число от 1 до {prediction_list_len} \n")
	    if not pred_number.isdigit():
	        print("Введите число, не расстраивайте птичку киви")
	    elif not 0 < int(pred_number) <= prediction_list_len:
	        print(f"Вы снова расстроили птичку киви. Введенное число не входит в интервал от 1 до {prediction_list_len}")
	    else:
	        return pred_number
	        break

pred_number = process_input()
make_prediction(pred_number)