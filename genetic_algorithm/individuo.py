from math import *

class Individuo:
    def __init__(self, chromosomes,aptidao):
        self.chromosomes = chromosomes
        self.aptidao = aptidao
    
    
    # DA UMA REVISADA NESSA PARTE 
    def calc_aptidao(individuo):
        value = 0
        elements = individuo.chromosomes.copy()
        # print(individuo.chromosomes)
        # for i in range(len(individuo.chromosomes)):
        #     digit = str(elements.pop())
        #     if digit == '1':
        #         value = value + pow(2, i)
        
        value = 0
        n = 15
        for i in range(16):
            value =  value + (2**n * elements[i])
            n = n-1
        
        x = -20 + ((40*value) / (2**16 - 1))
        
        if x < -20:
            x = -20
            
        elif x > 20:
            x = 20
        
        # print("valor em decimal desse chromossome é de: ", value)
        aptidao = cos(x)*x + 2
        # print("a aptidão é de: ", aptidao)
        
        return aptidao