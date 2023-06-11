"""Модуль для ввода марки и модели авто, сбора данных с сайта и записи их в файл"""

import requests
import json


url = 'https://auto.ru/-/ajax/desktop/listing/'

# здесь планируется наисать функцию авторизации  и получения нужного токена
headers = '''********'''.strip().split("\n")    #из строки превращаем все в словарь

def requests_avto(chek_mark, chek_model, headers):
    """
    Принимает значения Марки chek_mark и Модели мошины, chek_model
    headers - заголовки запроса
    функция возвращает первое значение марка и модель автомобиля и второе значение количество таких моделей
    """
    dict_headers = {}
    headers_1 = headers
    chek_mark_1 = str.upper(chek_mark)
    chek_model_1 = str.upper(chek_model)
    
    for header in headers_1:
        key, value = header.split(': ')
        dict_headers[key] = value

    offers =[]
    for x in range(1,5):       # для примера не все 99 страниц
        param = {              # параметры для поиска
            "top_days":"1",
            "category":"cars",
            "section":"all",
            "page":1,
            "catalog_filter":[{"mark":"HYUNDAI","model":"SOLARIS"}],
            "geo_id":[],
        }
        param["catalog_filter"] = [{"mark": chek_mark_1,"model": chek_model_1}]
        

        r = requests.post(url, json=param, headers = dict_headers, verify=False)     
        data = r.json()
        offers.extend(data['offers'])
        # print("page ", x)

    with open("data.json", "w") as f:
        json.dump(offers, f)
    mark_model = chek_mark_1 + ' ' +chek_model_1   
    quantity = len(offers)
    # f.seek(0)
    f.close()
    return [mark_model, quantity]

def input_mark():
    a = requests_avto(input("введите марку: "), input("введите модель: "), headers)
    print("Автомобиль марки -", a[0], " Количество: ", a[1], " шт.")

# input_mark()

   
