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

        
        x = -20 + ((40*value) / (2**16 - 1))
        
        aptidao = cos(x)*x + 2
        
        return aptidao