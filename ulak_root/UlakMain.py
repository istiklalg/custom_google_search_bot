
"""
encoding:utf-8
@author : istiklal

"""
from googleapiclient import discovery
from passcodes import istiklal_api_key, ulak_1_search_engine_id, ulak_2_search_engine_id, ulak_3_search_engine_id
from ULAK_APIS import UlakSearchEngine
from timing import create_sort_sentence
from searcher import start_search, backup_and_clean_results, ulak_digger
from postman import despatch_rider, despatch_rider_HTML
import datetime


with open('exceptions.txt', 'a', encoding='utf-8') as exception:
    exception.write(f"\n**({datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}) - UlakMain triggered\n")


ulak_1 = UlakSearchEngine(istiklal_api_key, ulak_1_search_engine_id)
ulak_2 = UlakSearchEngine(istiklal_api_key, ulak_2_search_engine_id)
ulak_3 = UlakSearchEngine(istiklal_api_key, ulak_3_search_engine_id)

# to create and use more than one search engine
engine_list = [ulak_1, ulak_2, ulak_3]

# backing up existing results.txt to old_results.txt and clean it for new search
backup_and_clean_results("old_results.txt", "results.txt")

# 90 day search limit for new search according to today
sort_sentence = create_sort_sentence()

try:
    ulak_digger(engine_list, date_sort_sentence=sort_sentence)
except Exception as err:
    print(err)
    with open('exceptions.txt', 'a', encoding='utf-8') as exception:
            exception.write(f"\n**({datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}) - UlakMain calling start_search function - ({err}) - ({engine_list})\n")

try:
    despatch_rider_HTML(_content_file="results.txt", _receipents_file="mail_receipents.txt")
except Exception as err:
    print(err)
    with open('exceptions.txt', 'a', encoding='utf-8') as exception:
        exception.write(f"\n**({datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}) - dispatch_rider function - ({err})\n")