
"""
@author : istiklal
API Infos and Class level definitions for APIS
"""

class UlakSearchEngine:
    def __init__(self, _api_key, _search_engine_id):
        self.api_key = _api_key
        self.search_engine_id = _search_engine_id


#s2 = UlakSearchEngine("WWWkloım95535443reomervle", "55555sdfsdfs555")

# decorator function for object error handler
def engine_test(func):
    def inner(*args, **kwargs):
        x = args[0]
        if type(x) != UlakSearchEngine:
            print(f"{x} is not an instance of UlakSearchEngine an it's skipped without searching")
            pass
        else:
            return func(*args, **kwargs)
    return inner

@engine_test
def view(engine, num):
    print(str(engine.search_engine_id)+" "+str(num))
    print(f" Bu nesne için süreç ilerledi ")
    

# view(s1, 7645)
#view(s2, 16352)
#view("bu NE", 5)


        
            

"""
# an example for search function creation:
------------------------------------------
from googleapiclient.discovery import build

my_api_key = "YOUR_API_KEY"
my_cse_id = "YOUR_CSE_ID"

def google_results_count(query):
    service = build("customsearch", "v1",
                    developerKey=my_api_key)
    result = service.cse().list(q=query, cx=my_cse_id, sort="date:r:20110101:20131231").execute()
    return result["searchInformation"]["totalResults"]

print google_results_count('arab spring site:www.cnn.com')
"""