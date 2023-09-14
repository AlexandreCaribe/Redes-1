import requests
import ast
import socket
import json
import re

hist_compras = []

def iniciar_compra():
    print("Iniciando compra...")
    path = '/iniciar_compra'
    #url = "http://34.95.163.62:3389/iniciar_compra"
    url = "http://172.16.103.0:3389/iniciar_compra"
    #data = {"OK": "OK"}

    try:
        #response = requests.post(url, data)
        response = requests.post(url)
        request = "POST {} HTTP/1.1\r\nHost: 34.95.163.62\r\n\r\n".format(path)
        conexao(request)
        print("Compra iniciada com sucesso!")
    except Exception as e:
        print("\n")

def receber_json():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_ip = "172.16.103.0"
        server_port = 8889
        client.connect((server_ip, server_port))

        json_data = b""
        '''
        while True:
            data = client.recv(1024)
            if not data:
                break
            json_data += data
            print("\n\nAQUOO", json_data)
        '''
        data = client.recv(1024)
        json_str = data.decode("utf-8")
        #print("JSON recebido:", json_str)
        #print(type(json_str))
        #print(json_str)
        json_obj = json.loads(json_str)
        valor_total = json_obj.get("Valor Total", 0)
        nomes_produtos = json_obj.get("Lista de Produtos", 1)
        valores_produtos = json_obj.get("Valores dos Produtos", 2)

        intercalar = [f'{nomes_produtos[i]} [{valores_produtos[i]}]\n' for i in range(len(nomes_produtos))]
        print("\nProduto Preco:\n", "".join(intercalar))


        print("Valor Total:", valor_total)
        #print("Valores dos Produtos:", valores_produtos)
        #print("Nomes dos Produtos:", nomes_produtos)

                    
        '''
        json_obj = json.loads(json_str)  # Converter a string JSON em um objeto Python
        total_value = json_obj.get('Valor Total', 0)
        prod_prec = json_obj.get('Lista de produtos', {})
        print("Status da operação: Compra Realizada")
        print("Total Value:", total_value)
        print("Prod Prec:", prod_prec)
        '''
        return valor_total
    except Exception as e:
        print("\n")
    finally:
        client.close()

def pagar(valor):
    print("Seu carrinho custa:", valor)
    pgt = input("Digite o Valor que deseja pagar: ")
    if(float(pgt) < valor):
        pagar(valor)
    else:
        print("Pagamento Confirmado!")
        
def conexao(req):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_port = 8888
    server_ex = "172.16.103.0"

    try:
        client.connect((server_ex, server_port))
        client.send(req.encode())

        response = client.recv(1024)
        resp_str = response.decode("utf-8")
        resp = resp_str.split("\n")
        return resp_str
    except Exception as e:
        print("Erro ao conectar:", e)

def main():
    print("Bem-vindo ao Caixa Inteligente!")
    while True:
        print("\nOpções:")
        print("1. Iniciar Compra")
        print("2. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            iniciar_compra()
            pgmt = receber_json()
            pagar(pgmt)
        elif choice == '2':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
