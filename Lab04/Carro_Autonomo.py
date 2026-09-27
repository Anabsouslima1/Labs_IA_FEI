pip install scikit-fuzzy
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

distancia = ctrl.Antecedent(np.arange(0, 101, 1), 'distancia')
velocidade = ctrl.Antecedent(np.arange(0, 101, 1), 'velocidade')
pressao = ctrl.Consequent(np.arange(0, 101, 1), 'pressao')

# =========================
# FUNÇÕES DE PERTINÊNCIA
# =========================

# Distância
distancia['curta'] = fuzz.trimf(distancia.universe, [0, 0, 40])
distancia['media'] = fuzz.trimf(distancia.universe, [20, 50, 80])
distancia['longa'] = fuzz.trimf(distancia.universe, [60, 100, 100])

# Velocidade
velocidade['lenta'] = fuzz.trimf(velocidade.universe, [0, 0, 40])
velocidade['moderada'] = fuzz.trimf(velocidade.universe, [20, 50, 80])
velocidade['rapida'] = fuzz.trimf(velocidade.universe, [60, 100, 100])

# Pressão
pressao['suave'] = fuzz.trimf(pressao.universe, [0, 0, 40])
pressao['media'] = fuzz.trimf(pressao.universe, [20, 50, 80])
pressao['forte'] = fuzz.trimf(pressao.universe, [60, 100, 100])

# =========================
# REGRAS DE INFERÊNCIA
# =========================

regra1 = ctrl.Rule(
    distancia['curta'] & velocidade['lenta'],
    pressao['media']
)

regra2 = ctrl.Rule(
    distancia['curta'] & velocidade['moderada'],
    pressao['forte']
)

regra3 = ctrl.Rule(
    distancia['curta'] & velocidade['rapida'],
    pressao['forte']
)

regra4 = ctrl.Rule(
    distancia['media'] & velocidade['lenta'],
    pressao['suave']
)

regra5 = ctrl.Rule(
    distancia['media'] & velocidade['moderada'],
    pressao['media']
)

regra6 = ctrl.Rule(
    distancia['media'] & velocidade['rapida'],
    pressao['forte']
)

regra7 = ctrl.Rule(
    distancia['longa'] & velocidade['lenta'],
    pressao['suave']
)

regra8 = ctrl.Rule(
    distancia['longa'] & velocidade['moderada'],
    pressao['suave']
)

regra9 = ctrl.Rule(
    distancia['longa'] & velocidade['rapida'],
    pressao['media']
)

# =========================
# SISTEMA FUZZY
# =========================

sistema_controle = ctrl.ControlSystem([
    regra1,
    regra2,
    regra3,
    regra4,
    regra5,
    regra6,
    regra7,
    regra8,
    regra9
])

simulador = ctrl.ControlSystemSimulation(sistema_controle)

# =========================
# ENTRADA DO USUÁRIO
# =========================

distancia_entrada = float(
    input("Digite a distância do obstáculo (m): ")
)

velocidade_entrada = float(
    input("Digite a velocidade atual (km/h): ")
)

# =========================
# VALIDAÇÃO DAS ENTRADAS
# =========================

if not 0 <= distancia_entrada <= 100:
    print("A distância deve estar entre 0 e 100 metros.")
    exit()

if not 0 <= velocidade_entrada <= 100:
    print("A velocidade deve estar entre 0 e 100 km/h.")
    exit()

# =========================
# INFERÊNCIA FUZZY
# =========================

simulador.input['distancia'] = distancia_entrada
simulador.input['velocidade'] = velocidade_entrada

simulador.compute()

# =========================
# RESULTADO
# =========================

resultado = simulador.output['pressao']

print(f"Pressão no freio: {resultado:.2f}%")

