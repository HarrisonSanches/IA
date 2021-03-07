import time
from genetic_algorithm import *
from individuo import *
import random

def main():

    # inicio = time.time()
    ga = Genetic_Algorithm(10,10,0.6,0.01,16)
    population = ga.create_initial_population(ga.population_size, ga.chromosome_size)
    
    for i in range(len(population)):
        population[i].aptidao = Individuo.calc_aptidao(population[i])

    # print(population[0].aptidao)
    # population.sort(key=lambda individuo: (individuo.aptidao))
    # b = population.copy()
    
    generation_count = 0
    list_best_of_generations = []
    the_best = Genetic_Algorithm.best_of_generation(population)
    # print(the_best.aptidao)
    
    list_best_of_generations.append(the_best)

    while generation_count < ga.generations:
        descendants = Genetic_Algorithm.elitism(population)
        # print("no inicio, a quantidade de descendentes era de:", len(descendants))
        # for i in range(len(descendants)):
            # print(descendants[i].aptidao)
        # print()
        while len(descendants) < len(population):
            father, father2 = Genetic_Algorithm.select_parent(population)
            prob_crossover = random.random()
            print("prob_crossover", prob_crossover)
            if prob_crossover <= ga.crossover_rate:
                # print("crossover? sim")
                son1, son2 = Genetic_Algorithm.crossover(father,father2)
                prob_mutation = random.random()
                if prob_mutation <= ga.mutation_rate:
                    print("prob_mutation", prob_mutation)
                    son1 = Genetic_Algorithm.mutation(son1)
                    son2 = Genetic_Algorithm.mutation(son2)
            else:
                son1 = father
                son2 = father2
                prob_mutation = random.random()
                if prob_mutation <= ga.mutation_rate:
                    print("prob_mutation", prob_mutation)
                    son1 = Genetic_Algorithm.mutation(son1)
                    son2 = Genetic_Algorithm.mutation(son2)
            
                
            descendants.append(son1)
            descendants.append(son2)
            # print(len(descendants))
            
        the_best = Genetic_Algorithm.best_of_generation(descendants)
        print("o melhor da geração é: ", the_best.aptidao)
        list_best_of_generations.append(the_best)
        population = descendants
                
        # adicionar os melhores de cada geração no best o generations
        # best_of_generations
        generation_count += 1
        # print(generation_count)
    
    # list_best_of_generations.sort()
    
    for i in range(len(list_best_of_generations)):
        print(list_best_of_generations[i].aptidao) 
        # b = list_best_of_generations[i].chromosomes
        # value = 0
        # n = 15
        # for i in range(16):
        #     value =  value + (2**n * b[i])
        #     n = n-1
        
                
        # if value < -20:
        #     value = -20
            
        # elif value > 20:
        #     value = 20
        
        # print(value)

    
    return 0

if __name__ == '__main__':
    main()