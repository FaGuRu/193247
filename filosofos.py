import time
import random
import threading
from threading import Thread, Lock

total_filosofos = 3
turnos = 1
contador = 1
parar = False

class filosofo(threading.Thread):
    exlusion = threading.Lock()
    tenedores = [] #Array para el turno de tenedores
    situacion = [] #Array para conocer la situación de cada filosofo
    count=0 #Cuenta los filosofos que entran

    def __init__(self):
        super().__init__() 
        self.id=filosofo.count
        filosofo.count+=1 #agrega un filosofo
        filosofo.situacion.append('Entrando')
        filosofo.tenedores.append(threading.Semaphore(0)) #agrega un semaforo al tenedor
        print("filosofo {0} - Entrando a la cena".format(self.id))
        
                                        # >>>>>>Simulación del tenedor<<<<<<        
    def tenedor_derecho(self,i):
        return (i-1)%total_filosofos

    def tenedor_izquierdo(self,i):
        return(i+1)%total_filosofos

    def comprobar_situacion(self,i):
        if filosofo.situacion[i] == 'con hambre' and filosofo.situacion[self.tenedor_izquierdo(i)] != 'comiendo' and filosofo.situacion[self.tenedor_derecho(i)] != 'comiendo':
            filosofo.situacion[i]='comiendo'
            filosofo.tenedores[i].release() #Si estan libres los tenedores cambia su situación a comer
            

                                        # >>>>>>Simulación de comida, aquí es donde se usa la exclusión mutua<<<<<<
                                        
    def tomar_tenedor(self):
        filosofo.exlusion.acquire()
        filosofo.situacion[self.id] = 'con hambre'
        self.comprobar_situacion(self.id) #verifica si puede tomarlos
        filosofo.exlusion.release()
        filosofo.tenedores[self.id].acquire() #Solo si podia tomarlos cambia a comer
        
    def soltar_tenedor(self):
        filosofo.exlusion.acquire()
        filosofo.situacion[self.id] = 'Analizando'
        self.comprobar_situacion(self.tenedor_izquierdo(self.id))
        self.comprobar_situacion(self.tenedor_derecho(self.id))
        filosofo.exlusion.release()

    def situacion_comer(self):
        global contador
        global parar
        print("filosofo {} esta comiendo".format(self.id))
        time.sleep(2) #Tiempo que le lleva comar
        print("filosofo {} ya termino de comer".format(self.id))
        contador = contador + 1
        #print("Este es el contador -->",contador)
        if contador >= total_filosofos:
            #print("Hola, entre")
            parar = True
            #print("Parar es --> ",parar)

                                            # >>>>>>Aquí corremos la simulación<<<<<< 
      
    def run(self):
        global parar
        for i in range(turnos):
            self.tomar_tenedor()
            self.situacion_comer()
            self.soltar_tenedor()
            #print("Parar aquí es --> ",parar)
            if parar == True:
                #print("Hola, entre 2")
                break
            
def main():
    list_filosofo=[]
    for i in range(total_filosofos):
        list_filosofo.append(filosofo())
    for t in list_filosofo:
            t.start()
    for t in list_filosofo:
        t.join()

if __name__=="__main__":
    main()