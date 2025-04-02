"""
Ejercicio 6: Contar líneas en un archivo FASTA.

Este script lee un archivo FASTA y cuenta el número de secuencias presentes en él.
Las secuencias en un archivo FASTA están identificadas por líneas que comienzan con '>'.
"""

# Ruta del archivo de entrada
## Proviene del output del ejercicio 5
input_file = "../../results/E1/5_dna_sequences.fa"

#Lectura del archivo de entrada
with open(input_file, "r") as infile:
    lines = infile.readlines()

    #Cuenta cuántas secuencias hay en el archivo (líneas que comienzan con >)
    lines_filtred =[line for line in lines if line.startswith(">")]
    print(f"El archivo {input_file} tiene {len(lines_filtred)} secuencias.")