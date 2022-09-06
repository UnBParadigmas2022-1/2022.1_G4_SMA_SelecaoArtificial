import mesa

from utils import *

# Ricardo

class AgenteResistente(mesa.Agent):
    """
    Agente com fator de resistência, o qual perde menos pontos em relação ao ambiente que se encontra,
    ao encontrar uma praga que se identifica com sua resistência, não perde pontos e se move
    caso a praga seja diferente 
    """

    def __init__(self, pos, modelo, tipo, vida):
        """
        Criando um agente resistente.

        Args:
           unique_id: Identificador do agente unico.
           x, y: Posição inicial do agente.
           tipo: Indicador do tipo do agente
        """
        super().__init__(pos, modelo)
        self.pos = pos
        self.tipo = tipo #fomeResistente
        self.vida = {
            'fome': vida,
            'radiacao': vida,
            'doenca': vida,
            'frio': vida,
            'calor': vida,
            'toxico': vida
        }


    def step(self):
        """
            Um agente resistente perde apenas
            quando tiver algum agente diferente
            da sua resistência ao redor.
        """
        self.operate()

# Ítalo A. 

    def operate(self) -> None:
        """
        Executa a ação do agente
        """
        for vizinho in self.model.grid.iter_neighbors(self.pos, True):
            tipoVizinho = vizinho.tipo.replace('Praga', '')
            tipoAtual = self.tipo.replace('Resistente', '')

            if tipoVizinho != tipoAtual:

                self.vida[tipoAtual] -= 1

                if self.vida[tipoAtual] <= 0 and self.pos != None:
                    self.model.grid.remove_agent(self)
                    self.model.schedule.remove(self)
                else:
                    self.advance()

    def advance(self) -> None:
        """
        Move o agente para uma posição vazia
        """
        if self.pos != None:
            posicoes_ocupadas = [agente.pos for agente in self.model.schedule.agents]
            pos = posicaoVazia(self.model, posicoes_ocupadas)
            self.model.grid.move_agent(self, pos)
