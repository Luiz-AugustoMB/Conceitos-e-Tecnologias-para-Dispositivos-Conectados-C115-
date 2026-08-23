from socket import *

# ---------------------------------------------------------------
# C115 - Projeto 1: Mini Kahoot com Sockets TCP
# CLIENTE
#
# Como rodar:  python quiz_cliente.py   (com o servidor ja rodando)
# ---------------------------------------------------------------

serverName = 'localhost'
serverPort = 3000
totalQuestoes = 3  # o servidor envia 3 questoes

# cria o socket TCP e conecta no servidor
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

print('=========================================')
print('        MINI KAHOOT - C115')
print('=========================================')

# 1) informa o nome de usuario ao servidor
nome = input('Digite seu nome de usuario: ')
# a mensagem deve estar em bytes antes de ser enviada ao buffer de transmissao
clientSocket.send(nome.encode())

print('\nVoce vai responder', totalQuestoes, 'questoes. Responda com A, B, C ou D.\n')

# 2) recebe uma questao por vez e envia a resposta
for i in range(totalQuestoes):
    # devemos converter a mensagem de volta para string antes de imprimir
    questao = clientSocket.recv(1024).decode()
    print(questao)

    # so aceita as letras validas, senao pede de novo
    resposta = input('Sua resposta: ').strip().upper()
    while resposta not in ['A', 'B', 'C', 'D']:
        print('Opcao invalida! Digite apenas A, B, C ou D.')
        resposta = input('Sua resposta: ').strip().upper()

    clientSocket.send(resposta.encode())
    print('')

# 3) recebe o resultado final com a correcao
resultado = clientSocket.recv(2048).decode()
print(resultado)

# fecha a conexao
clientSocket.close()
