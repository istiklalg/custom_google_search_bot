
"""
encoding:utf-8
@author : istiklal

"""
from googleapiclient import discovery
from passcodes import istiklal_api_key, ulak_1_search_engine_id, ulak_2_search_engine_id, ulak_3_search_engine_id
from ULAK_APIS import UlakSearchEngine
from timing import create_sort_sentence
from searcher import start_search, backup_and_clean_results
from postman import despatch_rider
import datetime

with open('exceptions.txt', 'a', encoding='utf-8') as exception:
    exception.write(f"\n**({datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}) - ulak_root triggered\n")


ulak_1 = UlakSearchEngine(istiklal_api_key, ulak_1_search_engine_id)
ulak_2 = UlakSearchEngine(istiklal_api_key, ulak_2_search_engine_id)
ulak_3 = UlakSearchEngine(istiklal_api_key, ulak_3_search_engine_id)

engine_list = [ulak_1, ulak_2, ulak_3]

backup_and_clean_results("old_results.txt", "results.txt")

sort_sentence = create_sort_sentence()

for engine in engine_list:
    try:
        start_search(engine, date_sort_sentence=sort_sentence)
    except Exception as err:
        print(err)
        with open('exceptions.txt', 'a', encoding='utf-8') as exception:
            exception.write(f"\n**({datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}) - ulak_root calling start_search function - ({err}) - ({engine})\n")
        

try:
    despatch_rider(_content_file="results.txt")
except Exception as err:
    print(err)
    with open('exceptions.txt', 'a', encoding='utf-8') as exception:
        exception.write(f"\n**({datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}) - dispatch_rider function - ({err})\n")


