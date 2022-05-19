from random import choice
from constants import CARACTERE_ESCONDIDO, CINCO_ERROS, DERROTA, DESISTIR, DIRETORIO, DOIS_ERROS, ESCOLHA_LETRA, ESCOLHA_PALPITE, JA_USADA, MODO_COMP_HUMANO, OPCOES_EM_JOGO, PEDIR_LETRA, PEDIR_PALPITE, QUATRO_ERROS, RESPOSTA, SEIS_ERROS, TENTATIVAS, TOPO, TRES_ERROS, UM_ERRO, VITORIA, ZERO_ERROS, TEMAS_DISPONIVEIS, TENTATIVAS


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


def verificaVitoria(palavraEscolhida: str, palavraOcultada: str) -> bool:
    if palavraEscolhida == palavraOcultada:
        return True
    return False


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


def geraTentativas(tentativasAtual: str, letra: str) -> str:
    tentativasAtual = tentativasAtual + "  " + letra
    return tentativasAtual


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


def jogoForca(palavra: str, tema: str, modoDeJogo: str):
    erros = 0
    letrasTentadas = ""

    if modoDeJogo == MODO_COMP_HUMANO:
        tema = escolheTema()
        palavra = escolhePalavra(tema)

    palavraOcultada = ocultaPalavra(palavra)
    palavraOcultada = atualizaPalavra(palavra, palavraOcultada, "-")
    palavraOcultada = atualizaPalavra(palavra, palavraOcultada, ".")

    while True:
        base = geraBase(palavraOcultada)
        print(TENTATIVAS + letrasTentadas) 

        print(f"========== {tema} ==========")
        print(TOPO)
        print(geraForca(erros))
        print(base)
        
        #aqui começa as ações possivei no jogo
        opcaoJogo = input(OPCOES_EM_JOGO)

        if opcaoJogo == ESCOLHA_LETRA:
            chuteLetra = input(PEDIR_LETRA).upper().strip()

            if chuteLetra[0] in letrasTentadas:
                print(JA_USADA)
            elif verificaLetra(palavra, chuteLetra[0]):
                palavraOcultada = atualizaPalavra(palavra, palavraOcultada, chuteLetra[0])
            else:
                erros = erros + 1

            if not(chuteLetra[0] in letrasTentadas):
                letrasTentadas = geraTentativas(letrasTentadas, chuteLetra[0])

        elif opcaoJogo == ESCOLHA_PALPITE:
            chutePalpite = input(PEDIR_PALPITE)

            if verificaPalpite(palavra, chutePalpite):
                print(VITORIA)
                break
            else:
                erros = erros + 1

        elif opcaoJogo == DESISTIR:
            print(DERROTA)
            print(RESPOSTA + palavra)
            break
        
        #finaliza jogo em caso de derrota
        if erros == 6:
            print(DERROTA)
            print(RESPOSTA + palavra)
            break

        if verificaVitoria(palavra, palavraOcultada):
            print(VITORIA)
            print(RESPOSTA + palavra)
            break


if __name__ == "__main__":
    any = True
