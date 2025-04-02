"""
Ejercicio 7: Extraer los primeros tres nucleótidos de cada secuencia.

Este script toma una lista de secuencias de ADN ingresadas por el usuario,
extrae los primeros tres nucleótidos (codones de inicio) de cada secuencia
y muestra los resultados.
"""

#Pedir al usuario que ingrese varias secuencias de ADN separadas por comas.
##Usualmente despues de una coma se pone un espacio
sequences = input("Ingrese las secuencias de ADN separadas por comas: ").split(",")

#Extraer los primeros tres nuqleótidos de cada secuencia.
#Usalmente despues de una coma se usan espacio, se manejan los espacios
start_codons = [sequence.strip()[:3] for sequence in sequences]
print(f"Los primeros tres nucleótidos de cada secuencia son: {start_codons}")

#codondes_inicio = [sequence[:3] for sequence in sequences] cuando no se usan espacios de separacion