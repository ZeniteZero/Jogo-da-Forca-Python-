from constants import ENCERRAR, ERRO_ESCOLHA, MODO_COMP_HUMANO, MODO_HUMAN_HUMAN, OPCOES_TIPO_DE_JOGO, PEDIR_PALAVRA, PEDIR_TEMA
from functions import jogoForca


if __name__ == '__main__':
    
    while True:
        modoDeJogo = input(OPCOES_TIPO_DE_JOGO)

        if modoDeJogo == MODO_COMP_HUMANO:
            jogoForca("any", "any", MODO_COMP_HUMANO)

        elif modoDeJogo == MODO_HUMAN_HUMAN:
            palavraEscolhida = input(PEDIR_PALAVRA).strip().upper()
            temaEscolhido = input(PEDIR_TEMA).strip().upper()

            jogoForca(palavraEscolhida, temaEscolhido, MODO_HUMAN_HUMAN)

        elif modoDeJogo == ENCERRAR:
            break

        else:
            print(ERRO_ESCOLHA)
            
