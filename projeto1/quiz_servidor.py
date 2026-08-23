from socket import *

# ---------------------------------------------------------------
# C115 - Projeto 1: Mini Kahoot com Sockets TCP
# SERVIDOR
#
# Como rodar:  python quiz_servidor.py
# ---------------------------------------------------------------

serverPort = 3000

# banco de questoes do quiz (enunciado, alternativas e gabarito)
questoes = [
    {
        "enunciado": "Q1. Em redes, qual protocolo e orientado a conexao?",
        "alternativas": ["A) UDP", "B) TCP", "C) ICMP", "D) ARP"],
        "correta": "B"
    },
    {
        "enunciado": "Q2. Qual camada do modelo OSI e responsavel pelo roteamento dos pacotes?",
        "alternativas": ["A) Enlace", "B) Transporte", "C) Rede", "D) Aplicacao"],
        "correta": "C"
    },
    {
        "enunciado": "Q3. Qual e a porta padrao utilizada pelo protocolo HTTP?",
        "alternativas": ["A) 21", "B) 25", "C) 80", "D) 443"],
        "correta": "C"
    }
]

# cria o socket TCP (SOCK_STREAM) usando IPv4 (AF_INET)
serverSocket = socket(AF_INET, SOCK_STREAM)
# atribui a porta ao socket criado
serverSocket.bind(('', serverPort))
# aceita conexoes com no maximo um cliente na fila
serverSocket.listen(1)

print('Servidor do quiz pronto na porta', serverPort)

while True:
    # fica bloqueado aqui ate um cliente conectar
    connectionSocket, addr = serverSocket.accept()
    print('Cliente conectado:', addr)

    # 1) recebe o nome do usuario (chega em bytes, converte para string)
    nome = connectionSocket.recv(1024).decode().strip()
    print('Jogador:', nome)

    respostas = []  # guarda a letra respondida em cada questao

    # 2) envia uma questao por vez e SEMPRE espera a resposta antes de mandar a proxima.
    # Isso e importante porque o TCP e um fluxo de bytes: se o servidor mandasse
    # duas mensagens seguidas, elas poderiam chegar grudadas em um unico recv().
    for questao in questoes:
        # monta o texto da questao: enunciado + as 4 alternativas
        texto = questao["enunciado"] + "\n"
        for alternativa in questao["alternativas"]:
            texto = texto + alternativa + "\n"

        # envio tbm deve ser em bytes
        connectionSocket.send(texto.encode())

        # recebe a letra escolhida pelo cliente
        resposta = connectionSocket.recv(1024).decode().strip().upper()
        respostas.append(resposta)
        print('   resposta recebida:', resposta)

    # 3) corrige o quiz e monta o feedback final
    acertos = 0
    resultado = "=========================================\n"
    resultado = resultado + "RESULTADO FINAL\n"
    resultado = resultado + "Jogador: " + nome + "\n"

    linhas = ""
    for i in range(len(questoes)):
        correta = questoes[i]["correta"]
        marcada = respostas[i]

        if marcada == correta:
            acertos = acertos + 1
            situacao = "ACERTOU"
        else:
            situacao = "ERROU"

        linhas = linhas + "Q" + str(i + 1) + " (resposta: " + marcada
        linhas = linhas + " | correta: " + correta + ") -> " + situacao + "\n"

    resultado = resultado + "Total de acertos: " + str(acertos) + " de " + str(len(questoes)) + "\n"
    resultado = resultado + "-----------------------------------------\n"
    resultado = resultado + linhas
    resultado = resultado + "========================================="

    # 4) envia o resultado e encerra a conexao com esse cliente
    connectionSocket.send(resultado.encode())
    print('Quiz finalizado.', nome, 'acertou', acertos, 'de', len(questoes))
    print('-----------------------------------------')
    connectionSocket.close()
