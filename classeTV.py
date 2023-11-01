class TV:
    def __init__(self):
        self.cor = "preta"
        self.ligada = False
        self.tamanho = 55
        self.canal = "Prime"
        self.volume = 10

    def mudar_canal(self, canal):
        self.canal = canal


tv_sala = TV()
tv_quarto = TV()

tv_quarto.mudar_canal("Netflix")

print(tv_sala.cor)
print(tv_quarto.canal)
