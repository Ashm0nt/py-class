"""
Ejercicio 4: Eliminar adaptadores de secuencias.

Este script lee un archivo de secuencias de ADN con adaptadores,
elimina los primeros 14 nucleótidos (asumiendo que son los adaptadores)
y escribe las secuencias limpias en un archivo de salida.
"""

#Rutas de los archivos 
input_file = "../../data/E1/4_input_adapters.txt"
output_file = "../../results/E1/4_output_no_adapters.txt"

#Abre el archivo de entrada y salida
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:

        #Cortar adaptadores de la secuencia 4_input_adapters.txt
        clean_sequence = line.strip()[14:]

        #Manda la salida a un archivo 4_input_no_adapters.txt
        outfile.write(f"{clean_sequence}\n")

        #Opcion alterna 
        #print (clean_sequence, file=outfile, end="\n")
