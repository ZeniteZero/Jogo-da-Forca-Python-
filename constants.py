#--------------Modos de Jogo--------------#
MODO_COMP_HUMANO = "1"
MODO_HUMAN_HUMAN = "2"
ENCERRAR = "3"

#--------------Mensagens de Erro--------------#
ERRO_ESCOLHA = f"\nEssa opção não está no jogo!!\nEscolha [{MODO_COMP_HUMANO}] para o modo Computador X Humano,[{MODO_HUMAN_HUMAN}] para o modo Humano X Humano oou \n[{ENCERRAR} para encerrar o jogo."

#--------------Regras de Jogo--------------#
MAX_ERROS = 6
TEMAS_DISPONIVEIS = ["FRUTAS", "OBJETOS", "PLANETAS", "FLORES", "PAISES", "ESTADOS(BRASIL)", "CAMPEOES(LOL)", "COMIDAS"]
DIRETORIO = f"temes\\\\"
CARACTERE_ESCONDIDO = "_"
ESCOLHA_LETRA = "1"
ESCOLHA_PALPITE = "2"
DESISTIR = "3"

#--------------Forcas--------------#
TOPO = f" _________"
ZERO_ERROS = f"║\n║\n║\n║\n║\n║"
UM_ERRO = f"║         |\n║         O\n║\n║\n║\n║"
DOIS_ERROS = f"║         |\n║       __O\n║\n║\n║\n║" 
TRES_ERROS = f"║         |\n║       __O__\n║\n║\n║\n║"
QUATRO_ERROS = f"║         |\n║       __O__\n║         |\n║\n║\n║"
CINCO_ERROS = f"║         |\n║       __O__\n║         |\n║        /\n║\n║"
SEIS_ERROS = f"║         |\n║       __O__\n║         |\n║        / \\\n║\n║"

#--------------Mensagens--------------#
OPCOES_TIPO_DE_JOGO = f"\nESCOLHA O MODO DE JOGO:\n[{MODO_COMP_HUMANO}] Computador vs Humano\n[{MODO_HUMAN_HUMAN}] Humano vs Humano\n[{ENCERRAR}] Encerrar o jogo\n"
OPCOES_EM_JOGO = f"[1] Dizer uma letra\n[2] Dar palpite\n[3] Desistir\n"
JA_USADA = f"\nEssa letra já foi usada!!\n"

TENTATIVAS = f"\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \nVocê já tentou:"

DERROTA = f"\n \n \n \n \n║------------║ VOCÊ PERDEU!!!!!!! ║------------║\n \n \n \n \n"
VITORIA = f"\n \n \n \n \n║------------║ PARABÉNS, VOCÊ VENCEU!!! ║------------║\n \n \n \n \n"
RESPOSTA = f"A resposta era: "

PEDIR_LETRA = f"Escreva a Letra: "
PEDIR_PALPITE = f"Digite seu palpite: "
PEDIR_PALAVRA = f"Pense em uma palavra: "
PEDIR_TEMA = f"Escolha um tema para a sua palavra: "
