# Jogo-da-Forca-Python
  Um projeto simples de jogo da forca programado em python.

  A pasta "temes" possui arquivos de texto, onde estão as palavras que serão usadas no jogo. Cada linha é uma palavra sem caracteres especiais. Os espeaços foram substituidos por um hífen.

  Temos 2 modos de jogo. Um é Computador contra Humano, onde é usado arquivos de texto para armazenar as palavras, cujo os temas são os nomes dos prórpios arquivos. E também o modo Humano contra Humano onde uma pessoa pode escolher a palavra e o tema para que outra possa tentar adivinhar.

  É permitido apenas 6 erros.

  A busca dos arquivos temas.txt está adaptada para sistemas windows para alterar para um sistema linux é necessário:
  1 - abrir o arquivo constants.py
  2 - alterar a variável DIRETORIO para f"/temes"
