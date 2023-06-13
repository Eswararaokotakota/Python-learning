
import threading
import datetime
import time

def samplethread():

    def print_time():
        for i in range(0,5):
            print(datetime.datetime.now(),"thread1",i)
            time.sleep(1)
    def print_time2():
        for i in range(0,7):
            print(datetime.datetime.now(), "thread2",i)
            time.sleep(1)

    # print_time()
    # print_time2()
    thread1 = threading.Thread(target=print_time, args=())
    thread2 = threading.Thread(target=print_time2, args=())

    thread1.start()
    thread2.start()  #Working printing the current time paralelly

samplethread()