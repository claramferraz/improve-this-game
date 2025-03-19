from personagem import Personagem
from registro import Registro

class Heroi(Personagem, Registro):

    def __init__(self, nome, vida, habilidades):
        self.nome = nome
        self.vida = vida
        self.habilidades = habilidades
        herois= {nome:[habilidades, vida]}
        self.herois = herois

    def ataque(self, personagem):
        mensagem =f'{self.nome} atacou {personagem.nome}!'
        print(mensagem)
        Registro.registrar(mensagem)
        personagem.downgrade_vida()

    def ataque_final(self, personagem):
        mensagem = f'{self.nome} matou {personagem.nome}'
        print(mensagem)
        Registro.registrar(mensagem)
    
    def defesa(self):
        mensagem = f'{self.nome} recarregou a armadura'
        print(mensagem)
        Registro.registrar(mensagem)
        self.upgrade_vida()


    def __str__(self):
        return f'\nHerói:{self.nome}, Vida:{self.vida}, Habilidades:{self.habilidades}'