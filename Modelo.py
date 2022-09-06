import mesa

from AgentePraga import AgentePraga
from AgenteResistente import AgenteResistente
from utils import *

# Ítalo V.
def totalCaracteristica(model, caracteristica):
    """
    Retorna a soma de todos os valores de uma característica
    """
    resistentes = [a for a in model.schedule.agents if 'Resistente' in a.tipo]

    total = len(list(filter(lambda x: caracteristica in x.tipo , resistentes)))
    
    return total

# Modelo que simula todos os agentes pragas e agentes resistentes
class Modelo(mesa.Model):
    def __init__(self, num_resistentes, num_pragas, width, height, vida):
        self.num_agentes_resistentes = num_resistentes
        self.num_agentes_pragas = num_pragas
        self.grid = mesa.space.MultiGrid(width, height, torus=False)
        self.schedule = mesa.time.RandomActivation(self)
        self.running = True

        self.datacollector = mesa.datacollection.DataCollector(
            model_reporters={"Fome": lambda m: totalCaracteristica(m, 'fome'), "Radiação": lambda m: totalCaracteristica(m, 'radiacao'), "Doença": lambda m: totalCaracteristica(m, 'doenca'), "Frio": lambda m: totalCaracteristica(m, 'frio'), "Calor": lambda m: totalCaracteristica(m, 'calor'), "Tóxico": lambda m: totalCaracteristica(m, 'toxico')},
            agent_reporters={"Tipo": lambda a: a.tipo, "Posicao": lambda a: a.pos},
        )

# Gabriel A.
        # Posições já ocupadas
        posicoes_ocupadas = []

        # Criando agentes resistentes
        for i in range(self.num_agentes_resistentes):
            # Posição aleatória vazia
            pos = posicaoVazia(self, posicoes_ocupadas)
            posicoes_ocupadas.append(pos)

            tipo = self.random.choice(['fome', 'radiacao', 'doenca', 'frio', 'calor', 'toxico'])
            agente = AgenteResistente(pos, self, f'{tipo}Resistente', vida)
            self.schedule.add(agente)
            self.grid.place_agent(agente, pos)

        # Criando agentes pragas
        for i in range(self.num_agentes_pragas):
            # Posição aleatória vazia
            pos = posicaoVazia(self, posicoes_ocupadas)
            posicoes_ocupadas.append(pos)

            tipo = self.random.choice(['fome', 'radiacao', 'doenca', 'frio', 'calor', 'toxico'])
            agente = AgentePraga(pos, self, f'{tipo}Praga')
            self.schedule.add(agente)
            self.grid.place_agent(agente, pos)



    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()