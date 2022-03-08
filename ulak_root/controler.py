import schedule
import timing

def write_hello():
    print("hello")

schedule.every(10).seconds.do(write_hello)
# schedule.every().day.at('23:59').do(write_hello)

