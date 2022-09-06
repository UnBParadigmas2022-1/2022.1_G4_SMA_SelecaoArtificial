import mesa
from Modelo import Modelo

# Guilherme

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

# Ian

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
                     "text": agent.tipo[:2].upper(), # Texto
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


canvas_elementos = mesa.visualization.CanvasGrid(modelo_desenho, 20, 20, 500, 500)
fome_grafico = mesa.visualization.ChartModule([{"Label": "Fome", "Color": cores['fome']}])
radiacao_grafico = mesa.visualization.ChartModule([{"Label": "Radiação", "Color": cores['radiacao']}])
doenca_grafico = mesa.visualization.ChartModule([{"Label": "Doença", "Color": cores['doenca']}])
frio_grafico = mesa.visualization.ChartModule([{"Label": "Frio", "Color": cores['frio']}])
calor_grafico = mesa.visualization.ChartModule([{"Label": "Calor", "Color": cores['calor']}])
toxico_grafico = mesa.visualization.ChartModule([{"Label": "Tóxico", "Color": cores['toxico']}])


model_params = {
    # Slidebar
    "num_resistentes": mesa.visualization.Slider(
        name="Número de resistentes",
        min_value=0,
        max_value=40,
        step=1,
        value=30,
    ),
    "num_pragas": mesa.visualization.Slider(
        name="Número de pragas",
        min_value=0,
        max_value=40,
        step=1,
        value=10,
    ),
    "vida": mesa.visualization.Slider(
        name="Vida",
        min_value=0,
        max_value=50,
        step=1,
        value=20,
    ),
    "width": 20,
    "height": 20,
}

server = mesa.visualization.ModularServer(
    Modelo,
    [
        canvas_elementos,
        vidaMediaResistentes,
        quantidadeResistentes,
        fome_grafico,
        radiacao_grafico,
        doenca_grafico,
        frio_grafico,
        calor_grafico,
        toxico_grafico,
    ],
    "Seleção artificial",
    
    model_params,
)
