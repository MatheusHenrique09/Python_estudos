from random import randint
from time import sleep
def sorteio():
    i=0
    num = randint(1,26)
    while i < 3:
        print("sorteando ...")
        sleep(0.25)
        print("sorteando ..")
        sleep(0.25)
        i+=1
    return print("número sorteado: ",num)