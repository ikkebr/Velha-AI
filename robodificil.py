class RoboDificil(object):
    '''Robo bom com MinMax'''

    def __init__(self, nome, marca):
        self.marca = marca
        self.nome = nome

        if self.marca == 'X':
            self.oponente = 'O'
        else:
            self.oponente = 'X'

    def jogada(self, tabuleiro):
        posicao,score = self.maximized_move(tabuleiro)
        tabuleiro.marcar(self.marca, posicao)



    def maximized_move(self,gameinstance):
        ''' Find maximized move'''    
        bestscore = None
        bestmove = None

        for m in gameinstance.movimentos_disponiveis():
            gameinstance.marcar(self.marca, m)
        
            if gameinstance.terminou():
                score = self.get_score(gameinstance)
            else:
                move_position,score = self.minimized_move(gameinstance)
        
            gameinstance.reverter()
            
            if bestscore == None or score > bestscore:
                bestscore = score
                bestmove = m

        return bestmove, bestscore

    def minimized_move(self,gameinstance):
        ''' Find the minimized move'''

        bestscore = None
        bestmove = None

        for m in gameinstance.movimentos_disponiveis():
            gameinstance.marcar(self.oponente, m)
        
            if gameinstance.terminou():
                score = self.get_score(gameinstance)
            else:
                move_position,score = self.maximized_move(gameinstance)
        
            gameinstance.reverter()
            
            if bestscore == None or score < bestscore:
                bestscore = score
                bestmove = m

        return bestmove, bestscore

    def get_score(self,gameinstance):
        if gameinstance.terminou():
            if gameinstance.vencedor  == self.marca:
                return 1 # Won
            elif gameinstance.vencedor == self.oponente:
                return -1 # Opponent won
        return 0 # Draw
