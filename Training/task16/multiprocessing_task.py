import multiprocessing as mp
import time
import random
import csv

def client_process():
    while True:
        name_input = input("Enter Name: ")
        Phonenumber_input = input("Enter Phone Number: ")
        query_input = input("Enter your query: ")
        name_queue.put(name_input)
        phonenumber_queue.put(Phonenumber_input)
        query_queue.put(query_input)
        print("Sent..!")
        time.sleep(random.randint(1,8))

    
def office(name_queue, phonenumber_queue, query_queue):#Process done...!
    count = 0
    while True:
        if name_queue.qsize() and phonenumber_queue.qsize() and query_queue.qsize()>0:
            print("\n"+"Data Received..!")
            name_data = name_queue.get()
            Phonenumber_data = phonenumber_queue.get()
            query_data = query_queue.get()
            file = open("E:\\Coding\\Python\\Training\\task16\\output_files\\"+name_data+".txt","w")
            #--------------Writing in the txt file-------------#
            file.write("Name: "+name_data)
            file.write("\n"+"Phone number: "+Phonenumber_data)
            file.write("\n"+"Query: "+query_data)
            file.close()
            #--------------Writing in the csv file-------------#
            file_csv = open("E:\\Coding\\Python\\Training\\task16\\output_files\\"+"Client_Queries.csv","a",newline='')
            writer = csv.writer(file_csv)
            if count == 0:
                writer.writerow(["Name","Phone Number","Query"])
            writer.writerow([name_data,Phonenumber_data,query_data])
            count+=1
            file_csv.close()
            # client_process()
            


if __name__ == "__main__":
    name_queue = mp.Queue()
    phonenumber_queue = mp.Queue()
    query_queue = mp.Queue()
    # process1 = mp.Process(target=client_process, args=())
    process2 = mp.Process(target=office, args=(name_queue,phonenumber_queue,query_queue))
    # process1.start()   
    process2.start()
    # process1.join()
    client_process()  
    # process2.join()

   

