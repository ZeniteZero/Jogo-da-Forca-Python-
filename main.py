from constants import ENCERRAR, ERRO_ESCOLHA, MODO_COMP_HUMANO, MODO_HUMAN_HUMAN, OPCOES_TIPO_DE_JOGO, PEDIR_PALAVRA, PEDIR_TEMA
from functions import geraForca, jogoComputadorHumano, jogoHumanoHumano


if __name__ == '__main__':
    
    while True:
        modoDeJogo = input(OPCOES_TIPO_DE_JOGO)

        if modoDeJogo == MODO_COMP_HUMANO:
            jogoComputadorHumano()

        elif modoDeJogo == MODO_HUMAN_HUMAN:
            palavraEscolhida = input(PEDIR_PALAVRA)
            temaEscolhido = input(PEDIR_TEMA)

            jogoHumanoHumano(palavraEscolhida, temaEscolhido)

        elif modoDeJogo == ENCERRAR:
            break

        else:
            print(ERRO_ESCOLHA)
            