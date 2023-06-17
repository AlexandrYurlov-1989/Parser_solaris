#!/.venv/bin/python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : name: Yurlov A. A. emil: alexandryurlov@rambler.ru
# Created Date: 12.06.23
# version ='0.1.3'
# ---------------------------------------------------------------------------
"""Модуль для добавления собранных метрик в пакеты и отправки их в на сервер kafka"""

import json
import time
from Sender2Monitoring import PacketMetrics, Metric
import solaris

# Вызваем функцию для выбора марки и модели автомобиля, и записи в файл data.json
solaris.input_mark()

def price():
    """Получение словаря с ключом price из файла с данными
		Возвращает:
		price - все цены по данным из полученных обьявлений
	"""
    with open("data.json", "r", encoding="utf8")  as file:
        data = json.load(file)  # теперь это словарь
    price_avto = [] #словарь для записи цен
    file.close()
    for offer in data:
        if offer['price_info']:
            price_avto.append(offer['price_info']['price'])

    return price_avto

value_price = price() # записываем все значения цен в переменную

# settings - настройки скрипта, содержащие адреса серверов мониторинга.
# kafka кластер для тестирования. Поднят для экспериментов 'dev-kafkaServers': 'mon-test-kafka1'
settings = {'dev-kafkaServers': 'mon-test-kafka1'}

# Получение Time Stamp для метрик
time_stamp = round(time.time())
now = time_stamp

# Создает объект packet класса PacketMetrics, который будет содержать в себе набор объектов Metric
packet = PacketMetrics(60)

# цикл для обновления значения цены в метрике и отправки в пакет
for value_one in value_price:
    # Создает объект metric класса Metric
    metric = Metric('Solaris',  # имя метрики
                    now,  # timestamp
                    value_one,  # значение
                    tags={  # набор тэгов
                        'script': __file__.split('/')[-1:][0],  # какой скрипт шлет метрику
                        'contur': 'dev-kafkaServers', # обязательный тэг contur
                        'service': 'someService',  # прочие тэги
                        'subsystem': 'someSubsystem'
                        }, replace_symbol="/")

    packet.add_metric(metric) # добовляем метрику в пакет

# отправляет пакет в Мониторинг
# settings - здесь пока настройка с введенными в ручную адресом сервера
# debug - False по-умолчанию, при True - осуществляется вывод print stdout вместо отправки
# отправка идёт в environment dev для теста
packet.send_packet(settings, debug=True, environment='dev')
