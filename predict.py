import random
import re

def is_in_range(func):
    def wrapper(*args):
        number = func(*args)
        if not 0 < int(number) <= args[0].prediction_list_len:
            message_text = f"Птички киви живут до 60-ти лет. И она навсегда запомнит, что введенное вами число не входит в интервал от 1 до {args[0].prediction_list_len}"
        else:
            message_text = int(number)
        return message_text
    return wrapper

class Predictions():

    PREDICTION_1 = "Лапа"
    PREDICTION_2 = "Клюв"
    PREDICTION_3= "Крылышко"
    PREDICTION_4 = "Перья"

    prediction_list = [PREDICTION_1, PREDICTION_2, PREDICTION_3, PREDICTION_4]
    prediction_list_len = len(prediction_list)

    def shuffle_predictions(self):
        random.shuffle(self.prediction_list)

    def make_prediction(self, number):
        prediction = self.prediction_list[number-1]
        text = prediction

        return text

    @is_in_range
    def convert_to_int(self, number):
        print(number)
        number = int(number)
        return number

    def process_input(self, pred_number):
        text = pred_number
        is_any_number = any(i.isdigit() for i in pred_number)
        if is_any_number:
            text = re.search(r'\d+', pred_number)[0]
            text = self.convert_to_int(text)
        else:
            text = "Введите число, не расстраивайте птичку киви"
        
        return text


        
"""     def check_strint(self, pred_number):
        if not pred_number.isdigit():
            text = "Введите число, не расстраивайте птичку киви"
            is_any_number = any(i.isdigit() for i in pred_number)
            if is_any_number:
                number = re.search(r'\d+', pred_number)[0]
                number = int(text) """
                
        