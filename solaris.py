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

 # здесь в будущих версиях планируется наисать функцию авторизации  и получения нужного токена
request_headers = '''
Authority: auto.ru
Method: POST
Path: /-/ajax/desktop/listing/
Scheme: https
Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6
Content-Length: 144
Content-Type: application/json
Cookie: gdpr=0; spravka=dD0xNjg1NzgyNzM4O2k9NzcuMjIwLjUxLjIxMDtEPUQzNzZCOUYwNjA3RjJDQjc0MkU5Qzk3
RkUzRUQ3OEU3QjE1RDgwOUVCMzhEM0U5RDMzRjE3Q0RGRjU5OUFDNUE0ODg4NDc5NDg0NEZGQUFFNjNEMTcyMkYyRDIwREYw
ODIwNUM7dT0xNjg1NzgyNzM4MTc0NDI4NjI0O2g9MGRhZDZhNTY3ZGY0NmJjNzEwZWNkZWZhOTEwN2E1ZGQ=; suid=b88f0
b653d62efc81cd8c07126891c97.5a28716851536010cdf14dc74e8b1bbc; _csrf_token=c1496c99b6068cf3ae4c58
834ab947d11e4fcca3e8c295f2; autoru_sid=a%3Ag647b00d22cskghcb2923c42crvele52.d4e458802ef9282fc215
ba7ee330c9b6%7C1685782738403.604800.FVb6orN2UVKW7vg0JVAZXg.0uahn1diHOBN3K2cHCKwCZM1RqatM2d6f5gOz
xS3idA; autoruuid=g647b00d22cskghcb2923c42crvele52.d4e458802ef9282fc215ba7ee330c9b6; from=direct
; yuidlt=1; yandexuid=390820861674325034; _ym_uid=1685782735622551257; _ym_isad=2; crookie=AgOL3
WMWS7/IHBB5mJm+5jjT0pZJcwt4th1CBX4zVUeUvTDH6Wkhfj73O0JmQ73GDyYxAeQrn+zibSjNxNn2Yahe5hQ=; cmtchd=
MTY4NTc4Mjc0ODU5MQ==; yandex_login=; i=2T5Dt3ghv2IXFUmjPI7VwOxtWFr9X0l23YogDBLCGIibe6YXiar6YFBwB
Kqw3da+vSSuxd6cVkzcxQGUqnbbTL5XkU4=; yaPassportTryAutologin=1; cycada=CqWMNH7+UH6YsVXK34QEjW3unp
BXQc3PrSx5jsIvXeA=; _ym_d=1685796690; _yasc=anoziatQHBeloyVjPNXlS5GDXuRIYMRmLugGGkTQNlO6hEPiVThm
acv0k/SdpQ==; layout-config={"screen_height":864,"screen_width":1536,"win_width":1536,"win_heigh
t":296}; count-visits=6; from_lifetime=1685796698907; Session_id=noauth:1685796699; sessar=1.99.CiB3Hgl6mX6AQegJgR9u7KZxJCxuhkqfFu9mJGStErazSg.yXkgwk6qXkB8ifGz49SyyBtTbdl_wVEgChIg2ah3k08; ys=w
prid.1685782533906348-17486272844148808132-balancer-l7leveler-kubr-yp-sas-81-BAL-7474#c_chck.156
2372776; mda2_beacon=1685796699004; sso_status=sso.passport.yandex.ru:synchronized
Origin: https://auto.ru
Referer: https://auto.ru/yaroslavl/cars/hyundai/solaris/used/
Sec-Ch-Ua: "Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: same-origin
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chr
ome/113.0.0.0 Safari/537.36
X-Client-App-Version: 388.0.11623293
X-Client-Date: 1685796787527
X-Csrf-Token: c1496c99b6068cf3ae4c58834ab947d11e4fcca3e8c295f2
X-Page-Request-Id: beb54648834f97e51e4df86ceddd9d35
X-Requested-With: XMLHttpRequest
X-Retpath-Y: https://auto.ru/yaroslavl/cars/hyundai/solaris/used/
X-Yafp: {"a1":"4J8mXURbpTsGig==;0","a2":"3Kdan+wzpbMSEHR6Rle5H5KAT0DHmQ==;1","a3":"ILBPfSb3giRSX
KBNWr+QJg==;2","a4":"7aW9gZ9fwPgjAlAKWW5GF7fGWh//MzaXalIZhh96TzqRpTNMOh7ouNJ3BbGrRw==;3","a5":"G
faqJuMUyrkxWA==;4","a6":"di8=;5","a7":"wgZs81thiMtB4w==;6","a8":"OiKzr1f36Fk=;7","a9":"VFh2S7zdK
Bhv9w==;8","b1":"40kUqavI2ZU=;9","b2":"PTwuc7w5mDM/ew==;10","b3":"EBJZc1KHLH4kUA==;11","b4":"2IK
oKVXnNAc=;12","b5":"i98ElUm19OWTRQ==;13","b6":"wgCu84klVE5o4w==;14","b7":"q6t5InG4azs0PQ==;15","
b8":"Yl43OlPouu3J5A==;16","b9":"5A4DMp3DyOxMcQ==;17","c1":"J12HsA==;18","c2":"8AEnmF2nrL/tXF5erF
T13Q==;19","c3":"fZWGh4G/76f3jwjNJ3HcJA==;20","c4":"+x5YOPUgPFw=;21","c5":"iynaiJeivdc=;22","c6"
:"j4Hvqg==;23","c7":"d6zwTW6247U=;24","c8":"7aw=;25","c9":"CkgoUVwf7hU=;26","d1":"keiEe0VEJwk=;2
7","d2":"UtNf8Q==;28","d3":"4T3XcUY2/Pi4Ew==;29","d4":"FJsDofOKtIs=;30","d5":"ksUHznewyX4=;31","
d7":"Bt9SW2L13gw=;32","d8":"rznpDO3mvpcyAyZFaT1kC5sVj+C8KJwpeqA=;33","d9":"EdRsaAY5sus=;34","e1"
:"LNd6DvGKv+mZRg==;35","e2":"/ezy+eviV2w=;36","e3":"OKcMXH9S1CU=;37","e4":"aLoby4wKsSA=;38","e5"
:"4l6qfmCxOP259g==;39","e6":"4/jI/6BaSWc=;40","e7":"Wg8b3Vrqu5BozQ==;41","e8":"F3O1M/dJelg=;42",
"e9":"E5UhWFKwfn0=;43","f1":"+molBcBALQTLbw==;44","f2":"n7al7xqcdDc=;45","f3":"tQ2ARzUnsAjVJA==;
46","f4":"B4O5fTvx+1s=;47","f5":"ozNniNlsJtFY2g==;48","f6":"WtG1mIaGdB+q8Q==;49","f7":"3Q8XxYZuc
yTg9Q==;50","f8":"A+AREtaH25apTw==;51","f9":"sleQzLI79gs=;52","g1":"yjYPB8kOdxamkQ==;53","g2":"j
Y3BZbdf4MT6Sw==;54","g3":"LUjtxu16k90=;55","g4":"VpxsaPbT+4aBZQ==;56","g5":"ERoXZZDuZHQ=;57","g6
":"maxJ/l4M86o=;58","g7":"IUMiHj6eRUc=;59","g8":"PaUYXaVoa8Y=;60","g9":"HwJWMhrstyg=;61","h1":"l
YyikYEpZGg7tQ==;62","h2":"5tVADJyiiHmkxg==;63","h3":"Te1gSSORhmZzWA==;64","h4":"RBjbIa91XKNHqg==
;65","h5":"tAv7MIyjUfw=;66","h6":"DQlmVmEIuN3zgA==;67","h7":"K2uqE0l47ziEB6fVOGWYl6iuf8tcjuioHg2
Xam5g3CxB+eVR;68","h8":"dYztBuooSNqz8w==;69","h9":"AOW4HEkfnQReZQ==;70","i1":"g2oImXslPXg=;71","
i2":"iXmAkV7djB5NHw==;72","i3":"qJU0rLwxjtSapQ==;73","i4":"S0OCONZsUCJe4g==;74","i5":"vF1bt3DhXp
NCIQ==;75","z1":"IYYcC+u5Jutdj6+HIObQHgVy83qCxaBYB7KQcZtI0NcOEOar88spT7LS/1TG2TRq3r0Wm/Ubj+/cRPh
A7/tj1A==;76","z2":"kSnKgmvM2Jc2RicaGDrUQYIb/rzGOhAHbepWF3ZJi2J4APwZYENVNMlfWS7K80l/EOeGlxo4fwCK
ZPs7pm/neQ==;77","y2":"RLr8zgmNcoC2Yw==;78","y3":"XYDLJX9D0kBCsw==;79","y6":"bRkwJ3OdK/9XsQ==;80
","y8":"Rq9/2lL/FKopOw==;81","x4":"a0xVxjkp5F2P2g==;82","z5":"kuNCcHY7elw=;83","z4":"o/SWkoMcC/b
mwA==;84","z6":"VZHAlRW96+7aEE/7;85","z7":"/ic/Afh6Ox7HEu4o;86","z8":"+bvFYfd+uR8hjykwkOY=;87","
z9":"y6ADfYUpbKM2FCLr;88","y1":"ar4kPM+/+zFlXZsb;89","y4":"r06PzV2l80keh+IN;90","y5":"NTh5vaJ83t
ELc6bCIQo=;91","y7":"bEMilPLHUKoRXF0Q;92","y9":"9NEXEw/gJFOtiudZ+1c=;93","y10":"j8Dw3mZCoz1xYgH7
90w=;94","x1":"ynWKpHrkaBGfMH/T;95","x2":"AXRT6gdgW4M0cEPlya4=;96","x3":"sB8BvMbMeo4apQyx;97","x
5":"Ojs0/FpbhflFLBHk;98","z3":"91lKh/mgeQeHE3O1qh7Sl17+5vS/nS5nK2NojwGJWCw=;99","v":"6.3.1","pgr
dt":"gLODbI04rpY8ooupTPM84JbwTPU=;100","pgrd":"fVyAHEtUZhR37NCb3jIEMJr3hP3Iv7dB+tHXs2eBYgbKdI3U+j6GH72EFsR1OzG8bsCCeABFdpuS5W6xPQA73IcxHnY1yxel80W1RR9JMtCazL2cHj08Tq7UgO+5TWM2jQzNwXzKMFntSdbl
1UrdyJ1+fAqAR++fgtxWkbuSueXYaxJa+Xs297XV/OsoP5FnxPxObGQtHdosGthg7S5pv38KEbs="}
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
# endregion
