
"""
@author : istiklal
API Infos and Class level definitions for APIS
"""

class UlakSearchEngine:
    def __init__(self, _api_key, _search_engine_id):
        self.api_key = _api_key
        self.search_engine_id = _search_engine_id


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
  
