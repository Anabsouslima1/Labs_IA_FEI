import numpy as np

def triangular(x, a, b, c):
    if a == b:
        if x <= b:
            return 1.0
        elif x >= c:
            return 0.0
        else:
            return (c - x) / (c - b)
    if b == c:
        if x >= b:
            return 1.0
        elif x <= a:
            return 0.0
        else:
            return (x - a) / (b - a)
    if x <= a or x >= c:
        return 0.0
    elif x == b:
        return 1.0
    elif x < b:
        return (x - a) / (b - a)
    else:
        return (c - x) / (c - b)

# Distância
def distancia_curta(x):
    return triangular(x, 0, 0, 40)

def distancia_media(x):
    return triangular(x, 20, 50, 80)

def distancia_longa(x):
    return triangular(x, 60, 100, 100)

# Velocidade
def velocidade_lenta(x):
    return triangular(x, 0, 0, 40)

def velocidade_moderada(x):
    return triangular(x, 20, 50, 80)

def velocidade_rapida(x):
    return triangular(x, 60, 100, 100)

# Pressão
def pressao_suave(x):
    return triangular(x, 0, 0, 40)

def pressao_media(x):
    return triangular(x, 20, 50, 80)

def pressao_forte(x):
    return triangular(x, 60, 100, 100)

def inferencia(distancia, velocidade):
    dc = distancia_curta(distancia)
    dm = distancia_media(distancia)
    dl = distancia_longa(distancia)
    vl = velocidade_lenta(velocidade)
    vm = velocidade_moderada(velocidade)
    vr = velocidade_rapida(velocidade)

    # Regras
    r1 = min(dc, vl)
    r2 = min(dc, vm)
    r3 = min(dc, vr)
    r4 = min(dm, vl)
    r5 = min(dm, vm)
    r6 = min(dm, vr)
    r7 = min(dl, vl)
    r8 = min(dl, vm)
    r9 = min(dl, vr)
  
    # Agregação
    suave = max(r4, r7, r8)
    media = max(r1, r5, r9)
    forte = max(r2, r3, r6)
  
    return suave, media, forte

def calcular_pressao(distancia, velocidade):
    suave, media, forte = inferencia(distancia, velocidade)
    valores = np.linspace(0, 100, 1001)

    saida_suave = np.array([
        min(suave, pressao_suave(x))
        for x in valores
    ])

    saida_media = np.array([
        min(media, pressao_media(x))
        for x in valores
    ])

    saida_forte = np.array([
        min(forte, pressao_forte(x))
        for x in valores
    ])

    agregada = np.maximum(
        saida_suave,
        np.maximum(saida_media, saida_forte)
    )

    if np.sum(agregada) == 0:
        return 0

    return np.sum(valores * agregada) / np.sum(agregada)

# Entrada do usuário
distancia = float(input("Digite a distância do obstáculo (m): "))
velocidade = float(input("Digite a velocidade atual (km/h): "))

pressao = calcular_pressao(distancia, velocidade)

print(f"Pressão no freio: {pressao:.2f}%")
