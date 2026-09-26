!pip install pyswarms

import pyswarms as ps
import numpy as np

def aptidao(enxame):
    
    resultados = []
    
    for individual in enxame:
        
        x, y, z = individual
        
        resultado = x**2 + y**2 + z**2
        
        resultados.append(resultado)
    
    return np.array(resultados)

options = {
    'c1': 1.5,
    'c2': 1.5,
    'w': 0.7
}

limites = (
    np.array([-10, -10, -10]),
    np.array([10, 10, 10])
)

pso = ps.single.GlobalBestPSO(
    n_particles=20,
    dimensions=3,
    options=options,
    bounds=limites
)


melhor_custo, melhor_individuo = pso.optimize(
    aptidao,
    iters=50
)

x, y, z = melhor_individuo

resultado = x**2 + y**2 + z**2

print("Melhor indivíduo:", melhor_individuo)
print("f(x,y,z):", resultado)
