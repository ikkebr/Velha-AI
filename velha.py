#*-* encoding: iso-8859-1 *-*

from humano import Humano
from robofacil import RoboFacil
from robomedio import RoboMedio

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

if __name__ == '__main__':
    jogo=Jogo()     
    jogador2 = RoboFacil(u"Henrique", "X")
    jogador1 = RoboMedio(u"João", "O")
    
    jogo.jogar( jogador2, jogador1)
