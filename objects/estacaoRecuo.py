from objects.canal import Canal
import random

class Estacao:
    numeroEstacao = 0
    emEspera: bool
    cooldownTransmitir : int
    naoTransmitiu = 0
    numColisoes = 0

    def __init__(self,numeroEstacao : int):
        self.probabilidadeTransmtir = 100 #Já está em porcentagem, ou seja, 1 corresponde a 1%
        self.numeroEstacao = numeroEstacao
        self.emEspera = True
        self.cooldownTransmitir = 0

    def printEstacao(self):
        print("Numero da estação: "+str(self.numeroEstacao)+"")
        print("Quer efetuar a transmissão: " + str(self.emEspera) + "")
        print("Cooldown: "+str(self.cooldownTransmitir)+"")
        print("Número de colisões: "+str(self.numColisoes)+"")
        print("--------------------------")

    def tentarTransmitir(self,canal : Canal):
        if self.numColisoes == 16:
            self.emEspera = True
            return
        if self.cooldownTransmitir == 0:
            if canal.estadoCanal() == False:
                    self.emEspera = False
        else:
            self.cooldownTransmitir -=1

    def colisao(self):
        self.numColisoes+=1
        self.emEspera = True
        self.cooldownTransmitir = random.randint(0, 2**self.numColisoes -1)
