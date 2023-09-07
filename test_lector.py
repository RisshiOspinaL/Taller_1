import yaml

# Ruta del archivo YAML
ruta_archivo_yml = r'Ariel'

def lector(archivo):
    try:
        with open(archivo) as objetivo:
            contenido = archivo.read()


            return archivo

test_1 = lector(ruta_archivo_yml)

print(test_1)

