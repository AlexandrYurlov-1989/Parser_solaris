#!/.venv/bin/python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : name: Yurlov A. A. emil: alexandryurlov@rambler.ru
# Created Date: 12.06.23
# version ='0.1.3'
# ---------------------------------------------------------------------------

import json
from Sender2Monitoring import PacketMetrics, Metric
import time 
import Solaris

# Вызваем функцию для выбора марки и модели автомобиля, и записи данных полученных обьявлений в файл data.json 
Solaris.input_mark() 

def price():
	"""Получение словаря с ключом price из файла с данными
		Возвращает:
		price - все цены по данным из полученных обьявлений
	"""
	with open("data.json", "r", encoding="utf8")  as f:
		data = json.load(f)  # теперь это словарь
	price = [] #словарь для записи цен 
	f.close()
	for offer in data:
		if offer['price_info']:
			price.append(offer['price_info']['price']) #записываем в словарь все значения ключа 'price' (цены) 

	return price

value_price = price() # записываем все значения цен в переменную

# settings - настройки скрипта, содержащие адреса серверов мониторинга.
# kafka кластер для тестирования. Поднят для экспериментов 'dev-kafkaServers': 'mon-test-kafka1'}
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
                        'script': __file__.split('/')[-1:][0],  # рекомендуется для понимания что за скрипт шлет метрику
                        'contur': 'dev-kafkaServers', # обязательный тэг contur
                        'service': 'someService',  # прочие тэги
                        'subsystem': 'someSubsystem'
                        }, replace_symbol="/")
                  
    packet.add_metric(metric) # добовляем метрику в пакет

# отправляет пакет в Мониторинг
# settings - здесь пока настройка с введенными в ручную адресом сервера
# debug - False по-умолчанию, при True - осуществляется вывод print (stdout) вместо отправки
# отправка идёт в environment dev для теста
packet.send_packet(settings, debug=True, environment='dev')
