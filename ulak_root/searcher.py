
"""
encoding:utf-8
@author : istiklal
contain searcher functions
"""
from googleapiclient import discovery
from ULAK_APIS import engine_test
from timing import create_sort_sentence
import datetime



@engine_test
def start_search(engine, date_sort_sentence="", keywords_file='keywords.txt', results_file='results.txt', record_count=20):
    """
    starting a search process with given custom search engine which is instance of UlakSearchEngine class
    for given sort and search parameters:
        engine : An engine object instance of UlakSearchEngine Class
        date_sort_sentence : A filter sentence for constricting your search in between two date, 
        you can create it with create_sort_sentence function
        keywords_file : A file which will be read te get search keywords
        results_file : A file which will be used for writing results of search proccess
        record_count : Result count of each keyword search
    """
    search_time = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    print(search_time)

    k = open(keywords_file, 'r', encoding='utf-8')
    keywords = k.read().splitlines()
    k.close()

    f = open(results_file, 'a', encoding='utf-8')
    f.write(f"\nEXACT SEARCHING DATE & TIME : {search_time}\n")
    if date_sort_sentence == "":
        search_date_interval = " NO INTERVAL SELECTED"
    else:
        first_date = date_sort_sentence.split(":")[-2]
        last_date = date_sort_sentence.split(":")[-1]
        search_date_interval = f" {first_date} - {last_date}"
    f.write(f"\nSEARCHING BETWEEN DATES : {search_date_interval}\n")

    resource = discovery.build("customsearch", 'v1', developerKey=engine.api_key).cse()

    search_json = []

    # to walk in result pages for each keyword search action
    result_count = 0
    keyword_counter = 0
    for keyword in keywords:
        keyword_counter+=1
        search_results = []
        result_counter = 1
        f.write(f"\nKEYWORD ({keyword_counter}) - SEARCH RESULTS FOR '{keyword}' :\n")

        for i in range(1, record_count, 10):
            if date_sort_sentence == "":
                resource_object = resource.list(q=keyword, cx=engine.search_engine_id, start=i)
            else:
                resource_object = resource.list(q=keyword, cx=engine.search_engine_id, sort=date_sort_sentence, start=i)
            _result = resource_object.execute()
            search_json += _result
            try:
                if _result['items'] is not None:
                    search_results += _result['items']
            except Exception as err:
                print(f"There is no element like : {err}")
                with open('exceptions.txt', 'a', encoding='utf-8') as exception:
                    exception.write(f"\n**({datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}) - start_search function - ({err}) - ({engine}) - ({_result})\n")
        result_count += len(search_results)
        for item in search_results:
            f.write(f"{result_counter}- ***({item['snippet']})\n      **NEWS TITLE**({item['title']})\n      **LINK TO CONTENT**({str(item['link']).lower()})\n")
            result_counter+=1
        
    f.write(f"\n---------- Search operation is finished successfully for {keyword_counter} keyword, total result count is {result_count} ----------\n")
    f.close()

    with open("result.json", 'a', encoding='utf-8') as s_json:
        s_json.write(f"\n** Search results as complate JSON : {datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}\n{search_json}")
        try:
            for res in search_json.items():
                for k, v in res:
                    s_json.write(f"*** FOR KEY {k} VALUE IS {v}\n")
        except Exception as err:
            print("Error Writing to JSON file : {err}")
    print(f"Search operation is finished successfully for {keyword_counter} keyword, total result count is {keyword_counter*record_count}, you can find results in results.txt")


def backup_and_clean_results(_backup_file, _clean_file):
    backing_up = open(_clean_file, 'r+', encoding='utf-8')
    file_back_up = backing_up.read()
    old_file = open(_backup_file, 'a', encoding='utf-8')
    old_file.write(f"\n-- BACKING UP DATE & TIME : ({datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}) --\n{file_back_up}")
    old_file.close()
    backing_up.truncate(0)
    backing_up.close()
    print("Back-up and clean proccess successfully finished")
    with open('exceptions.txt', 'a', encoding='utf-8') as exception:
        exception.write(f"\n** Back-up and clean proccess successfully finished\n")
        

def ulak_digger(engineList, date_sort_sentence="", keywords_file='keywords.txt', results_file='results.txt', record_count=10):
    search_time = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    print(search_time)

    k = open(keywords_file, 'r', encoding='utf-8')
    keywords = k.read().splitlines()
    k.close()

    f = open(results_file, 'a', encoding='utf-8')
    f.write(f"\n<br>EXACT SEARCHING DATE & TIME : {search_time}<br>\n")
    if date_sort_sentence == "":
        search_date_interval = " NO INTERVAL SELECTED"
    else:
        first_date = date_sort_sentence.split(":")[-2]
        last_date = date_sort_sentence.split(":")[-1]
        search_date_interval = f" {first_date} - {last_date}"
    f.write(f"\n<br>SEARCHING BETWEEN DATES : {search_date_interval}<br>\n")

    resource = discovery.build("customsearch", 'v1', developerKey=engineList[0].api_key).cse()

    search_json = []

    result_count = 0
    keyword_counter = 0
    for keyword in keywords:
        keyword_counter+=1
        search_results = []
        result_counter = 1
        f.write(f"\n<h4>KEYWORD ({keyword_counter})- SEARCH RESULTS FOR '{keyword}' </h4>\n")
        
        for i in range(1, record_count, 10):
            if date_sort_sentence == "":
                for engine in engineList:
                    resource_object = resource.list(q=keyword, cx=engine.search_engine_id, start=i)
                    _result = resource_object.execute()
                    search_json += _result
                    try:
                        if _result['items'] is not None:
                            search_results += _result['items']
                    except Exception as err:
                        print(f"There is no element like : {err}")
                        with open('exceptions.txt', 'a', encoding='utf-8') as exception:
                            exception.write(f"\n**({datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}) - ulak_digger function - ({err}) - ({engine}) - ({_result})\n")
            else:
                for engine in engineList:
                    resource_object = resource.list(q=keyword, cx=engine.search_engine_id, sort=date_sort_sentence, start=i)
                    _result = resource_object.execute()
                    search_json += _result
                    try:
                        if _result['items'] is not None:
                            search_results += _result['items']
                    except Exception as err:
                        print(f"There is no element like : {err}")
                        with open('exceptions.txt', 'a', encoding='utf-8') as exception:
                            exception.write(f"\n**({datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}) - start_search function - ({err}) - ({engine}) - ({_result})\n")
        result_count += len(search_results)
        if len(search_results) > 0:
            for item in search_results:
                f.write(f"<div class='parts'><span class='counter'>{result_counter}-</span> ({item['snippet']})<br>\n      TITLE : <span class='title'>({item['title']})</span><br>\n      LINK : <a href='{str(item['link']).lower()}'>({str(item['link']).lower()})</a><br></div>\n")
                result_counter+=1
        else:
            f.write(f"\n<div class='parts'>      No current results were found for this searched keyword. <br></div>\n")
        
    f.write(f"\n<br><h4>---------- Search operation is finished successfully for {keyword_counter} keyword, total result count is {result_count} ----------</h4><br>\n")
    f.close()

    with open("result.json", 'a', encoding='utf-8') as s_json:
        s_json.write(f"\n** Search results as complate JSON : {datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}\n{search_json}")
        try:
            for res in search_json.items():
                for k, v in res:
                    s_json.write(f"*** FOR KEY {k} VALUE IS {v}\n")
        except Exception as err:
            print("Error Writing to JSON file : {err}")
    print(f"Search operation is finished successfully for {keyword_counter} keyword, total result count is {result_count}, you can find results in results.txt")
