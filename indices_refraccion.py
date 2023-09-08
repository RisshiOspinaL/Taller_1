#------------------------Punto 1.3:

import matplotlib.pyplot as plt
import os 
#print(os.listdir())


#ruta_archivo_yml = input("Ingrese la ruta del archivo: ")

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

#tuplas_resultantes = procesar_archivo_yml(ruta_archivo_yml)
#for i in tuplas_resultantes:
#    print(i)

#----------------------------------------Punto 1.4:




#tuplas_resultantes = procesar_archivo_yml(ruta_archivo_yml)

#longitudes_onda, indices_refraccion = zip(*tuplas_resultantes)


#plt.figure(figsize=(8, 6))


#plt.plot(longitudes_onda, indices_refraccion, label='Kapton')


#plt.xlabel('Longitud de Onda')
#plt.ylabel('Indice de Refracción')
#plt.title('Indice de Refracción v.s. Longitud de Onda - Kapton')
#plt.legend()

#plt.grid()

#--------------------------Punto 1.5:

def graficar_1(ruta_archivo_yml):
    
    tuplas = procesar_archivo_yml(ruta_archivo_yml)
    
    longitudes_onda, indices_refraccion = zip(*tuplas)

    plt.figure(figsize=(8, 6))

    plt.plot(longitudes_onda, indices_refraccion, label=ruta_archivo_yml.split("/")[1])

    plt.xlabel('Longitud de Onda')
    plt.ylabel('Indice de Refracción')
    plt.title('Indice de Refracción v.s. Longitud de Onda - Kapton '+ ruta_archivo_yml.split("/")[1])
    plt.legend()

    plt.grid()

    plt.savefig(ruta_archivo_yml.split(".")[0]+".pdf")
    plt.close()

graficar_1("Mezclas/PEDOT.yml")

os.listdir()

for i in os.listdir():
    if "." not in i:
        for j in os.listdir(i):
            if ".pdf" not in j:

                graficar_1(i+"/"+j)