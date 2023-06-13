import queue   #important >>>> Please dont save the filename as queue.py (for this problem i wasted so much time)

myqueue = queue.Queue(maxsize=3) #initilizing the queue

myqueue.put("Eswar")
myqueue.put("Rao")

print(myqueue.qsize()) #size is 2

print(myqueue.get()) #Taken one from queue

print(myqueue.qsize()) #size is 1

myqueue.put("Lastone")

print("queue full boy", myqueue.full())

myqueue.put("from this queue will be full")

print("queue full boy", myqueue.full())

print("queue empty",myqueue.empty()) #gives false because it hase some content