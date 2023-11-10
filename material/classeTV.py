class TV:
    def __init__(self, tamanho: int):
        self.cor = "preta"
        self.ligada = False
        self.tamanho = tamanho
        self.canal = "Prime"
        self.volume = 10

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal


tv_sala = TV(55)
tv_quarto = TV(40)

tv_quarto.mudar_canal("Netflix")

print(tv_sala.tamanho)
print(tv_quarto.canal)
