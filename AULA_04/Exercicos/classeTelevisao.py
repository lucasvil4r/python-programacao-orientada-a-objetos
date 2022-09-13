class Televisao:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume


    def aumentar_volume(self):
        self.volume += 1
        return self.volume

    def diminuir_volume(self):
        self.volume -= 1
        return self.volume

    def alterar_canal(self, novo_canal):
        self.canal = novo_canal
        return novo_canal

tv = Televisao(1, 0)
tv.alterar_canal(5)
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()
print(f'A tv está no canal {tv.canal}')             # A tv está no canal 5
print(f'A tv está no volume {tv.volume}')           # A tv está no volume 2
