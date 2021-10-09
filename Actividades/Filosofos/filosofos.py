import time
import random
import threading
from threading import Thread, Lock

total_filosofos = 5
turnos = 1
contador = 1
parar = False

class filosofo(threading.Thread):
    exlusion = threading.Lock()
    situacion = [] #Array para conocer la situación de cada filosofo
    tenedores = [] #Array para el turno de tenedores
    count=0 #Cuenta los filosofos que entran

    def __init__(self):
        super().__init__() 
        self.id=filosofo.count
        filosofo.count+=1 #agrega un filosofo
        filosofo.situacion.append('Entrando')
        filosofo.tenedores.append(threading.Semaphore(0)) #agrega un semaforo al tenedor
        print("filosofo {0} - Entrando a la cena".format(self.id))
