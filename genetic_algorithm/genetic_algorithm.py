
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
    # populacao_inicial.sort(key=lambda individuo: (individuo.alocacao, individuo.quantidade_slots_ocupados))
    
    # for item in populacao_inicial:
    #     print('{0} {1} {2}'.format(item.cromossomos, item.quantidade_slots_ocupados, item.alocacao))

    # melhor_solucao = populacao_inicial[0]
    # print("MELHOR SOLUÇÃO INICIAL!")
    # print('{0} {1} {2}'.format(melhor_solucao.quantidade_slots_ocupados, melhor_solucao.alocacao, melhor_solucao.cromossomos))

    # geracao = 0
    # while geracao < 30:
    #     descendentes = []
    #     # k = 0.75
    #     while len(descendentes) < len(populacao_inicial):
    #         individuo1 =  populacao_inicial[randint(0,len(populacao_inicial)- 1)]
    #         individuo2 =  populacao_inicial[randint(0,len(populacao_inicial)- 1)]

    #         pai1 = seleciona_pai(individuo1, individuo2)

    #         individuo1 =  populacao_inicial[randint(0,len(populacao_inicial)- 1)]
    #         individuo2 =  populacao_inicial[randint(0,len(populacao_inicial)- 1)]

    #         pai2 = seleciona_pai(individuo1, individuo2)

    #         #lista vai ta ordenada, posso só pegar os indices

    #         corte = randint(0,7)

    #         cromossomo_filho1 = pai1.cromossomos[0:corte] + pai2.cromossomos[corte:] 
    #         alocacao = alocacoes(demandas,cromossomo_filho1,dic_rotas_link,links)
    #         slots_filho1 = fitness_link_mais_carregado(links)
    #         reseta_rede(links)

    #         filho1 = Individuo(cromossomo_filho1,slots_filho1,alocacao[0])
    #         descendentes.append(filho1)
            
    #         cromossomo_filho2 = pai2.cromossomos[0:corte] + pai1.cromossomos[corte:]
    #         alocacao = alocacoes(demandas,cromossomo_filho2,dic_rotas_link,links)
    #         slots_filho2= fitness_link_mais_carregado(links)
    #         reseta_rede(links)
            
    #         filho2 = Individuo(cromossomo_filho2,slots_filho2, alocacao[0])
    #         descendentes.append(filho2)

    #     fator_mutacao = randint(0,100)
    #     # print("MEU FATOR DE MUTAÇÃO É DE: ", fator_mutacao)
    #     if fator_mutacao <= 2:
    #         mutacao = randint(0,len(descendentes)-1)
    #         mutacao2 = randint(0,7)
    #         mutacao3 = randint(0,7)
    #         # print("INDICE DO INDIVIDUO MUTADO: ", mutacao)
    #         # print("PARTE 1 DO INDIVIDUO A SER MUTADO: ", mutacao2)
    #         # print("PARTE 2 DO INDIVIDUO A SER MUTADO: ", mutacao3)

    #         mutacao4 = randint(0,3)
    #         while mutacao4 ==  descendentes[mutacao].cromossomos[mutacao2][mutacao3]: 
    #             mutacao4 = randint(0,3)      
            
    #         # print("ROTA ANTES: ", descendentes[mutacao].cromossomos[mutacao2][mutacao3])
    #         # print("ROTA DEPOIS: ", mutacao4)
    #         descendentes[mutacao].cromossomos[mutacao2][mutacao3] = mutacao4


    #     descendentes.sort(key=lambda individuo: (individuo.alocacao, individuo.quantidade_slots_ocupados))
        

    #     # print('{0} {1} {2}'.format(descendentes[0].quantidade_slots_ocupados, descendentes[0].alocacao, descendentes[0].cromossomos))#       FALTA FAZER A MUTAÇÃO!


    #     if descendentes[0].alocacao == 1 and descendentes[0].quantidade_slots_ocupados < melhor_solucao.quantidade_slots_ocupados:
    #         melhor_solucao = descendentes[0]
        
    #     populacao_inicial = descendentes
        
    #     print(geracao)
    #     geracao += 1

    # fim = time.time()
    # print("Tempo de execução: ", fim - inicio)
    # print("MELHOR SOL APOS GA")
    # print('{0} {1} {2}'.format(melhor_solucao.quantidade_slots_ocupados, melhor_solucao.alocacao, melhor_solucao.cromossomos))
    