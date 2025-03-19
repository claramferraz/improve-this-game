from vilao import Vilao
from heroi import Heroi
from personagem import Personagem
from ataques import Luta
from registro import Registro

def main():
    # Criando personagens e vilões
    heroi = Heroi('Iron Man', 120, ['Voo', 'Armas', 'Genialidade'])
    vilao = Vilao('Thanos', 120, ['Força sobre-humana', 'Telepatia', 'Telecinese'] )
    historico = []

    # Mostrando personagens
    print(heroi)
    print(vilao)

    # Ataque vilão e herói
    Luta.batalha(vilao, heroi)
    Registro.exibir_historico(historico)


if __name__ == "__main__":
    main()
