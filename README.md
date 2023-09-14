# Problema 1 - Supermercado Inteligente
## Resumo
Este repositório contém os códigos fonte e recursos relacionados ao projeto Supermercado Inteligente. O projeto consiste em uma solução de caixa de supermercado inteligente que permite aos usuários iniciar compras, receber informações sobre os produtos adquiridos e efetuar o pagamento. Os códigos aqui presentes são divididos em três partes: o servidor Python que lida com as leituras de sensores RFID e operações dos produtos, o cliente Python que inicia e conclui compras e a integração com uma Raspberry Pi para aquisição de dados dos sensores.

## Abstract
This repository contains the source code and related resources for the Smart Supermarket project. The project is a smart supermarket checkout solution that enables users to initiate purchases, receive information about purchased products, and complete payments. The code presented here is divided into three parts: the Python server that handles RFID sensor readings and product operations, the Python client that initiates and completes purchases, and the integration with a Raspberry Pi for sensor data acquisition. This solution aims to enhance efficiency and the shopping experience for customers in supermarkets.

## Introdução
A automação se tornou um tópico popular e se tem experimentado um crescimento notável nos últimos anos, impulsionado pela constante evolução da tecnologia. Diversas tendências têm contribuído para esse progresso, com benefícios que buscam aprimorar suas operações, reduzir custos e elevar a produtividade. Em particular, a automação pode melhorar e acelerar todo e qualquer tipo de operação manual.

Seguindo essa tendência, nos foi pedido para criar um Sistema de Automação em um Supermercado, o que facilitaria todo o processo de compras de produtos e que fácilmente se pagaria pela não necessidade de funcionários realizando o trabalho manual.

Baseado nessa ideia nos foi proposto desenvolver um sistema de Caixa de Supermercado automatizado com acesso a um Leitor RFID (tecnologia de Identificação por Radiofrequência) que executará todo o processo de identificação de produtos e preços em questão de segundos, já mostrando os valores a serem pagos. A tecnologia RFID com suporte à leitura simultânea de etiquetas permite o pagamento sem atritos, onde diversos produtos são automaticamente identificados e registrados em grupo. Isso reduz a necessidade de escanear cada item individualmente e agiliza o fluxo de clientes pelos caixas.

## Fundamentação Teórica

Internet das Coisas (IoT):

A IoT refere-se à interconexão de dispositivos e objetos físicos à internet, permitindo a coleta e troca de dados em tempo real. Quando aplicada a supermercados, a IoT possibilita a criação de um ecossistema digital em que os diversos componentes, como prateleiras, carrinhos de compras, caixas e produtos, estão conectados à rede.

Identificação por Radiofrequência (RFID):

A tecnologia RFID é uma abordagem de identificação automática que utiliza sinais de rádio para transmitir dados entre uma etiqueta RFID e um leitor. No contexto de supermercados inteligentes, cada produto é equipado com uma etiqueta RFID contendo informações úteis, como nome, preço e outros detalhes. Isso oferece benefícios notáveis:

1. Pagamento sem Atritos: Quando os produtos têm etiquetas RFID, os clientes podem simplesmente colocar os itens em seus carrinhos e, ao passarem pelo caixa, as etiquetas são lidas automaticamente pelo leitor RFID. Isso elimina a necessidade de escanear cada produto individualmente, tornando o processo de pagamento muito mais rápido e conveniente.

2. Precisão no Registro de Compras: O RFID reduz consideravelmente erros de registro de produtos, uma vez que a identificação é automatizada. Isso evita a duplicação de produtos ou erros de preço.

3. Rastreamento de Produtos: A tecnologia RFID permite o rastreamento em tempo real de produtos desde o momento em que são colocados nas prateleiras até a compra pelo cliente. Isso é valioso para gerenciamento de estoque e prevenção de perdas.

4. Segurança: Os sistemas RFID podem ser usados para fins de segurança, ajudando a prevenir o roubo de produtos, pois as etiquetas RFID podem ser desativadas no caixa.

A implementação de uma API REST (Representational State Transfer) desempenha um papel fundamental na orquestração e controle do fluxo de informações em um ambiente de supermercado inteligente, especialmente quando se trata da integração de tecnologias como RFID, IoT e sistemas de gerenciamento.

