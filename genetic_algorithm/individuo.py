from math import *

class Individuo:
    def __init__(self, chromosomes,aptidao):
        self.chromosomes = chromosomes
        self.aptidao = aptidao
        
    def calc_aptidao(individuo):
        value = 0
        elements = individuo.chromosomes.copy()
        # print(individuo.chromosomes)
        for i in range(len(individuo.chromosomes)):
            digit = str(elements.pop())
            if digit == '1':
                value = value + pow(2, i)
                
        if value < -20:
            value = -20
            
        if value > 20:
            value = 20
        
        # print("valor em decimal desse chromossome é de: ", value)
        aptidao = cos(value)*value + 2
        # print("a aptidão é de: ", aptidao)
        
        return aptidao