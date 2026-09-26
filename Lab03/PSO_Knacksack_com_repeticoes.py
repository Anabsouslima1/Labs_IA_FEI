!pip install pyswarms

import pyswarms as ps
import numpy as np

data = [
    {'cor': 'verde',   'valor': 4,  'peso': 12},
    {'cor': 'cinza',   'valor': 2,  'peso': 1},
    {'cor': 'amarelo', 'valor': 10, 'peso': 4},
    {'cor': 'laranja', 'valor': 1,  'peso': 1},
    {'cor': 'azul',    'valor': 2,  'peso': 2}
]

CAPACIDADE = 15

max_quantidades = np.array([
    CAPACIDADE // item['peso']
    for item in data
])

def aptidao(enxame, data):

    resultados = []

    for individual in enxame:

        quantidades = np.rint(individual).astype(int)

        quantidades = np.maximum(quantidades, 0)

        peso = sum(
            quantidade * caixa['peso']
            for quantidade, caixa in zip(quantidades, data)
        )

        dinheiro = sum(
            quantidade * caixa['valor']
            for quantidade, caixa in zip(quantidades, data)
        )

        excesso = max(0, peso - CAPACIDADE)

        custo = -dinheiro + 1000 * excesso

        resultados.append(custo)

    return np.array(resultados)


options = {
    'c1': 1.5,
    'c2': 1.5,
    'w': 0.7
}

pso = ps.single.GlobalBestPSO(
    n_particles=20,
    dimensions=len(data),
    options=options,

    bounds=(
        np.zeros(len(data)),
        max_quantidades.astype(float)
    )
)

melhor_custo, melhor_posicao = pso.optimize(
    aptidao,
    iters=50,
    data=data
)

melhor_individuo = np.rint(melhor_posicao).astype(int)

peso = sum(
    quantidade * caixa['peso']
    for quantidade, caixa in zip(melhor_individuo, data)
)

dinheiro = sum(
    quantidade * caixa['valor']
    for quantidade, caixa in zip(melhor_individuo, data)
)

print("Melhor indivíduo:", melhor_individuo)
print("Peso:", peso, "kg")
print("Dinheiro:", dinheiro)
