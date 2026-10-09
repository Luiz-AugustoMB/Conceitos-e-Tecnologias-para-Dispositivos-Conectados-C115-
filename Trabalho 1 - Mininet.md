Login no mininet:

![Login no mininet](prints/00_login.png)

Comando para a criação da rede linear com 6 switches, limitando a largura de banda com 25 Mbps, e padronizando os endereços MAC:

```
sudo mn --topo=linear,6 --link tc,bw=25 --mac
```

![Criação da topologia](prints/01_criacao_topologia.png)

Confirmação dos nós e das conexões:

```
nodes
net
```

![nodes e net](prints/02_nodes_net.png)

Conferindo as informações de cada nó:

```
dump
```

![dump](prints/03_dump.png)

Conferindo os endereços MAC, se estão padronizados mesmo:

```
h1 ifconfig
h2 ifconfig
h3 ifconfig
h4 ifconfig
h5 ifconfig
h6 ifconfig
```

![ifconfig h1](prints/04_ifconfig_h1.png)
![ifconfig h2](prints/04_ifconfig_h2.png)
![ifconfig h3](prints/04_ifconfig_h3.png)
![ifconfig h4](prints/04_ifconfig_h4.png)
![ifconfig h5](prints/04_ifconfig_h5.png)
![ifconfig h6](prints/04_ifconfig_h6.png)

Realizando o teste de ping entre todos os nós:

```
pingall
```

![pingall](prints/05_pingall.png)

Realizando o ping de h1 para h2, com a contagem de 5:

```
h1 ping -c 5 h2
```

![ping h1 h2](prints/06_ping_h1_h2.png)

Realizando o ping de h1 para os demais hosts, também com a contagem de 5:

```
h1 ping -c 5 h3
h1 ping -c 5 h4
h1 ping -c 5 h5
h1 ping -c 5 h6
```

![ping h1 h3 h4](prints/07_ping_h1_h3_h4.png)
![ping h1 h5 h6](prints/08_ping_h1_h5_h6.png)

Feita toda a configuração com o Xming e o Putty, abrimos o terminal do Windows para H1 e H2:

```
xterm h1
xterm h2
```

![xterm h1 e h2](prints/09_xterm_h1_h2.png)

Configurando H1 como servidor TCP na porta 5555, com um relatório por segundo:

```
iperf -s -p 5555 -i 1
```

![Servidor h1](prints/10_iperf_servidor_h1.png)

Configurando H2 como cliente, conectando no H1 com um relatório por segundo e teste de 15 segundos:

```
iperf -c 10.0.0.1 -p 5555 -i 1 -t 15
```

![Cliente h2](prints/11_iperf_cliente_h2.png)

Resultado final do teste:

![Resultado iperf](prints/12_iperf_resultado.png)
