import threading
import time
import random
import queue
import csv

# name = []
# phonenumber = []
# query = []



class threading_task(): #successfully completed (extra-- writing the data in to the csv file)
    def client():
        while True:
            name_input = input("Enter Name: ")
            Phonenumber_input = input("Enter Phone Number: ")
            query_input = input("Enter your query: ")
            # name.append(name_input)                     #|
            # phonenumber.append(Phonenumber_input)       #|Used fot the storing tha input in the list
            # query.append(query_input)                   #| 
            name_queue.put(name_input)        
            phonenumber_queue.put(Phonenumber_input)
            query_queue.put(query_input)
            print("Sent..!")
            time.sleep(random.randint(1,8))
            # print(len(name),len(phonenumber),len(query))    

    def office():
        count = 0
        while True:
            if name_queue.qsize() and phonenumber_queue.qsize() and query_queue.qsize()>0:
                print("\n"+"Data Received..!")
                name_data = name_queue.get()                   #||
                Phonenumber_data = phonenumber_queue.get()     #||This is because we are using these queues data for multiple times
                query_data = query_queue.get()                 #||

                file = open("E:\\Coding\\Python\\Training\\task15\\task15\\client_quieries\\"+"queue--"+name_data+".txt","w") #creates data in txt file
                # print("file created")
                #--------------Writing in the txt file-------------#
                file.write("Name: "+name_data)
                file.write("\n"+"Phone number: "+Phonenumber_data)
                file.write("\n"+"Query: "+query_data)
                file.close()
                
                #--------------Writing in the csv file-------------#
                file_csv = open("E:\\Coding\\Python\\Training\\task15\\task15\\client_quieries\\Client_Queries.csv","a",newline='') #creates data in csv file
                writer = csv.writer(file_csv)
                
                if count == 0:
                    writer.writerow(["Name","Phone Number","Query"])
                writer.writerow([name_data,Phonenumber_data,query_data])
                count+=1
                # name.clear();  phonenumber.clear();  query.clear()
                file_csv.close()



if __name__ == "__main__":
    print(__name__)
    name_queue = queue.Queue()
    phonenumber_queue = queue.Queue()
    query_queue = queue.Queue()
    thread1 = threading.Thread(target=threading_task.client, args=())
    thread2 = threading.Thread(target=threading_task.office, args=())
    thread1.start()
    thread2.start()

