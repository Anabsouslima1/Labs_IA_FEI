!pip3 install pyeasyga
from pyeasyga import pyeasyga
import matplotlib.pyplot as plt
import random
import copy
import numpy as np

# Dados
data = [
    {'name': 'green',  'value': 4,  'weight': 12},
    {'name': 'gray',   'value': 2,  'weight': 1},
    {'name': 'yellow', 'value': 10, 'weight': 4},
    {'name': 'orange', 'value': 1,  'weight': 1},
    {'name': 'blue',   'value': 2,  'weight': 2}
]

tamanho_populacao = 20
geracoes = 50

ga = pyeasyga.GeneticAlgorithm(
    data,
    population_size=tamanho_populacao,
    generations=geracoes,
    crossover_probability=0.9,
    mutation_probability=0.3,
    elitism=True,
    maximise_fitness=True
)

def my_create_individual(data):

    while True:

        individual = [
            random.randint(0, 15),
            random.randint(0, 15),
            random.randint(0, 15),
            random.randint(0, 15),
            random.randint(0, 15)
        ]

        peso = 0

        for quantidade, caixa in zip(individual, data):
            peso += quantidade * caixa['weight']

        if peso <= 15:
            return individual


ga.create_individual = my_create_individual

def aptidao(individual, data):

    values = 0
    weights = 0

    for quantidade, caixa in zip(individual, data):
        values += quantidade * caixa['value']
        weights += quantidade * caixa['weight']

    if weights > 15:
        return -(weights - 15)

    return values


ga.fitness_function = aptidao

def crossover(parent_1, parent_2):
    crossover_index = random.randrange(1, len(parent_1))

    child_1 = (
        parent_1[:crossover_index]
        + parent_2[crossover_index:]
    )

    child_2 = (
        parent_2[:crossover_index]
        + parent_1[crossover_index:]
    )

    return child_1, child_2


ga.crossover_function = crossover

def my_mutation(individual):
    index = random.randrange(len(individual))

    if random.random() < 0.5:
        individual[index] += 1
    else:
        individual[index] -= 1

    if individual[index] < 0:
        individual[index] = 0

    if individual[index] > 15:
        individual[index] = 15

ga.mutate_function = my_mutation

def my_selection(population):
    tamanho_torneio = 3

    participantes = random.sample(population, tamanho_torneio)

    vencedor = max(participantes, key=lambda x: x.fitness)

    return vencedor


ga.selection_function = my_selection
ga.run()

print("Melhor solução:")
print(ga.best_individual())
