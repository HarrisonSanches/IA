import time
from genetic_algorithm import *
from individuo import *
import random

def main():

    # inicio = time.time()
    ga = Genetic_Algorithm(10,100,60,1,16)
    population = ga.create_initial_population(ga.population_size)
    
    for i in range(len(population)):
        population[i].aptidao = Individuo.calc_aptidao(population[i])

    # print(population[0].aptidao)
    # population.sort(key=lambda individuo: (individuo.aptidao))
    # b = population.copy()
    
    generation_count = 0
    list_best_of_generations = []
    the_best = Genetic_Algorithm.best_of_generation(population)
    
    list_best_of_generations.append(the_best)
    while generation_count < ga.generations:
        descendants = Genetic_Algorithm.elitism(population)
        while len(descendants) < len(population):
            father, father2 = Genetic_Algorithm.select_parent(population)
            prob_crossover = random.random()
            if prob_crossover < ga.crossover_rate:
                son1, son2 = Genetic_Algorithm.crossover(father,father2)
            else:
                son1 = father
                son2 = father2
            
            prob_mutation = random.random()
            if prob_mutation < ga.mutation_rate:
                son1 = Genetic_Algorithm.mutation(son1)
                son2 = Genetic_Algorithm.mutation(son2)
            
            descendants.append(son1)
            descendants.append(son2)
            
        the_best = Genetic_Algorithm.best_of_generation(population)
        list_best_of_generations.append(the_best)
        population = descendants
                
        # adicionar os melhores de cada geração no best o generations
        # best_of_generations
        generation_count += 1
    
    return 0

if __name__ == '__main__':
    main()