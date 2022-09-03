import mesa

from utils import *


class AgentePraga(mesa.Agent):
    """
        Agente Praga, o qual simula a praga que se move aleatoriamente
    """
    def __init__(self, pos, modelo, tipo):
        """
        Criando um agente praga.
    
        Args:
            unique_id: Identificador do agente único.
            x, y: Posição inicial do agente.
            tipo: Indicador do tipo do agente
        """
        super().__init__(pos, modelo)
        self.pos = pos
        self.tipo = tipo

    def step(self):
        self.operate()
        self.advance()
    
    def operate(self) -> None:
        """
        Executa a ação do agente
        """
        # Move apenas se houver um resitente ao seu redor
        for vizinho in self.model.grid.iter_neighbors(self.pos, True):
            tipoVizinho = vizinho.tipo.replace('Resistente', '')
            tipoAtual = self.tipo.replace('Praga', '')

            if tipoVizinho == tipoAtual:
                self.advance()


    def advance(self) -> None:
        try:
            self.model.grid.move_to_empty(self)
        except Exception as e:
            print('Erro ao mover agente resistente')
            pass