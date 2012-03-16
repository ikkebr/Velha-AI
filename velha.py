#*-* encoding: iso-8859-1 *-*
class Jogo(object):

    def __init__(self):
        '''Construtor - tabuleiro, pilha de jogadas e vencedor'''

        self.tabuleiro = [ '-' for i in range(0,9) ]
        self.jogadas = []
        self.vencedor = None
        
    def turno(self):
        return len(self.jogadas)+1

    def mostra_tabuleiro(self):
        '''Exibe o tabuleiro'''
        
        print u"\nTabuleiro atual:"
        
        for j in [0, 3, 6]: #linhas
            for i in [0, 1, 2]: #colunas
                if self.tabuleiro[j+i] == '-':
                    #print "%d" % (j+i),
                    print '-',
                    if i != 2:
                        print "|",
                else:
                    print "%s" % self.tabuleiro[j+i],
                    if i != 2:
                        print "|",
    
            print "\n",


    def movimentos_disponiveis(self):
        '''Lista de posições disponíveis'''

        movimentos = []
        for i,v in enumerate(self.tabuleiro):
            if v=='-':
                movimentos.append(i)
        return movimentos

    def marcar(self, marca, pos):
        '''Marca o tabuleiro com X ou O'''
        self.tabuleiro[pos] = marca
        self.jogadas.append(pos)

    def pode_ganhar(self, marca):
        for pos in self.movimentos_disponiveis():
            self.marcar( marca, pos)
            if self.terminou():
               self.tabuleiro[pos] = '-'
               self.jogadas.pop()
               return pos
            else:
                self.tabuleiro[pos] = '-'
                self.jogadas.pop()
        return False


    def terminou(self):
        '''Verifica se alguém venceu'''

        posicoes_vitoria = [(0,1,2), (3,4,5), (6,7,8), (0,3,6),(1,4,7),(2,5,8), (0,4,8), (2,4,6)]

        for i,j,k in posicoes_vitoria:
            if self.tabuleiro[i] == self.tabuleiro[j] == self.tabuleiro[k] and self.tabuleiro[i] != '-':
                self.vencedor = self.tabuleiro[i]
                return True

        if '-' not in self.tabuleiro:
            self.vencedor = '-'
            return True

        return False

    def jogar(self, jogador1, jogador2):
        '''Executa o jogo com jogador1 e jogador2'''

        self.j1 = jogador1
        self.j2 = jogador2
    
        for i in range(9):

            self.mostra_tabuleiro()
            
            if i%2==0:
                print u"\t\t[Jogada de %s (%s)]"  % (self.j1.nome, self.j1.marca)

                self.j1.jogada(self)
            else:
                print u"\t\t[Jogada de %s (%s)]"  % (self.j2.nome, self.j2.marca)

                self.j2.jogada(self)

            if self.terminou():
                self.mostra_tabuleiro()
                if self.vencedor == '-':
                    print u"\nEmpate!"
                else:
                    print u"\tVencedor : %s" %self.vencedor
                return

class Humano(object):
    '''Jogador Humano'''

    def __init__(self,nome, marca):
        self.nome = nome
        self.marca = marca
    
    def jogada(self, tabuleiro):

        while True:
        
            m = raw_input(u"Qual sua jogada? ")

            try:
                m = int(m)
            except:
                m = -1
        
            if m not in tabuleiro.movimentos_disponiveis():
                print u"Movimento Inválido. Tente novamente."
            else:
                break
    
        tabuleiro.marcar(self.marca,m)

class RoboFacil(object):
    ''' Robo que joga aleatório '''
    
    def __init__(self, nome, marca):
        self.nome = u"IA Fácil %s" % nome
        self.marca = marca
        
        if self.marca == 'O':
            self.oponente = 'X'
        else:
            self.oponente = 'O'
    
    def jogada(self, tabuleiro):
        from random import choice
        
        tabuleiro.marcar( self.marca, choice( tabuleiro.movimentos_disponiveis() ) )
        
class Robo(object):
    '''Robozinho'''
    
    def __init__(self, nome, marca):
        self.nome = "IA %s" % nome
        self.marca = marca
        
        self.inicio = 0
        self.turno = 0
        
        if self.marca == 'O':
            self.oponente = 'X'
        else:
            self.oponente = 'O'
        
    def jogada(self, tabuleiro):
        self.turno += 1
        
        if tabuleiro.turno() == 1:
            self.inicio = 1
            
        if self.inicio:
            if self.turno == 1:
                tabuleiro.marcar( self.marca, 4)
                return True
                
            if self.turno == 2:
                if self.oponente in [tabuleiro.tabuleiro[1], tabuleiro.tabuleiro[3], tabuleiro.tabuleiro[5], tabuleiro.tabuleiro[7]]:
                    tabuleiro.marcar( self.marca, 2)
                else:
                    tabuleiro.marcar( self.marca, 1)
                
                return True
                    
            if self.turno >= 3:
                if tabuleiro.pode_ganhar(self.marca):
                   tabuleiro.marcar( self.marca, tabuleiro.pode_ganhar(self.marca))
                elif tabuleiro.pode_ganhar(self.oponente):
                   tabuleiro.marcar( self.marca, tabuleiro.pode_ganhar(self.oponente))
                else:
                   tabuleiro.marcar(self.marca, self.jogada_aleatoria(tabuleiro))   

            return True   

        else:
            if self.turno == 1:
              if tabuleiro.tabuleiro[4] == '-':
                  self.inicio = 1
                  tabuleiro.marcar(self.marca, 4)
                  return True
              else:
                  tabuleiro.marcar(self.marca, 6)
                  self.inicio = 1
                  self.turno = 2
                  return True
 
            
        tabuleiro.marcar(self.marca, self.jogada_aleatoria(tabuleiro))
                    
            
                    
    def jogada_aleatoria(self, tabuleiro):
        from random import choice
        return choice(tabuleiro.movimentos_disponiveis())
                    
                    
                                    

if __name__ == '__main__':
    jogo=Jogo()     
    jogador2 = RoboFacil(u"Henrique", "X")
    jogador1 = Robo(u"João", "O")
    
    jogo.jogar( jogador2, jogador1)
