from random import choice
from constants import CARACTERE_ESCONDIDO, CINCO_ERROS, DERROTA, DESISTIR, DIRETORIO, DOIS_ERROS, ESCOLHA_LETRA, ESCOLHA_PALPITE, OPCOES_EM_JOGO, PEDIR_LETRA, PEDIR_PALPITE, QUATRO_ERROS, SEIS_ERROS, TOPO, TRES_ERROS, UM_ERRO, VITORIA, ZERO_ERROS, TEMAS_DISPONIVEIS


def escolheTema() -> str:
    return choice(TEMAS_DISPONIVEIS)


def escolhePalavra(temaEscolhido: str) -> str:
    with open(DIRETORIO + temaEscolhido + ".txt", "r") as file:
        opcoesPalavras = file.readlines()
        return choice(opcoesPalavras).strip()

    
def ocultaPalavra(palavraEscolhida: str) -> str:
    palavraOculta = ""
    for i,j in enumerate(palavraEscolhida):
        palavraOculta = palavraOculta + CARACTERE_ESCONDIDO
    return palavraOculta


def verificaLetra(palavraEscolhida: str, letra: str) -> bool:
    letra = letra.strip().upper()
    if letra in palavraEscolhida:
        return True
    return False


def verificaPalpite(palavraEscolhida: str, palpite: str) -> bool:
    palpite = palpite.strip().upper()
    for indice, caractere in enumerate(palavraEscolhida):
        if palavraEscolhida[indice] != palpite[indice]:
            return False
    return True


def geraBase(palavraEscondida: str) -> str:
    base = "║"
    for caractere in palavraEscondida:
        base = base + " " + caractere + " "
    return base


def atualizaPalavra(palavraEscolhida: str, palavraOculta: str, letra: str) -> str:
    letra = letra.strip().upper()
    novaPalavra = ""

    for indice, caractere in enumerate(palavraEscolhida):
        if caractere == letra:
            novaPalavra = novaPalavra + letra
        elif caractere in palavraOculta:
            novaPalavra = novaPalavra + palavraOculta[indice]
        else:
            novaPalavra = novaPalavra + CARACTERE_ESCONDIDO
    
    return novaPalavra


def geraForca(erros: int) -> str:

    if erros == 0:
        return ZERO_ERROS
    elif erros == 1:
        return UM_ERRO
    elif erros == 2:
        return DOIS_ERROS
    elif erros == 3:
        return TRES_ERROS
    elif erros == 4:
        return QUATRO_ERROS
    elif erros == 5:
        return CINCO_ERROS
    elif erros == 6:
        return SEIS_ERROS


def jogoComputadorHumano():
    erros = 0
    tema = escolheTema()
    palavra = escolhePalavra(tema)
    palavraOcultada = ocultaPalavra(palavra)

    while True:
        base = geraBase(palavraOcultada)

        print(f"========== {tema} ==========")
        print(TOPO)
        print(geraForca(erros))
        print(base)
        
        #aqui começa as ações possivei no jogo
        opcaoJogo = input(OPCOES_EM_JOGO)

        if opcaoJogo == ESCOLHA_LETRA:
            chuteLetra = input(PEDIR_LETRA)

            if verificaLetra(palavra, chuteLetra):
                palavraOcultada = atualizaPalavra(palavra, palavraOcultada, chuteLetra)
            else:
                erros = erros + 1

        elif opcaoJogo == ESCOLHA_PALPITE:
            chutePalpite = input(PEDIR_PALPITE)

            if verificaPalpite(palavra, chutePalpite):
                print(VITORIA)
                break
            else:
                erros = erros + 1

        elif opcaoJogo == DESISTIR:
            print(DERROTA)
            break
        
        #finaliza jogo em caso de derrota
        if erros == 6:
            print(DERROTA)
            break


def jogoHumanoHumano(palavra, tema):
    erros = 0
    palavraOcultada = ocultaPalavra(palavra)

    while True:
        base = geraBase(palavraOcultada)

        print(f"========== {tema} ==========")
        print(TOPO)
        print(geraForca(erros))
        print(base)
        
        #aqui começa as ações possivei no jogo
        opcaoJogo = input(OPCOES_EM_JOGO)

        if opcaoJogo == ESCOLHA_LETRA:
            chuteLetra = input(PEDIR_LETRA)

            if verificaLetra(palavra, chuteLetra):
                palavraOcultada = atualizaPalavra(palavra, palavraOcultada, chuteLetra)
            else:
                erros = erros + 1

        elif opcaoJogo == ESCOLHA_PALPITE:
            chutePalpite = input(PEDIR_PALPITE)

            if verificaPalpite(palavra, chutePalpite):
                print(VITORIA)
                break
            else:
                erros = erros + 1

        elif opcaoJogo == DESISTIR:
            print(DERROTA)
            break
        
        #finaliza jogo em caso de derrota
        if erros == 6:
            print(DERROTA)
            break


if __name__ == "__main__":
    any = True