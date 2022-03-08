
#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding='utf-8'
# encoding:'utf-8'

import datetime
# ULAK_1 api informations:
# api_key = "AIzaSyA75Ze1rKjAvjMQl6LInLC0zOEYwQpNntM"
# search_engine_id = '83f517ac088e46727'

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


"""
Notes about root_file :

# result = resource.list(q='covit-19', cx=search_engine_id).execute()

# you can search images as well
# result = resource.list(q='python', cx=search_engine_id, searchType='image').execute()

# print(result)

# print(len(result["items"]))

# print(result['items'][0])

# for item in result['items']:
#     print(item['title'], item['link'])
"""
"""
def backup_and_clean_results(_backup_file, _clean_file):
    backing_up = open(_clean_file, 'r+', encoding='utf-8')
    file_back_up = backing_up.read()
    old_file = open(_backup_file, 'a', encoding='utf-8')
    old_file.write(f"\n---\n{file_back_up}")
    old_file.close()
    backing_up.truncate(0)
    backing_up.close()

# backup_and_clean_results("old_results.txt", "results.txt")

p = open("results.txt", 'r+', encoding='utf-8')
p.truncate(0)
p.close()
"""

