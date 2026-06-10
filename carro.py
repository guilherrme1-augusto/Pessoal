class Carro:
    """Representa um carro com controle de velocidade."""

    def __init__(self, marca):
        ...
        self.marca = marca
        self.velocidade = 0

    def acelerar(self, valor):
        self.velocidade += valor

    def frear(self, valor):
        if self.velocidade - valor < 0:
            self.velocidade = 0
        else:
            self.velocidade -= valor

    def mostrar_velocidade(self):
        print(f'{self.marca}: {self.velocidade} km/h')

c1 = Carro("Fiat")
c1.acelerar(70)
c1.frear(100)
c1.mostrar_velocidade()
