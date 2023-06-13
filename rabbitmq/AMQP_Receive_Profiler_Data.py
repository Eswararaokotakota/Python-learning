import pika
import time
import csv
import os
from datetime import datetime
from PyQt5 import *
from PyQt5.QtCore import *
import ast
##import ast
##This Script is similar to AssetPC AMQP Receive Process
##This script gets data from Profiler PC and sends signal back to Profiler Window
class Receiver_msg(object):
##    signal_to_update_profiler_info=QtCore.pyqtSignal(dict)
    def __init__(self,address,send_info_queue,stop_profiler_receive_process):
        try:
            ##address ------>PC3 Ip Address
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=address,heartbeat=0))
            print(address)
            self.channel = self.connection.channel()
            ##dashboard_Profiler_data_receive_queue is used for communication between profiler PC and Dashboard PC
            self.ext_q = "dashboard_Profiler_data_receive_queue"
            self.channel.queue_declare(queue=self.ext_q)
            self.send_info_queue=send_info_queue
            self.stop_profiler_receive_process=stop_profiler_receive_process
            self.counter=0
            self.channel.queue_purge(queue=self.ext_q)
            self.channel.queue_declare(queue=self.ext_q)
            self.channel.basic_consume(queue=self.ext_q, on_message_callback=self.callback, auto_ack=True,)
            self.t=time.time()
            print("Waiting for messages. To exit press Ctrl+C, iterations")
            self.channel.start_consuming()
        except Exception as e:
            try:
                self.channel.stop_consuming()
                self.connection.close()
            except:
                print("Connection not established")
        
    def callback(self,ch, method, properties, body):
        ##This Block is executed when Profiler PC sends signal back to Dashboard PC
        try:
            rx_msg = body.decode("utf-8")
            if not self.stop_profiler_receive_process.empty():
                stop_msg=self.stop_profiler_receive_process.get()
                print("Stop#####")
                raise Exception("Receiving Closed")
##            print("signal Received")
                
            #data_from_profiler=ast.literal_eval(rx_msg)
            #print("Chainage in AMQP Receive :",data_from_profiler['Chainge_or_Counter'],"IRI :",data_from_profiler['IRI_value'])
            if self.send_info_queue.empty():
                self.send_info_queue.put([rx_msg])
            
            
##            self.signal_to_update_profiler_info.emit(rx_msg)
            #self.internal_q.put((rx_msg))
            
        except:
            try:
                self.channel.stop_consuming()
                self.connection.close()
            except:
                print("Connection not established")
