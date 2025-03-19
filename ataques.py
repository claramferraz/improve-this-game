from vilao import Vilao
from heroi import Heroi
from personagem import Personagem

class Luta(Vilao, Heroi, Personagem):
            
    def batalha(vilao, heroi):
        while vilao.vida > 20:
            heroi.dialogar()
            vilao.dialogar()
            vilao.ataque(heroi)

            if heroi.vida < 40 and heroi.vida > 0:
                heroi.defesa()
            
            contra_ataque = 'CONTRA-ATAQUE'
            print(contra_ataque.center(50, '*'))
            heroi.ataque(vilao)
            
        else:
            ultimato = 'ULTIMATO'
            print(ultimato.center(50,'*'))
            heroi.ataque_final(vilao)
                

            
        
