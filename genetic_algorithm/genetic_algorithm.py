
from auxiliary_functions import *
from individuo import Individuo
from random import randint
import random
import time

class Genetic_Algorithm:

    def __init__(self, generations, population_size,crossover_rate, mutation_rate,chromosome_size):
        self.generations = generations
        self.population_size = population_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.chromosome_size = chromosome_size 
    
    def create_initial_population(self, population_size,chromosome_size):
        population = []
        for i in range(population_size):
            individuo = Individuo([],None)
            for j in range(chromosome_size):
                individuo.chromosomes.append(random.randint(0,1))
            population.append(individuo)

        return population
    
    def best_of_generation(population):
        pop_copy = population.copy()
        pop_copy.sort(key=lambda individuo: (individuo.aptidao))
        return pop_copy[0]

    def select_parent(population):
        igual = True
        while igual:
            selected = []
            for i in range(4):
                selected.append(randint(0,len(population)-1))
                        
            if population[selected[0]].aptidao < population[selected[1]].aptidao:
                pos_winner = selected[0]
            else:
                pos_winner = selected[1]      
            
            if population[selected[2]].aptidao < population[selected[3]].aptidao:
                pos_winner1 = selected[0]
            else:
                pos_winner1 = selected[1]       
            
            if pos_winner != pos_winner1:
                igual = False
                return population[pos_winner], population[pos_winner1]
            
    def elitism(population):
        best = []
        pop_copy = population.copy()
        pop_copy.sort(key=lambda individuo: (individuo.aptidao))
        
        for i in range(3):
            best.append(pop_copy[i])
        
        return best
    
    def crossover(father1, father2):
        # revisar o tipo de crossover utlizado
        point = randint(0,len(father1)-1)
        son1 = Individuo([],0)
        son2 = Individuo([],0)       
        
        son1.chromossome = father1.chromosome[:point] + father2.chromosome[point:]
        son1.aptidao = Individuo.calc_aptidao(son1)     
        
        son2.chromossome = father2.chromosome[point:] + father1.chromosome[:point]
        son2.aptidao = Individuo.calc_aptidao(son2)     

        return son1,son2
    
    def mutation(individuo):
        pos_mutation = randint(0,len(individuo.chromosome)-1)
        if individuo.chromosome[pos_mutation] == 1:
            individuo.chromosome[pos_mutation] = 0
        else:
            individuo.chromosome[pos_mutation] = 1
        
        return individuo
 
