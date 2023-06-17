#!/.venv/bin/python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : name: Yurlov A. A. emil: alexandryurlov@rambler.ru
# Created Date: 12.06.23
# version ='0.1.3'
# ---------------------------------------------------------------------------
"""Модуль для ввода марки и модели авто, сбора данных с сайта и записи их в файл"""


# region IMPORT
import json
import requests
# endregion

# region variables
URL = 'https://auto.ru/-/ajax/desktop/listing/'

 # здесь в будущих версиях планируется наисать функцию авторизации и получения нужного токена
request_headers = '''***
'''.strip().split("\n")
# endregion

# region basic functions

def requests_avto(chek_mark, chek_model, headers):
    """
    Принимает значения Марки-chek_mark и Модели мошины-chek_model
    headers - заголовки запроса
    функция возвращает первое значение марка и модель автомобиля и второе количество
    Возвращает:
        mark_model - Название: марка и модель
        quantity - количество полученных объявлений
    """
    dict_headers = {}

    for header in headers:
        key, value = header.split(': ')
        dict_headers[key] = value

    offers =[]
    for page_x in range(1,5):       # для примера не все 99 страниц
        param = {              # параметры для поиска
            "top_days":"1",
            "category":"cars",
            "section":"all",
            "page":page_x,
            "catalog_filter":[{"mark":"HYUNDAI","model":"SOLARIS"}],
            "geo_id":[],
        }
        param["catalog_filter"] = [{"mark": chek_mark,"model": chek_model}]

        request = requests.post(URL, json=param, headers = dict_headers, verify=False,\
                                timeout=(3.05, 27))
        data = request.json()
        offers.extend(data['offers']) # запишим только славари с ключом 'offers'

    with open("data.json", "w", encoding='utf-8') as file:
        json.dump(offers, file)
    mark_model = chek_mark + ' ' +chek_model
    quantity = len(offers)
    file.close()
    return [mark_model, quantity]

def check_car_make(car_make, car_model):
    """Определяет правильность ввода марки автомобиля из кортежей"""
    allowed_makes = ['TOYOTA', 'HONDA', 'FORD', 'KIA']
    allowed_models = ['CAMRY', 'CEED']
    if car_make in allowed_makes:
        if car_model in allowed_models:
            return True
        raise ValueError('Недопустимая модель машины')
    raise ValueError('Недопустимая марка машины')

def input_mark():
    """Ввод марки и модели машины ввиде аргументов к функции requests_avto"""
    while True:
        car_make = str.upper(input("введите марку: "))
        car_model = str.upper(input("введите модель: "))
        try:
            check_car_make(car_make, car_model)
            avto = requests_avto(car_make, car_model, request_headers)
            # check_car_make(car_make, car_model, a[1])
            print("Автомобиль марки -", avto[0], " Количество: ", avto[1], " шт.")
            break
        except ValueError as err:
            print(err)
input_mark()
# endregion
