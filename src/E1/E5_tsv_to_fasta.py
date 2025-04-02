"""
Ejercicio 5: Convertir un archivo TSV a FASTA.

Este script lee un archivo TSV (valores separados por tabulaciones) que contiene
IDs y secuencias de ADN, y lo convierte a formato FASTA.
"""

#Rutas de los archivos
input_file = "../../data/E1/5_dna_sequences.txt"
output_file = "../../results/E1/5_dna_sequences.fa"

#Lectura de archivos
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:

        #Separar el ID y la secuencia
        id,sequence = line.strip().split("\t")

        #Escribir en formato FASTA y mandar la salida a un archivo
        outfile.write(f">{id}\n{sequence.upper()}\n")