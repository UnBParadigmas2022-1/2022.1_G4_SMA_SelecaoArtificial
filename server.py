import mesa
from Modelo import Modelo

cores = {
    "fome": "#FF0000",
    "radiacao": "#0000FF",
    "doenca": "#00FF00",
    "frio": "#000000",
    "calor": "#FFFF00",
    "toxico": "#FF00FF"
}

def vidaMediaResistentes(model):
    """
    Display a text count of how many happy agents there are.
    """
    resistentes = [a for a in model.schedule.agents if 'Resistente' in a.tipo]

    vidaTotal = 0
    vidaTotalAgente = 0
    tamCaracteristica = 1
    for a in resistentes:
        vidaTotalAgente = 0
        for v in a.vida.values():
            vidaTotalAgente += v
        tamCaracteristica = len(a.vida)
        vidaTotal += vidaTotalAgente / tamCaracteristica

    try:
        mediaVida = vidaTotal//len(resistentes)
    except ZeroDivisionError:
        mediaVida = vidaTotalAgente / tamCaracteristica

    # Parar a simulação quando a média de vida dos resistentes for menor que 0
    if len(resistentes) <= 0:
        model.running = False

    return f"Vida média dos resistentes: {mediaVida}"

def quantidadeResistentes(model):
    """
    Display a text count of how many happy agents there are.
    """
    resistentes = [a for a in model.schedule.agents if 'Resistente' in a.tipo]
    return f"Quantidade de resistentes: {len(resistentes)}"


def modelo_desenho(agent):
    """
    Portrayal Method for canvas
    """
    if agent is None:
        return
    
    if 'Resistente' in agent.tipo:
        portrayal = {"Shape": "circle",
                     "Filled": "true",
                     "r": 0.8,
                     "Layer": 0,
                     "Color": cores[agent.tipo.replace('Resistente', '')],
                     "text": agent.tipo[:2].upper(),
                     "text_color": "Black"}
    else:
        portrayal = {"Shape": "rect",
                     "Filled": "true",
                     "w": 0.8,
                     "h": 0.8,
                     "Layer": 0,
                     "Color": cores[agent.tipo.replace('Praga', '')],
                     "text": agent.tipo[:2].upper(),
                     "text_color": "Black"}

    return portrayal