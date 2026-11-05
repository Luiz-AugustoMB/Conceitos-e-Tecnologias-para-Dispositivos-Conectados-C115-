from mininet.topo import Topo

class MyTopo( Topo ):
    "Topologia customizada com 3 switches e 5 hosts."

    def __init__( self ):
        "Criar topologia customizada."

        # Inicializar topologia
        Topo.__init__( self )

        # Criar os hosts
        host1 = self.addHost( 'h1' )
        host2 = self.addHost( 'h2' )
        host3 = self.addHost( 'h3' )
        host4 = self.addHost( 'h4' )
        host5 = self.addHost( 'h5' )

        # Criar os switches
        Switch1 = self.addSwitch( 's1' )
        Switch2 = self.addSwitch( 's2' )
        Switch3 = self.addSwitch( 's3' )

        # Criar os links dos hosts
        self.addLink( host1, Switch1 )
        self.addLink( host2, Switch1 )
        self.addLink( host3, Switch2 )
        self.addLink( host4, Switch3 )
        self.addLink( host5, Switch3 )

        # Criar os links entre os switches
        self.addLink( Switch1, Switch2 )
        self.addLink( Switch2, Switch3 )


topos = { 'mytopo': ( lambda: MyTopo() ) }
