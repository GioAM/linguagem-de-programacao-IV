import time
import random
import threading

N = int(input())
state = []
mutexs = []
filosofos = []

def filosofo_start(i):
    print("Filosofo %d sentou se a mesa"%(i))
    while (1):
        think(i)
        if(take_fork(i)):
            eat(i)
            put_fork(i)

def think(i):
    print("Filosofo %d está pensando" % (i))
    time.sleep(random.randint(1,5))
    state[i] = "HUNGRY"

def take_fork(i):
    print(mutexs)
    if(mutexs[left(i)].locked() and mutexs[right(i)].locked()):
        return False
    else:
        print("Filosofo %d left: %d right: %d" % (i, left(i), right(i)))
        print("Filosofo %d pegou os garfos" % (i))
        mutexs[left(i)].acquire()
        mutexs[right(i)].acquire()
        return True



def eat(i):
    print("Filosofo %d está comendo" % (i))
    state[i] = "EATING"
    time.sleep(random.randint(1,5))

def put_fork(i):
    print("Filosofo %d soltou os garfos" % (i))
    state[i] = "THINKING"
    mutexs[left(i)].release()
    mutexs[right(i)].release()

def test(i):
    if(state[i] == "HUNGRY" and state[left(i)] != "EATING"  and state[right(i)] != "EATING"):
        return True
    return False

def right(i):
    return (i + N) % N

def left(i):
    return (i + N - 1) % N

for i in range(N):
    nome = "Filosofo" + str(i)
    mutex = threading.Lock()
    filosofo = threading.Thread(target=filosofo_start, name=nome, args=[i])
    filosofos.append(filosofo)
    mutexs.append(mutex)
    state.append("SIT")

for filosofo_top in filosofos:
    filosofo_top.start()