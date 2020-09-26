from src.codificador import Codificador
from src.decodificador import Decodificador

##### Configuracao do codificador #####

# Se deseja codificar:
codificar = True

# Nome do arquivo:
nome_arquivo = 'data/alice29.txt'

''' Tipos
    0 = Golomb
    1 = Elias Gamma
    2 = Fibonacci
    3 = Unaria
    4 = Delta
'''

# Escolha o tipo de codificacao
tipo = 4

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
nome_arquivo_codificado = 'alice29.delta'

# Extensao do novo arquivo decodificado
extensao_saida = 'txt2'

#########################################

# Codificacao:
if codificar:
    codifica = Codificador()
    codifica.codificar(nome_arquivo, tipo, golomb_divisor)

# Decodificacao:
if decodificar:
    decodifica = Decodificador()
    decodifica.decodificar(nome_arquivo_codificado, extensao_saida)