import time
import random
import threading
import queue

queue = queue.Queue(maxsize=4)

def productor():
    while True:
        if not queue.full():
            item = random.randint(1,4) #De 1 a 4 porque es 4 el maxsize
            queue.put(item)
            print("Elemento interno de la cola creada", item)
            
            time_sleep = random.randint(1,5)
            time.sleep(time_sleep)
            
def consumidor():
    while True:
        if not queue.empty():
            item = queue.get()
            queue.task_done()
            print("Consumo realizado", item)
            
            time_sleep = random.randint(1,5)
            time.sleep(time_sleep)
            
if __name__ == "__main__":
    productor_hilo = threading.Thread(target=productor)
    consumidor_hilo = threading.Thread(target=consumidor)
    
    productor_hilo.start()
    consumidor_hilo.start()
