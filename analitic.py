import json
from Sender2Monitoring import PacketMetrics, Metric
import time
import solaris

solaris.input_mark()
#  функция парсинга файла data.json и возврата всех значение ключа price - это цены за текущий день на Солярис
def price():
  with open("data.json", "r", encoding="utf8")  as f:
    data = json.load(f)  # теперь это словарь
  print(len(data))
  price = []
  f.close()
  for offer in data:
    if offer['price_info']:
      price.append(offer['price_info']['price'])

  print(price)
  return price

price()

# settings = {dev-kafkaServers: 'mon-test-kafka1'} # kafka кластер для тестирования. Поднят для экспериментов

# # Получение Time Stamp для метрик
# time_stamp = round(time.time())

# # Класс PacketMetrics(interval) 
# # interval - интревал сбора в секундах
# # Создает объект packet класса PacketMetrics, который будет содержать в себе набор объектов Metric
# packet = PacketMetrics(60)

# solaris_price = price() # вызов функции и присвоение возвращенного значения

# metric = Metric('SomeMetricName',  # тэг name
#                 now,  # timestamp
#                 solaris_price,  # значение
#                 tags={  # набор тэгов
#                     'script': __file__.split('/')[-1:][0],  # рекомендуется для понимания что за скрипт шлет метрику
#                     'contur': 'prod', # обязательный тэг contur
#                     # если отправка идёт в environment prod, то contur должен быть prod
#                     # если отправка идёт в любой другой environment, то contur может быть любым, но не пустым.
#                     'service': 'someService',  # прочие тэги
#                     'subsystem': 'someSubsystem'
#                     })
#                 # zabbix_metric='SomeZabbixMetric',  # item в заббиксе, если пакет готовится в т.ч. для zabbix
#                 # zabbix_host_name='SomeZabbixServerName')  # хост в заббиксе, если пакет готовится в т.ч. для zabbix



 