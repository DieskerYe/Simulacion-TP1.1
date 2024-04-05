import random
import sys
import numpy
import statistics
import matplotlib.pyplot as plt

if len(sys.argv) != 7 or sys.argv[1] != "-n" or sys.argv[3] != "-c" or sys.argv[5] != "-e":
    print("Uso: python script.py -n <cantidad_tiradas> -c <corridas> -e <número_elegido>")
    sys.exit(1)

cant_corridas = int(sys.argv[4])
num_elegido = int(sys.argv[6])
media_esperada = 18
frecuencia_esperada = 1 / 37
varianza_esperada = 114
desvio_esperado = 10.677
frecuencia_absoluta = 0
num_corrida = []
frecuencias_relativas = []
promedios = []
varianzas = []
desvios = []
resultados_totales = []  # Lista para almacenar todos los resultados de todas las corridas

for i in range(cant_corridas):
    #Generación de valores aleatorios enteros
    cant_tiradas = int(sys.argv[2])
    resultados = [random.randint(0, 36) for _ in range(cant_tiradas)]
    resultados_totales.extend(resultados)  
    # Calculo de funciones estadísticas
    promedios.append(statistics.fmean(resultados_totales))
    varianzas.append(numpy.var(resultados_totales))
    desvios.append(numpy.std(resultados_totales))
    frecuencia_absoluta += resultados.count(num_elegido)
    frecuencia_relativa_acumulada = frecuencia_absoluta / ((i + 1) * cant_tiradas)
    frecuencias_relativas.append(frecuencia_relativa_acumulada)
    num_corrida.append(i)

# Crear la figura y los subgráficos
fig, axs = plt.subplots(1, 4, figsize=(20, 6))

# Graficar en el primer subgráfico (Media)
axs[0].plot(num_corrida, promedios, color='red', label='Media Calculada')
axs[0].axhline(y=media_esperada, color='blue', label='Valor Esperado')
axs[0].set_title('Gráfico 1: Media')
axs[0].set_xlabel('Número de corridas')
axs[0].set_ylabel('Media')

# Graficar en el segundo subgráfico (Varianza)
axs[1].plot(num_corrida, varianzas, color='red', label='Varianza Calculada')
axs[1].axhline(y=varianza_esperada, color='blue', label='Valor Esperado')
axs[1].set_title('Gráfico 2: Varianza')
axs[1].set_xlabel('Número de corridas')
axs[1].set_ylabel('Varianza')

# Graficar en el tercer subgráfico (Desvío estándar)
axs[2].plot(num_corrida, desvios, color='red', label='Desvío Calculado')
axs[2].axhline(y=desvio_esperado, color='blue', label='Valor Esperado')
axs[2].set_title('Gráfico 3: Desvío estándar')
axs[2].set_xlabel('Número de corridas')
axs[2].set_ylabel('Desvío')

# Graficar en el cuarto subgráfico (Frecuencia relativa acumulada)
axs[3].plot(num_corrida, frecuencias_relativas, color='red', label='Frecuencia relativa acumulada')
axs[3].axhline(y=frecuencia_esperada, color='blue', label='Valor Esperado')
axs[3].set_title('Gráfico 4: Frecuencia relativa')
axs[3].set_xlabel('Número de corridas')
axs[3].set_ylabel('Frecuencia relativa')

plt.tight_layout()
plt.savefig('graficas_valores_aleatorios.png')
plt.show()