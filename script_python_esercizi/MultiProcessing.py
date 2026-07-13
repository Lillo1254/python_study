import time
from multiprocessing import Process

def elabora_dati(id_blocco):
    print(f"[CPU] Processo {id_blocco} avviato su core dedicato...")
    somma = sum(x * x for x in range(1000000000))
    print(f"[CPU] Processo {id_blocco} terminato. somma: {somma}")
    

if __name__ == '__main__': 
    print("[MAIN] Avvio del programma...")
    print("[MAIN] Avvio dei processi...")
    
    p1 = Process(target=elabora_dati, args=(1,))
    p2 = Process(target=elabora_dati, args=(2,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print("[MAIN] Programma terminato")