!pip install pyeasyga

from pyeasyga import pyeasyga
import random
import numpy as np

tamanho_populacao = 20
geracoes = 50

def criar_individuo(data):
    return [
        random.uniform(-10, 10),
        random.uniform(-10, 10),
        random.uniform(-10, 10)
    ]

def aptidao(individual, data):

    x, y, z = individual

    resultado = x**2 + y**2 + z**2

    return 1 / (1 + resultado)

def selecao(population):

    participantes = random.sample(population, 3)

    vencedor = max(
        participantes,
        key=lambda individuo: individuo.fitness
    )

    return vencedor

def crossover(parent_1, parent_2):

    alpha = random.random()

    child_1 = [
        alpha * parent_1[i] + (1 - alpha) * parent_2[i]
        for i in range(3)
    ]

    child_2 = [
        alpha * parent_2[i] + (1 - alpha) * parent_1[i]
        for i in range(3)
    ]

    return child_1, child_2

def mutacao(individual):

    indice = random.randrange(3)

    individual[indice] += random.gauss(0, 1)

    individual[indice] = max(
        -10,
        min(10, individual[indice])
    )

ga = pyeasyga.GeneticAlgorithm(
    None,
    population_size=tamanho_populacao,
    generations=geracoes,
    crossover_probability=0.9,
    mutation_probability=0.3,
    elitism=True,
    maximise_fitness=True
)

ga.create_individual = criar_individuo
ga.fitness_function = aptidao
ga.selection_function = selecao
ga.crossover_function = crossover
ga.mutate_function = mutacao

ga.run()

melhor_individuo = ga.best_individual()[1]

x, y, z = melhor_individuo

resultado = x**2 + y**2 + z**2

print("Melhor indivíduo:", melhor_individuo)
print("f(x,y,z):", resultado)
