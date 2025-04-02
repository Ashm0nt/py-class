"""
Ejercicio 12: Encontrar secuencias de ADN que contengan un codón de parada.

Este script toma una lista de secuencias de ADN ingresadas por el usuario,
identifica y muestra las secuencias que contienen al menos un codón de parada (TAA, TAG o TGA).
"""

#Pide al usuario que ingrese varias secuencias de ADN separadas por comas.
sequences = input("Ingrese las secuencias de ADN separadas por comas: ").upper().split(",")


#Codones de paro
#Usalmente despues de una coma se pone un espacio, manejamos los espacios
sequences_stop = [sequence.strip() for sequence in sequences if "TAA" in sequence or "TAG" in sequence or "TGA" in sequence]

#Imprimir el resultado
print(f"Las secuencias que contienen un codón de parada son: {sequences_stop}")
