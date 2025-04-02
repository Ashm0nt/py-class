"""
Ejercicio 11: Invertir secuencias de ADN.

Este script toma una lista de secuencias de ADN ingresadas por el usuario,
invierte cada secuencia y muestra los resultados.
"""

#Pide al usuario que ingrese varias secuencias de ADN separadas por comas.
sequences = input("Ingrese las secuencias de ADN separadas por comas: ").split(",")

#Invertir las secuencias 
#Usualmente despues de una coma se pone un espacio, manejamos los espacios
sequences_inverted = [sequence[::-1].strip() for sequence in sequences]

print(f"Las secuencias invertidas son: {sequences_inverted}")