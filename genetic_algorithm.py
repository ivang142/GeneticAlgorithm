## Algoritmo genético en Python para encontrar 
# la cadena de texto "Hello, World!"

import random

# Configuración del algoritmo genético
OBJETIVO = "Hello, World!"  # La cadena que queremos encontrar
TAM_POBLACION = 100  # Número de individuos en cada generación
TASA_MUTACION = 0.10  # Probabilidad de mutación
GENERACIONES = 1000  # Número máximo de generaciones

# Función para generar una cadena aleatoria del mismo tamaño que el objetivo
def generar_individuo():
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz, !"
    return "".join(random.choice(caracteres) for _ in range(len(OBJETIVO)))

# Función de aptitud (fitness): cuántos caracteres coinciden con el objetivo
def calcular_aptitud(individuo):
    return sum(1 for i, c in enumerate(individuo) if c == OBJETIVO[i])

# Función de cruce entre dos individuos (punto de corte aleatorio)
def cruzar(padre, madre):
    punto = random.randint(0, len(OBJETIVO) - 1)
    hijo = padre[:punto] + madre[punto:]
    return hijo

# Función de mutación: cambia un carácter al azar con una pequeña probabilidad
def mutar(individuo):
    if random.random() < TASA_MUTACION:
        index = random.randint(0, len(OBJETIVO) - 1)
        caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz, !"
        individuo = individuo[:index] + random.choice(caracteres) + individuo[index + 1:]
    return individuo

# Algoritmo genético
poblacion = [generar_individuo() for _ in range(TAM_POBLACION)] 

for generacion in range(GENERACIONES):
    # Evaluar aptitud
    poblacion = sorted(poblacion, key=calcular_aptitud, reverse=True)
    
    # Mejor individuo
    mejor = poblacion[0]
    print(f"Generación {generacion}: {mejor} (Aptitud: {calcular_aptitud(mejor)})")
    
    if mejor == OBJETIVO:
        print("¡Solución encontrada!")
        break

    # Selección (los mejores sobreviven)
    nueva_poblacion = poblacion[:10]  # Conservamos los mejores 10

    # Reproducción (cruce y mutación)
    while len(nueva_poblacion) < TAM_POBLACION:
        padre, madre = random.choices(poblacion[:50], k=2)  # Selección de los mejores
        hijo = cruzar(padre, madre)
        hijo = mutar(hijo)
        nueva_poblacion.append(hijo)

    poblacion = nueva_poblacion
