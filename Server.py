import threading  # Importe a biblioteca threading
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import uuid
import subprocess

# Endereço e porta da Raspberry Pi
RASPBERRY_IP = "172.16.103.0"  # Substitua pelo IP da Raspberry Pi
RASPBERRY_PORT = 8888  # Substitua pela porta da Raspberry Pi


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/iniciar_compra':
            api = API()
            api.do_POST(self.path)
        else:
            print('\nErro ao iniciar compra')


class API():
    def do_POST(self, path):
        if path == '/iniciar_compra':
            thread = threading.Thread(target=self.handle_purchase_request)
            thread.start()
        else:
            print('\nErro ao iniciar Thread da compra')
    def handle_purchase_request(self):
        try:
            x, y, z = self.solicitar_sensor()
            #print("Resposta RasP:\n", x,y,z)
            response_data = {"message": "Compra iniciada", "Valor Total": x, "Lista de Produtos": y, "Valores dos Produtos": z}
            request = f"POST /iniciar_compra HTTP/1.1\r\n" \
                      f"Host: {RASPBERRY_IP}\r\n" \
                      f"Content-Type: application/json\r\n" \
                      f"Content-Length: {len(response_data)}\r\n" \
                      f"\r\n" \
                      f"{response_data}"
            self.enviar_json(response_data)
        except Exception as e:
            print("\nErro ao processar solicitação de compra:", e)

    def enviar_json(self, data):
        try:
            #print("\n\n\nJSON enviado para o Caixa:\n", data)
            json_data = ''
            bytes_data = b''
            json_data = json.dumps(data)
            bytes_data = json_data.encode("utf-8")
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET indica IPv4, SOCK_STREAM indica TCP
            ip = "0.0.0.0"  #O endereço IP "0.0.0.0" significa que o servidor escutará em todas as interfaces de rede
            port = 8889     #A porta em que o servidor vai escutar

            #Associa o socket à combinação de endereço IP e porta
            server.bind((ip, port))
            
            #Coloca o socket em modo de escuta, com uma fila de tamanho 5 para conexões pendentes
            server.listen(5)
            
            #Imprime uma mensagem indicando o endereço IP e a porta em que o servidor está escutando
            print("\nEscutando em: " + ip + ":" + str(port))
            while True:
                #Aceita uma conexão do cliente (bloqueia até que uma conexão seja estabelecida)
                (client_socket, address) = server.accept()
            
                #Imprime o endereço IP que se conectou
                print("\nRecebido por: " + address[0])
                #Recebe dados do cliente (até 1024 bytes)
                client_socket.send(bytes_data)
                print(bytes_data)

                #client_socket.close()
                matar_porta = self.check_ports()
            server.close()
        except Exception as e:
            print("\n",e)

    def solicitar_sensor(self):
        nomes_prod = []
        valor_prod = []
        valor_total = 0
        produtos = {
        'E20000172211010118905454': ("Banana", 2.00),
        'E20000172211011718905474': ("Maca", 3.00),
        'E2000017221101241890547C': ("Jaca", 4.00),
        'E2000017221100961890544A': ("Pera", 5.00),
        'E20000172211009418905449': ("Caju", 6.00),
        'E20000172211012518905484': ("Manga", 7.00),
        'E20000172211011118905471': ("Goiaba", 1.00),
        'E2000017221101321890548C': ("Acerola", 1.50),
        'E20000172211010218905459': ("Maracuja", 2.50),

        }                                                                                                                                                                             
                                                                                                                                                                                    

        # Cria um objeto de socket TCP
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET indica IPv4, SOCK_STREAM indica TCP
                                                                                                                                                                                    
        # Define o endere      o IP e a porta do servidor                                                                                                                             
        #server_ip = "172.16.103.0"  # Endere      o IP do servidor (localhost neste exemplo)
        server_port = 8888      # Porta em que o servidor est       escutando
        server_ex = "0.0.0.0"


        try:
            # Conecta-se ao servidor
            #client.connect((RASPBERRY_IP, RASPBERRY_PORT))
            client.connect((server_ex, server_port))            
            # Envia uma mensagem para o servidor
            msg = "GET /sensor HTTP/1.1\nHost: {}\n\n".format(RASPBERRY_IP)
            client.send(msg.encode())
            
            # Recebe e imprime a resposta do servidor
            response = client.recv(1024)
            resp_str = response.decode("utf-8")
            resp = resp_str.split("\n")
            for item in resp:
                if item in produtos:
                    nome, valor = produtos[item]
                    valor_total += valor
                    nomes_prod.append(nome)
                    valor_prod.append(valor)
                else:
                    print("Prod nao encontrado\n")  
        except Exception as erro:
            # Captura e imprime poss      veis erros
            print(erro)
        finally:
            # Fecha o socket do cliente ap      s a comunica            o
            client.close()
            print("FIM DA CONEXAO")
            #print("Resposta RasP:\n", valor_total, nomes_prod, valor_prod)
            return valor_total, nomes_prod, valor_prod

def run():
    server_address = ('', 3389)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print('Starting server...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
