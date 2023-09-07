import matplotlib.pyplot as plt
import numpy as np

ruta_archivo_yml = input("Ingrese la ruta del archivo: ")

def procesar_archivo_yml(ruta_archivo):
    
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
            inicio = contenido.find("data: |")
            
            if inicio == -1:
                
                return []

            contenido = contenido[inicio:]
            lineas = contenido.split('\n')

            resultados = []

            for linea in lineas[1:]:
                if not linea.strip():
                    break
                partes = linea.split()
                if len(partes) >= 2:
                    try:
                        longitud_onda = float(partes[0])
                        indice_refraccion = float(partes[1])
                        resultados.append((longitud_onda, indice_refraccion))
                    except ValueError:
                        pass

            return resultados

tuplas_resultantes = procesar_archivo_yml(ruta_archivo_yml)
for i in tuplas_resultantes:
    print(i)

#----------------------------------------Hasta aca todo iba bien.



def procesar_archivo_yml(ruta_archivo):
    # Código de procesamiento del archivo YAML que mencionaste

    longitudes_onda, indices_refraccion = zip(*tuplas_resultantes)

n_promedio = np.mean(indices_refraccion)
n_desviacion_estandar = np.std(indices_refraccion)

plt.plot(longitudes_onda, indices_refraccion, label='Kapton')

plt.xlabel('Longitud de Onda (nm)')
plt.ylabel('Índice de Refracción')
plt.title(f'Índice de Refracción en Función de la Longitud de Onda\nKapton - n Promedio: {n_promedio:.2f}, Desviación Estándar: {n_desviacion_estandar:.2f}')
plt.legend()

plt.grid()
plt.show()


