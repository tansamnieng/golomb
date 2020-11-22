import os
import time
from src.codificador import Codificador
from src.decodificador import Decodificador

##### Configuracao do codificador #####


def execution_time(start_time):
    print(" Time : %s second" % (time.time() - start_time))



def print_file_size(file_name,mode):
    file_size = os.path.getsize(file_name)
    file_size = file_size/1024 # to Kb
    if mode:
        print("Before compression : %d KB"%file_size)
    else:
        print("Decompression size : %d KB"%file_size)


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
extensao_saida = 'dat'

#########################################

# Codificacao:
if codificar:
    codifica = Codificador()

    print_file_size(nome_arquivo,True)
    start_time =time.time()
    codifica.codificar(nome_arquivo, tipo, golomb_divisor)
    execution_time(start_time)

# Decodificacao:
if decodificar:
    print_file_size(nome_arquivo_codificado,False)
    start_time =time.time()
    decodifica = Decodificador()
    decodifica.decodificar(nome_arquivo_codificado, extensao_saida)
    execution_time(start_time)