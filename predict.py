import random
import re
import config

class Predictions():
    prediction_list = config.prediction_list
    prediction_list_len = len(prediction_list)

    def shuffle_predictions(self):
        random.shuffle(self.prediction_list)

    def make_prediction(self, number):
        prediction = self.prediction_list[number-1]
        text = prediction

        return text

    def convert_to_int(self, number):
        print(number)
        number = int(number)
        return number

    def process_input(self, pred_number):
        is_any_number = any(i.isdigit() for i in pred_number)
        if is_any_number:
            text = re.search(r'\d+', pred_number)[0]
            if not 0 < int(text) <= self.prediction_list_len:
                text = f"Птички киви живут до 60-ти лет. И она навсегда запомнит, что введенное вами число не входит в интервал от 1 до {self.prediction_list_len}"
            else:
                text = int(text)
        else:
            text = "Введите число, не расстраивайте птичку киви"
        
        return text
