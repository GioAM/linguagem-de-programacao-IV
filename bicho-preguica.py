from threading import Thread
import time
import random

altura_maxima = 1000
numero_de_preguicas = 10
time.sleep(3)
bichos_preguicas = []
rodando = True
contador = 0

def sortHeight(elem):
    return elem.altura

class preguica(Thread):
    def __init__(self, nome):
        print(f"{nome} começando")
        Thread.__init__(self)
        self.nome = nome
        self.tentativas = 0
        self.altura = 0
    def run(self):
        global rodando
        global contador
        while rodando:
            altura_random = random.randint(0, 101)
            self.altura += altura_random
            self.tentativas += 1
            print(f"O {self.nome} subiu {altura_random}cm e já alcançou a altura de {self.altura}cm")
            if self.altura >= altura_maxima:
                rodando = False
            time.sleep(random.randint(3, 7))
        contador += 1


def ranking():
    bichos_preguicas.sort(key=sortHeight, reverse=True)
    index = 1
    for bicho in bichos_preguicas:
        print(f"{bicho.nome} foi x {index}° colocadx com {bicho.tentativas} tentativas. Altura: {bicho.altura/100}m")
        index += 1


for i in range(0, numero_de_preguicas):
    nome = "BICHO_PREGUICA_" + str(i)
    bch_prg = preguica(nome)
    bichos_preguicas.append(bch_prg)


for bichos_preguica in bichos_preguicas:
    bichos_preguica.start()

while contador != numero_de_preguicas:
    pass

ranking()
