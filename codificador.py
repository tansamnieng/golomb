import math

class Codificador():
    """Codifica arquivo."""

    def __init__(self):
        # Quantas caracteres/valores vai carregar por vez
        self.buffer_leitura = 500

    def codificar(self, arquivo, tipo, golomb_divisor = 0):
        """Codifica o arquivo com o tipo informado."""
        self.buffer_escrita = ''

        
        # Golomb - divisor deve ser potencia de 2 (2, 4, 8, 16,...)
        if tipo == 0:
            self.golomb_divisor = golomb_divisor
            self.logDivisor = int(math.log(self.golomb_divisor, 2))
            codificador = self._golomb
            codificador_final = self._trata_final_golomb
            extensao = '.golomb'
       
        destino = arquivo[arquivo.rfind('/')+1:]
        # print("Here"+destino)
        destino = destino[destino.rfind('\\')+1:]
        # print("#"+destino)
        # Cria arquivo de saida. Se arquivo tiver extensao, substitui pela nova
        if destino.rfind('.') >= 0:
            self.arquivo_destino = open(''.join([destino[:destino.rfind('.')], extensao]), 'wb')
        else:
            self.arquivo_destino = open(''.join([destino, extensao]), 'wb')

    
        self._criar_cabecalho(tipo, golomb_divisor)
        
        # Le arquivo que sera codificado
        with open(arquivo, 'rb') as file:
            # Le a quantidade de caracteres pemitidas no buffer
            leitura = file.read(self.buffer_leitura)

            # Leitura esta em binario "b' Lorem ipsum..."
            while (leitura != b''):
                # Separa cada caracter para codificar (L, o, r, e, m ...)
                for caracter in leitura: # Caracter = valor inteiro do binario (1001 = 9)
                    # Caractere de L vira o inteiro 76
                    self.buffer_escrita += codificador(caracter)
                    self._escrever_arquivo()

                leitura = file.read(self.buffer_leitura)

            # Se sobrou valores no buffer (quando for menos de 8 bits)
            if self.buffer_escrita != '':
                self._escrever_arquivo(True, codificador_final)

        file.close()
        self.arquivo_destino.close()
        # print('Codificado com sucesso!')

    def _criar_cabecalho(self, tipo, golomb_divisor, maiorValorDelta = 0):
        # Primeiro byte, informa qual o tipo da codificacao
        self.buffer_escrita += str(bin(tipo)[2:]).zfill(8)
        # Segundo byte, informa o divisor do Golomb
        self.buffer_escrita += str(bin(golomb_divisor)[2:]).zfill(8)
        # Terceiro byte, informa o maior valor do Delta
        self.buffer_escrita += str(bin(maiorValorDelta)[2:]).zfill(8)

    def _escrever_arquivo(self, final = False, codificador_final = None):
        """Transforma os bits em byte e salva no arquivo"""
        # Monta conjuntos de 8 bits para transformar em byte e salvar
        while len(self.buffer_escrita) >= 8:
            ## Não achei uma forma de transformar o binário (string) direto para byte, por isso essas convercoes ##
            # Transformar binario em inteiro
            inteiro = int(self.buffer_escrita[:8], 2)
            # Transforma inteiro em byte
            byte = bytes([inteiro])

            self.arquivo_destino.write(byte)

            # Tira os 8 bits do buffer que foram salvos no arquivo
            self.buffer_escrita = self.buffer_escrita[8:]

        # Se for ultima parte do arquivo, trata para atingir 8 bits e salva
        if final:
            self.buffer_escrita = codificador_final()
            inteiro = int(self.buffer_escrita, 2)
            byte = bytes([inteiro])
            self.arquivo_destino.write(byte)

    def _int_para_str_binario(self, inteiro):
        # Transforma inteiro em binario no formado string
        return bin(inteiro)[2:].zfill(8) # Formato string com len = 8

    ################ CODIFICADORES ################
    # Recebe valor inteiro do binario e retorna binario codificado
    """
        Regra básicas de todos codificadores:
            - Todos recebem valor inteiro de 0 a 255 que representa um byte
            - Serão chamadas a cada byte existe no arquivo de leitura
            - Todos devem retornar binarios no formato String ('111001'), os
                quais serao adicionados no arquivo codificado

        Trata_final == Quando nao for possivel completar um byte inteiro com a
            ultima parte dos bits codificados, entao devera ser feito algum
            tratamento para preencher o byte ou na hora de decodificar pode
            dar algum problema

        Se for necessario utilizar o binario em vez do valor inteiro, pode ser
            utilizado o metodo "_int_para_str_binario" para receber o binario do
            valor inteiro em formato string (entrada: 10, retorno: '00001010')
    """

    # Golomb --> prefixo(unario) + 1 + sufixo(binario)
    def _golomb(self, valor):
        # Calcula o quociente
        quociente = int(valor / self.golomb_divisor)
        # Calcula o resto
        resto = bin(valor % self.golomb_divisor)[2:].zfill(self.logDivisor)
        # Retorna o valor codificado
        return '1'.zfill(quociente + 1) + str(resto)

    # Escreve o Golomb no buffer
    def _trata_final_golomb(self):
        return self.buffer_escrita.ljust(8, '0')









