import mesa

from AgentePraga import AgentePraga
from AgenteResistente import AgenteResistente
from utils import *


def totalCaracteristica(modelo, caracteristica):
    """
    Retorna a soma de todos os valores de uma característica
    """
    resistentes = [a for a in modelo.schedule.agents if 'Resistente' in a.tipo]

    total = len(list(filter(lambda x: caracteristica in x.tipo , resistentes)))
    
    return total

# Modelo que simula todos os agentes pragas e agentes resistentes
class Modelo(mesa.Model):
    def __init__(self, numResistentes, numPragas, largura, altura, vida):
        self.numAgentesResistentes = numResistentes
        self.numAgentesPragas = numPragas
        self.grid = mesa.space.MultiGrid(largura, altura, torus=False)
        self.schedule = mesa.time.RandomActivation(self)
        self.running = True

        self.datacollector = mesa.datacollection.DataCollector(
            modeloReporters={"Fome": lambda m: totalCaracteristica(m, 'fome'), "Radiação": lambda m: totalCaracteristica(m, 'radiacao'), "Doença": lambda m: totalCaracteristica(m, 'doenca'), "Frio": lambda m: totalCaracteristica(m, 'frio'), "Calor": lambda m: totalCaracteristica(m, 'calor'), "Tóxico": lambda m: totalCaracteristica(m, 'toxico')},
            agenteReporters={"Tipo": lambda a: a.tipo, "Posicao": lambda a: a.pos},
        )

        # Posições já ocupadas
        posicoesOcupadas = []

        # Criando agentes resistentes
        for i in range(self.numAgentesResistentes):
            # Posição aleatória vazia
            pos = posicaoVazia(self, posicoesOcupadas)
            posicoesOcupadas.append(pos)

            tipo = self.random.choice(['fome', 'radiacao', 'doenca', 'frio', 'calor', 'toxico'])
            agente = AgenteResistente(pos, self, f'{tipo}Resistente', vida)
            self.schedule.add(agente)
            self.grid.place_agent(agente, pos)

        # Criando agentes pragas
        for i in range(self.numAgentesPragas):
            # Posição aleatória vazia
            pos = posicaoVazia(self, posicoesOcupadas)
            posicoesOcupadas.append(pos)

            tipo = self.random.choice(['fome', 'radiacao', 'doenca', 'frio', 'calor', 'toxico'])
            agente = AgentePraga(pos, self, f'{tipo}Praga')
            self.schedule.add(agente)
            self.grid.place_agent(agente, pos)



    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()