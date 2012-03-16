#*-* encoding: iso-8859-1 *-*

class RoboFacil(object):
    u''' Robo que joga aleatório '''
    
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