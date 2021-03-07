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
                
        if value < -20:
            value = -20
            
        elif value > 20:
            value = 20
        
        # print("valor em decimal desse chromossome é de: ", value)
        aptidao = cos(value)*value + 2
        # print("a aptidão é de: ", aptidao)
        
        return aptidao