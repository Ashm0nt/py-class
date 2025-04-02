"""
Ejercicio 9: Transformar secuencias de ADN en ARN.

Este script toma una lista de secuencias de ADN ingresadas por el usuario,
reemplaza todas las timinas (T) por uracilos (U) para convertirlas en secuencias de ARN,
y muestra los resultados.
"""

#Pedir al usario que ingrese varias secuencias de ADN separadas por comas.
#Usualmente despues de una coma se pone un espacio, manejamos los espacios
sequences = input("Ingrese las secuencias de ADN separadas por comas: ").split(",")

#Transformar las secuencias de ADN en ARN
sequences_arn =[sequence.replace("T", "U").split() for sequence in sequences]

#Imprimir las secuencias de ARN
print(f"Las secuencias de ARN son: {sequences_arn}")

