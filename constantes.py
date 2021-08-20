# NÃO ALTERE ESTE ARQUIVO

# CONSTANTES usadas para representar direções
# -------------------------------------------

# Caracteres ASCII usados para representar possíveis direções
# do movimento do ac-Man e dos fantasmas.
# Esses são as direcoes que podem ser digitadas pelo jogador.
#
#          ↑ 
#          w
#      ← a s d →
#          ↓
#
CIMA     = 'w' # ↑  
ESQUERDA = 'a' # ← 
BAIXO    = 's' # ↓ 
DIREITA  = 'd' # →
DIRECOES = CIMA + ESQUERDA + BAIXO + DIREITA

# usado apenas inicialmente quando criamos um objeto da classe Pacman.
PARADO   = 'p' 

# CONSTANTES em ASCII usadas no EP2 e que podem ser usadas no EP3
# --------------------------------------------------------------

PACMAN    = 'C'  
FANTASMA  = 'F'  
COLISAO   = 'X'
PAREDE    = '+'
VAZIO     = ' '  
PACDOT    = '.'

# string com caracteres que podem aparecer inicialmente em um labirinto
CARACTERES_VALIDOS   = VAZIO + PACDOT + PAREDE + FANTASMA + PACMAN

# string com os caracteres que podem aparecer em um labirinto após
# os caracteres PACMAN e FANTASMA terem sido removidos
CARACTERES_LABIRINTO = VAZIO + PACDOT + PAREDE

