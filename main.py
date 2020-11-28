import os
import time
from src.codificador import Codificador
from src.decodificador import Decodificador

##### Configuracao do codificador #####

def execution_time(start_time):
    # print(" Time : %s second" % (time.time() - start_time))
    return (time.time() - start_time)*1000


def print_file_size(file_name):
    file_size = os.path.getsize(file_name)
    return file_size 

def get_decompression_size(data):
    file = os.getcwd()
    file = file+ "/"+ data
    return print_file_size(file)


# Se deseja codificar:
codificar = True

# Nome do arquivo:
# nome_arquivo = 'data/alice29.txt'
nome_arquivo = 'data/group5/SD4.dat'

''' Tipos
    0 = Golomb
    1 = Elias Gamma
    2 = Fibonacci
    3 = Unaria
    4 = Delta
'''

# Escolha o tipo de codificacao
tipo = 0

golomb_divisor = 16 # Deve ser potencia de 2 (2, 4, 8, 16,...)

#######################################

##### Configuracao do decodificador #####

# Se deseja decodificar:
decodificar = True

'''Extensoes dos arquivos possiveis:
    .golomb     = Golomb
    .eliasgamma = Elias Gamma
    .fibonacci  = Fibonacci
    .unaria     = Unaria
    .delta      = Delta
'''
# Nome do arquivo que deseja decodificar:
# nome_arquivo_codificado = 'alice29.golomb'
nome_arquivo_codificado = 'SD4.golomb'
# Extensao do novo arquivo decodificado
# extensao_saida = 'txt'
GOLOMB=".golomb"
extensao_saida = 'dat'

#########################################
import pathlib
FILE_PATH = "/Users/smart/Desktop/golomb/data_group5"
conpression_time = 0.0
original_size=0
compressed_size =0
uncompress_size=0
decompress_time =0.0
compressed_file_name =""
for path in sorted (pathlib.Path(FILE_PATH).iterdir()):
    if path.is_file():
        data = str(path)
        data = data.split("/")[-1]
        print("\n")
        print("Golomb ON : %s " %data.split(".")[0])
        # Codificacao:
        if codificar:
            file_name = str(path)
            codifica = Codificador()
            original_size = print_file_size(file_name)
            start_time = time.time()
            codifica.codificar(file_name, tipo, golomb_divisor)
            conpression_time = execution_time(start_time)

        # Decodificacao:
        if decodificar:
            file_name_modified = str(path)
            file_name_modified = file_name_modified.split("/")[-1]
            file_name_modified = file_name_modified.split(".")[0]
            file_name_modified = file_name_modified+GOLOMB
            compressed_file_name = file_name_modified

            compressed_size = print_file_size(file_name_modified)
            start_time =time.time()
            decodifica = Decodificador()
            decodifica.decodificar(file_name_modified, extensao_saida)
            decompress_time = execution_time(start_time)
            
            
        print("Finished compression of : %s in %s ms" %(data,conpression_time))
        print("Original size : %s bytes " % original_size ) 
        print("Compressed size : %s bytes" % compressed_size )
        print("Compressed ratio : %s " % (original_size/compressed_size) )
        print("Finished decompression of %s in %s ms" % (compressed_file_name,decompress_time) )
        print("Uncompressed size : %s bytes" % get_decompression_size(data))

print("\n")