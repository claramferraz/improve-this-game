class Personagem:

    def __init__(self, nome, idade, vida, habilidades):
        self.nome = nome
        self.idade = idade
        self.vida = int(vida)
        self.habilidades = habilidades

    def upgrade_vida(self):
        if self.vida < 120:
            self.vida += 20
            print(f'\nVida de {self.nome} após upgrade: {self.vida}')
        else:
            print('A vida do personagem está cheia')

    def downgrade_vida(self):
        if self.vida > 20:
            self.vida -= 20
        else:
            self.vida = 0
        print(f'\nVida de {self.nome} após downgrade: {self.vida}')

    def dialogar(self):
        if self.nome == 'Iron Man':
            frases = ['Sei que falei que não haveria mais surpresas, '
            'mas eu esperava conseguir fazer uma última', 'Tudo o que eu já fiz e faço é '
            'para proteger este mundo', 'Eu tenho um plano. Ataque']
            frases = frases
            if self.vida >= 120:
                print(self.nome, ':', frases[2].center(50))
            elif self.vida < 120 and self.vida > 40:
                print(self.nome, ':', frases[1].center(50))
            else:
                print(self.nome, ':', frases[0].center(50))
        else:
            frases = ['Devia ter arrancado minha cabeça', 'Eu sou inevitável', 
                      'Você tem meu respeito, Stark']
            frases = frases
            if self.vida >= 120:
                print(self.nome, ':', frases[0].center(50))
            elif self.vida < 120 and self.vida > 40:
                print(self.nome, ':', frases[2].center(50))
            else:
                print(self.nome, ':', frases[1].center(50))

    def update_nome(self, nome_editado):
        self.nome = nome_editado

    def __str__(self):
        return f'Personagem:{self.nome}, Idade:{self.idade}, Vida:{self.vida}, Habilidades:{self.habilidades}'
