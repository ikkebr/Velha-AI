#*-* encoding: iso-8859-1 *-*

class RoboMedio(object):
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