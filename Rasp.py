from __future__ import print_function 
import time 
from datetime import datetime 
import mercury 
import socket

#FUNCAO REAL

def leitura():
    reader = mercury.Reader("tmr:///dev/ttyUSB0", baudrate=115200) 
    
    print(reader.get_model()) 
    print(reader.get_supported_regions()) 
    
    reader.set_region("NA3") 
    reader.set_read_plan([1], "GEN2", read_power=2000) 
    print(reader.read())
    valor_epc = reader.read()
    valor = [epc.epc.decode() for epc in valor_epc]
    reader.stop_reading()
    dado = "\n".join(valor)
    return dado
'''
#APAGAR
class EPC:
    def __init__(self, value):
        self.epc = value

def leitura():
    epcs = [
        EPC(b'E20000172211010118905454'),
        EPC(b'E20000172211012518905484'),
        EPC(b'E20000172211010218905459'),
        EPC(b'E2000017221101321890548C'),
        EPC(b'E20000172211009418905449'),
        EPC(b'E2000017221100961890544A'),
        EPC(b'E2000017221101241890547C'),
        EPC(b'E20000172211011118905471'),
        EPC(b'E20000172211011718905474')
    ]
    return epcs
#APAGAR
'''

#Cria um objeto de socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET indica IPv4, SOCK_STREAM indica TCP

ip = "0.0.0.0"  #O endereço IP "0.0.0.0" significa que o servidor escutará em todas as interfaces de rede
port = 8888     #A porta em que o servidor vai escutar

try:
    #Associa o socket à combinação de endereço IP e porta
    server.bind((ip, port))
    
    #Coloca o socket em modo de escuta, com uma fila de tamanho 5 para conexões pendentes
    server.listen(5)
    
    #Imprime uma mensagem indicando o endereço IP e a porta em que o servidor está escutando
    print("Escutando em: " + ip + ":" + str(port))
    

    while True:
        #Aceita uma conexão do cliente (bloqueia até que uma conexão seja estabelecida)
        (client_socket, address) = server.accept()
    
        #Imprime o endereço IP que se conectou
        print("Recebido por: " + address[0])
    

        #Recebe dados do cliente (até 1024 bytes)
        data = client_socket.recv(1024)
        print("Data encodeL:\n",data.decode())
        #Compara os dados recebidos com a mensagem
        sensores = leitura()

        '''
        #APAGAR
        valor = [epc.epc.decode() for epc in sensores]
        dado = "\n".join(valor)
        sens = dado.encode()
        #APAGAR
        '''

        client_socket.send(sensores.encode())
        client_socket.close()
except Exception as erro:
    #Captura e imprime possíveis erros
    print(erro)
