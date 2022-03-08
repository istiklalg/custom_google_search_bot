

# @author : istiklal

import datetime

k = open('keywords.txt', 'r', encoding='utf-8')
# k = [x.rstrip("\n") for x in config.readlines()]
# keywords = k.readlines()
keywords = k.read().splitlines()
k.close()
print(keywords)

for keyword in keywords:
   print(keyword)

today = datetime.date.today()
print(today.strftime("%Y%m%d"))
three_month = datetime.timedelta(days=90)
before = today.__sub__(three_month)
print(before)

search_time = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
print(search_time)


