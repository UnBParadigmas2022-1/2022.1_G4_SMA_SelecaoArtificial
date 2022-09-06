"""
    Funções auxiliares para verificar posições para os Agentes
"""

# Gabriel B.

def posicaoVazia(self, posicoes_ocupadas):
    x = self.random.randrange(self.grid.width)
    y = self.random.randrange(self.grid.height)
    pos = (x, y)

    # Verifica se a posição já está ocupada
    while posicaoJaExiste(pos, posicoes_ocupadas):
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        pos = (x, y)

    return pos


def posicaoJaExiste(pos, lista):
    for item in lista:
        if item == pos:
            return True
    return False
