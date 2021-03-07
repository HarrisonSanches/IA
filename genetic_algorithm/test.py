from individuo import Individuo
from math import *
def main():
    
    a = Individuo([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],20)
    
    c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    value = 0
    n = 15
    for i in range(16):
        value =  value + (2**n * c[i])
        n = n-1
    
    print(value)  
    
    
    # print(c.chromosomes)
    # print(cos(c.aptidao)*c.aptidao + 2)
    
    
    # print(a.calc_aptidao(a))
    
    # b = a.chromosomes
    
    # value = 0
    # n = 15
    # for i in range(16):
    #     value =  value + (2**n * c[i])
    #     n = n-1
    
    # print(value)  
    # if value < -20:
    #     value = -20
        
    # elif value > 20:
    #     value = 20
    
    # print(value)

    value = 0
    elements = c.copy()
    for i in range(len(a.chromosomes)):
        print(elements)
        digit = str(elements.pop())
        if digit == '1':
            value = value + pow(2, i)
    print("The decimal value of the number is", value)
   
    print("elemento apos calc = ", c)
    
    print(a.calc_aptidao())
    

    return 0
   
if __name__ == '__main__':
	main()