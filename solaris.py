#!/.venv/bin/python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : name: Yurlov A. A. emil: alexandryurlov@rambler.ru
# Created Date: 12.06.23
# version ='0.1.3'
# ---------------------------------------------------------------------------
"""Модуль для ввода марки и модели авто, сбора данных с сайта и записи их в файл"""


# region IMPORT
import requests
import json
# endregion

# region variables
url = 'https://auto.ru/-/ajax/desktop/listing/'

 # здесь в будущих версиях планируется наисать функцию авторизации  и получения нужного токена
headers = '''************'''.strip().split("\n")    #из строки превращаем все в словарь   *** - копировать данные из заголовкорв запросов
# endregion

# region basic functions    

def requests_avto(chek_mark, chek_model, headers):
    """
    Принимает значения Марки-chek_mark и Модели мошины-chek_model
    headers - заголовки запроса
    функция возвращает первое значение марка и модель автомобиля и второе значение количество таких моделей
    Возвращает:
        mark_model - Название: марка и модель
        quantity - количество полученных объявлений
    """
    dict_headers = {}
    headers_1 = headers
    chek_mark_1 = chek_mark
    chek_model_1 = chek_model
    
    for header in headers_1:
        key, value = header.split(': ')
        dict_headers[key] = value

    offers =[]
    for x in range(1,5):       # для примера не все 99 страниц
        param = {              # параметры для поиска
            "top_days":"1",
            "category":"cars",
            "section":"all",
            "page":x,
            "catalog_filter":[{"mark":"HYUNDAI","model":"SOLARIS"}],
            "geo_id":[],
        }
        param["catalog_filter"] = [{"mark": chek_mark_1,"model": chek_model_1}]
        
        r = requests.post(url, json=param, headers = dict_headers, verify=False)     
        data = r.json()
        offers.extend(data['offers']) # из полученных данных запишим только славари с ключом 'offers'
        
    with open("data.json", "w") as f: # файл для хранения полученных заголовков по каждой машине
        json.dump(offers, f)
    mark_model = chek_mark_1 + ' ' +chek_model_1   
    quantity = len(offers)
    f.close()
    return [mark_model, quantity]

def check_car_make(car_make, car_model):
    allowed_makes = ['TOYOTA', 'HONDA', 'FORD', 'KIA']
    allowed_models = ['CAMRY', 'CEED']                 
    if car_make in allowed_makes:
        if car_model in allowed_models:
            return True
        else:
            raise ValueError('Недопустимая модель машины')
    else:
        raise ValueError('Недопустимая марка машины')

    if car_model in allowed_models:
        return True
    else:
        raise ValueError('Недопустимая модель машины')

def input_mark():
    """Ввод марки и модели машины ввиде аргументов к функции requests_avto"""
    while True:
        car_make = str.upper(input("введите марку: "))
        car_model = str.upper(input("введите модель: "))
        try:
            check_car_make(car_make, car_model)
            a = requests_avto(car_make, car_model, headers)
            print("Автомобиль марки -", a[0], " Количество: ", a[1], " шт.")
            break
        except ValueError as e:
            print(e)
 
# endregion
