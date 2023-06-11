import json
from Sender2Monitoring import PacketMetrics, Metric
import time
import Solaris

Solaris.input_mark()
#  функция парсинга файла data.json и возврата всех значение ключа price - это цены за текущий день на Солярис
def price():
  with open("data.json", "r", encoding="utf8")  as f:
    data = json.load(f)  # теперь это словарь
#   print(len(data))
  price = []
  f.close()
  for offer in data:
    if offer['price_info']:
      price.append(offer['price_info']['price'])

#   print(price)
  return price

value_price = price()

settings = {'dev-kafkaServers': 'mon-test-kafka1'} # kafka кластер для тестирования. Поднят для экспериментов 'dev-kafkaServers': 'mon-test-kafka1'}

# Получение Time Stamp для метрик
time_stamp = round(time.time())
now = time_stamp

packet = PacketMetrics(60)

for value_one in value_price:
      # Создает объект metric класса Metric
  metric = Metric('Solaris',  # имя метрики
                  now,  # timestamp
                  value_one,  # значение
                  tags={  # набор тэгов
                      'script': __file__.split('/')[-1:][0],  # рекомендуется для понимания что за скрипт шлет метрику
                      'contur': 'dev-kafkaServers', # обязательный тэг contur
                      # если отправка идёт в environment prod, то contur должен быть prod
                      # если отправка идёт в любой другой environment, то contur может быть любым, но не пустым.
                      'service': 'someService',  # прочие тэги
                      'subsystem': 'someSubsystem'
                      }, replace_symbol="/")
                  
  packet.add_metric(metric)

packet.send_packet(settings, debug=True, environment='dev')
