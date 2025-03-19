class Registro():
    historico = []

    def registrar(mensagem):
        Registro.historico.append(mensagem)

    def exibir_historico(self):
        historico_jogo = ('HISTÓRICO JOGO')
        print(historico_jogo.center(50, '*'))

        for evento in Registro.historico:
            print(evento)

