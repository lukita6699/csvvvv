import csv
#Crear el contexto para abrir un nuevo archivo .csv
with open('nuevo_archivolol.csv', 'w', newline='', encoding='utf-8') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
# Escribir una fila en el archivo CSV
    escritor_csv.writerow(lista)
# Escribir múltiples filas en el archivo CSV
    escritor_csv.writerows(matriz)
print ("Se creo correctamente el archivo .csv"); 

import csv
with open('nuevo_archivolol.csv', 'r', newline='', encoding='utf-8') as archivo_csv:
    lector_csv = csv.reader (archivo_csv);
    for x in lector_csv:
        print (x) 