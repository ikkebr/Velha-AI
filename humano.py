#*-* encoding: iso-8859-1 *-*

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