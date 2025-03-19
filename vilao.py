from personagem import Personagem 
from registro import Registro 

class Vilao(Personagem, Registro):
    def __init__(self, nome, vida, habilidades):
        self.nome = nome
        self.vida = vida
        self.habilidades = habilidades
        viloes = {nome:[habilidades, vida]}
        self.viloes = viloes


    def ataque(self, personagem):
        mensagem = f'{self.nome} atacou {personagem.nome}!'
        print(mensagem)
        Registro.registrar(mensagem)
        personagem.downgrade_vida()

    def defesa(self):
        mensagem = f'{self.nome} tomou elixir'
        print(mensagem)
        Registro.registrar(mensagem)
        self.upgrade_vida()

    def __str__(self):
        return f'Vilão: {self.nome}, Vida: {self.vida}, Habilidades: {self.habilidades}'