Aqui estão algumas considerações importantes sobre a implementação de uma API REST para controlar o fluxo de informações em um contexto de supermercado inteligente:

## Metodologia
O projeto é dividido em três partes principais:
1. **Servidor RFID:** Um servidor Python que lida com as leituras de sensores RFID e fornece informações sobre os produtos aos clientes.
2. **Cliente de Caixa:** Um cliente Python que permite aos usuários iniciar compras, receber informações sobre os produtos e efetuar o pagamento.
3. **Raspberry Pi:** Uma Raspberry Pi que coleta dados dos sensor RFID de produtos e envia esses dados para o servidor.

A operação tem inicio com o Cliente chegando ao Caixa, a partir daí ele têm a opção de iniciar compra, isso feito é chamada uma função que inicia o processo de compra realizando uma requisição para o Servidor RFID. A partir do momento que ele recebe a resposta ele apenas a exibe para o Cliente a lista de produtos, a lista de preços e o Valor Total da Compra. Dando a possibilidade de efetuar o pagamento logo em seguida e ao concluir o pagamento o cliente tem a tranquilidade de saber que todo o processo foi efetuado com sucesso em questão de segundos.


O Servidor fica esperando uma requisição POST para iniciar a operação. Quando ele detecta essa requisição ele cria uma conexão TCP/IP com a Raspberry Pi se utilizando do padrão Rest API para requisitar a leitura dos sensores RFID, feito isso o Servidor recebe essa resposta e trata a resposta para ser enviada em formato JSON para o Caixa, para haver essa conexão é necessário mais uma conexão TCP IP enviando a resposta da requisição para o Caixa já contendo o JSON com todas informações já processadas e calculadas para que o Caixa tenha apenas a função de receber a lista de produtos, a lista de preços e o Valor Total da Compra.

A Raspberry Pi tem uma única função que é a de leitura do sensor RFID e enviar esse dado como resposta para a conexão TCP/IP do Servidor.

O problema segue esse Fluxo: 
![Casos drawio+(1)](https://github.com/AlexandreCaribe/Redes-1/assets/38389307/1b166fd0-8b2f-4ff1-b9a9-c6465de9035c)

## Para a execução do problema é necessário seguir estes passos abaixo

#### Executar os Código dentro da Raspberry Pi:
```
  SSH -o ServerAliveInterval= 60 172.16.103.0
```
```
  cd TP01/Alexandre/exec
```
```
  python3 rasp.py
```

```
  python3 server.py
```

####Executar o código do Caixa:

```
  python3 caixa.py
```

## Resultados e Discussões
Os resultados do projeto incluem uma solução funcional de caixa inteligente que simplifica o processo de compra para os clientes. No entanto uma solução incompleta visto que não foi possível colocar a aplicação funcional na nuvem com o Google Cloud, pois ao fazer requisições do Cliente para o Servidor havia alguma barreira travando essa comunicação. O Servidor ainda respondia as requisições através do Insomnia, porém ele não identificava de forma alguma as requisições do Cliente Local, mesmo com todas as informações de endereços IPs e portas corretamente, além de estar habilitado o modo HTTP e HTTPS para comunicação no Google Cloud.

O Administrador também ficou incompleto sem poder visualizar o Histórico de Compras, Compras atuais e bloquear/liberar caixa. 

As discussões se concentram nas vantagens da automação e no potencial de expansão e aprimoramento do sistema. Como uma melhoria na Interface do Cliente, uma comunicação ainda mais rápida do Servidor e expansão de produtos e metódos usando Banco de Dados ou implementando outras aplicações.

## Conclusão
O projeto Supermercado inteligente demonstra que se bem-aplicada a automação de Compras de supermercado pode se beneficiar muito de tecnologias como RFID, comunicação em rede e automação de serviço. Essa solução pode ser implementada em estabelecimentos comerciais para melhorar a eficiência e a experiência do cliente.É necessário fazer uma implementação mais limpa e completa com comunicação com a nuvem e funções administrativas implementadas.

Autor
=======
| [<img src="https://avatars.githubusercontent.com/u/38389307?v=4" width=115><br><sub>Alexandre Silva Caribé</sub>](https://github.com/AlexandreCaribe) 
