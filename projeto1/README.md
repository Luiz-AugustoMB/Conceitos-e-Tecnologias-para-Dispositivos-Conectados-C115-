# Projeto 1 - Mini Kahoot com Sockets TCP (C115)

Quiz de 3 questões executado no terminal, com servidor e cliente se comunicando por **Sockets TCP** (`AF_INET` + `SOCK_STREAM`).

## Arquivos

| Arquivo | Função |
|---|---|
| `quiz_servidor.py` | Guarda as questões e o gabarito, envia as perguntas, corrige e devolve o resultado |
| `quiz_cliente.py` | Pede o nome, mostra as questões, envia as respostas e imprime o resultado final |

## Como executar

Abra **dois terminais** na pasta do projeto.

Terminal 1 (servidor):

```
python quiz_servidor.py
```

Terminal 2 (cliente):

```
python quiz_cliente.py
```

> Para rodar em máquinas diferentes, troque `serverName = 'localhost'` no cliente pelo IP da máquina do servidor (a porta usada é a **3000**).

## Fluxo da comunicação

```
CLIENTE                                SERVIDOR
   |-- connect() --------------------->|  accept()
   |-- nome de usuario --------------->|
   |<-- Q1 + alternativas -------------|
   |-- letra (A/B/C/D) --------------->|
   |<-- Q2 + alternativas -------------|
   |-- letra (A/B/C/D) --------------->|
   |<-- Q3 + alternativas -------------|
   |-- letra (A/B/C/D) --------------->|
   |<-- resultado final ---------------|  corrige as 3 respostas
   |-- close() ----------------------->|  close()
```

A troca é sempre **pergunta → resposta** (ping-pong). Isso é proposital: como o TCP é um fluxo contínuo de bytes, duas mensagens enviadas em sequência poderiam chegar grudadas em um único `recv()`. Esperando a resposta do cliente antes de enviar a próxima questão, cada `recv()` recebe exatamente uma mensagem.

## Exemplo de saída

```
=========================================
RESULTADO FINAL
Jogador: Luiz
Total de acertos: 2 de 3
-----------------------------------------
Q1 (resposta: B | correta: B) -> ACERTOU
Q2 (resposta: A | correta: C) -> ERROU
Q3 (resposta: C | correta: C) -> ACERTOU
=========================================
```

## Detalhes de implementação

- **Gabarito fica só no servidor.** O cliente nunca recebe a resposta correta antes do fim — a correção é feita no servidor.
- **Validação no cliente.** Só aceita `A`, `B`, `C` ou `D`; qualquer outra entrada é pedida de novo (sem gastar mensagem na rede).
- **Normalização no servidor.** As respostas passam por `.strip().upper()`, então minúsculas também funcionam.
- **Servidor contínuo.** Depois de encerrar um jogador, o `while True` volta ao `accept()` e atende o próximo (um por vez).
