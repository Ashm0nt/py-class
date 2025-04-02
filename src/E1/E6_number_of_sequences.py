#Ejercicio 6 Contar lienas en un archivo FASTA

# Ruta del archivo de entrada
## Proviene del output del ejercicio 5
input_file = "../../results/E1/5_dna_sequences.fa"

#Lectura del archivo de entrada
with open(input_file, "r") as infile:
    lines = infile.readlines()

    #Cuenta cuántas secuencias hay en el archivo (líneas que comienzan con >)
    lines_filtred =[line for line in lines if line.startswith(">")]
    print(f"El archivo {input_file} tiene {len(lines_filtred)} secuencias.")