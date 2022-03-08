
"""
@author : istiklal
calculating date and time for search date / time filter
"""

import datetime
from postman import despatch_rider, despatch_rider_HTML, read_content


today = datetime.date.today()
print(today.strftime("%Y%m%d"))
three_month = datetime.timedelta(days=90)
before = today.__sub__(three_month)
print(before)


def create_sort_sentence(last_date=datetime.date.today(), first_date=0, days_do_earlier=1):
    """
    last_date : last date of date interval, it needs a datetime object
    first_date : first date of date interval, it needs a datetime object
    days_to_earlier : how many days to go earlier from last date of interval for sorting results
    configure a sort sentence for date filter case.
    """
    _sentence =""
    if first_date == 0 and type(last_date) == datetime.date:
        t1 = last_date.strftime("%Y%m%d")
        t2 = last_date.__sub__(datetime.timedelta(days=days_do_earlier)).strftime("%Y%m%d")
        _sentence = f"date:r:{t2}:{t1}"
    elif type(first_date) == datetime.date :
        t1 = last_date.strftime("%Y%m%d")
        t2 = first_date.strftime("%Y%m%d")
        _sentence = f"date:r:{t2}:{t1}"
    else:
        print("We got Type Error About given variables")
        with open('exceptions.txt', 'a', encoding='utf-8') as exception:
            exception.write(f"\n**({datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}) - create_sort_centence function - variable type ERROR")
    
    return _sentence


test = create_sort_sentence()
print(test)

def denemek_icin(alicilar):
    try:
        despatch_rider(_content_file="results.txt", _receipents_file=alicilar)
    except Exception as err:
        print(err)
        with open('exceptions.txt', 'a', encoding='utf-8') as exception:
            exception.write(f"\n**({datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}) - dispatch_rider function - ({err})\n")



def html_denemek_icin(alicilar):
    try:
        despatch_rider_HTML(_content_file="results.txt", _receipents_file=alicilar)
    except Exception as err:
        print(err)
        with open('exceptions.txt', 'a', encoding='utf-8') as exception:
            exception.write(f"\n**({datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}) - dispatch_rider_html function - ({err})\n")



def testing_html_template(alicilar="ben.txt"):
    try:
        despatch_rider_HTML(_content_file="sonuc.txt", _receipents_file=alicilar, _template_file="mesaj.html")
    except Exception as err:
        print(err)
        # with open('exceptions.txt', 'a', encoding='utf-8') as exception:
        #     exception.write(f"\n**({datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}) - dispatch_rider_html function - ({err})\n")

# testing_html_template()
