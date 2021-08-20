"""
  Nome :Renan de Souza Luiz

"""
import random # para random.seed()

# as constantes que podem ser usadas estão em constantes.py
# para usá-las não é necessário escrever "constantes."
from constantes import * 

# módulo com a definição da classe Labirinto
# os métodos da classe Labirinto poderão ser usados:
#    dimensao(), get(), put(), direcoes_possiveis(), matriz(), ... 
from labirinto import *

# módulo com a definição da classe Pacman
# os métodos da classe Pacman poderão ser usados:
#    posicao(), direcao(), morra(), reposicione(),... 
from pacman import *

# módulo com a definição da classe Fantasma
# os métodos da classe Fantasma poderão ser usados:
#    posicao(), direcao(), mova(), ... 
from fantasma import *

# módulo com a definição da classe Console
# os métodos da classe Console poderão ser usados:
#    no caso, o métodos __str__() quando usamos print()
from console import *

# CONSTANTES
PROMPT = "Direção (w:cima, a:esquerda, s:baixo, d:direita, x:sair): "

# caractere que se digitado encerra a execução do programa
SAIR   = 'x'

#----------------------------------------------------------------------
#
#   M A I N 
#
#----------------------------------------------------------------------

#----------------------------------------------------------------------
def main():
    # NÃO MODIFIQUE AS LINHAS ABAIXO
    # ------------------------------
    semente = 0
    random.seed(semente)

    print("Bem-vindo ao bom e velho Come-come!")
    nome_do_arquivo = input("Digite o nome do arquivo do labirinto ou enter para o labirinto padrão: ")
    if nome_do_arquivo == '':
        nome_do_arquivo = "labirinto-original.txt"

    # leitura da configuração inicial do labirinto
    lab = Labirinto(nome_do_arquivo)

    # AGORA VOCÊ PODE MODIFICAR O MAIN
    # --------------------------------   
    pacman = crie_pacman(lab)
    fantasmas = crie_fantasmas(lab)
    no_pacdots = lab.no_pacdots()
    console = Console(pacman,fantasmas,lab)

    while pacman.no_vidas()>0 and pacman.pontos()<no_pacdots:
       
        print(console)
        i=0
        while i<len(fantasmas):
            fantasmas[i].mova()
            i+=1
        
        colisao=houve_colisao(pacman,fantasmas)
        if colisao==False:
            direc_pacman=input("Direção de movimento do pacman:")
            pacman.mova(direc_pacman)
        
        
        
        colisao=houve_colisao(pacman,fantasmas)
        if colisao==True:
            lin_antes,col_antes= pacman.posicao()
            novo_lab=lab.matriz()
            print(console)
            pacman.morra()
            print("Você perdeu a sua %da vida..."%(3-pacman.no_vidas()))
            if pacman.no_vidas()>0:
                posicao_invalida=True
                while posicao_invalida==True: 
                    novo_lin=int(input("Digite a linha  de onde quer recomeçar:"))
                    novo_col=int(input("Digite a coluna de onde quer recomeçar:"))
                    n_lin,n_col=lab.dimensao()
                    if novo_lin<n_lin and novo_col<n_col and lab.get(novo_lin,novo_col)==' ' and novo_lab[novo_lin][novo_col]!='X' and novo_lab[novo_lin][novo_col]!='F' :
                        print("main(): pacman mudou-se de [%d][%d] para [%d][%d]"%(lin_antes,col_antes,novo_lin,novo_col))
                        pacman.reposicione(novo_lin,novo_col)
                        posicao_invalida=False
                    
                    else:
                        print("Posição inválida. Digite uma nova posição, que tenha VAZIO.")
                    
            else:
                print("Terminou o jogo...  Você conseguiu %d pontos"%pacman.pontos())
                
        
                
        
        if lab.no_pacdots()==0:
            print(console)
            print("Você venceu!!!  Terminou o jogo com %d pontos e %d vidas!"%(pacman.pontos(),pacman.no_vidas()))
            
        
       
            
        
        
            
        
        
            
        
        
            
            
            
            
        
    
    

#----------------------------------------------------------------------
def crie_pacman(lab):
    '''(Labirinto) -> Pacman

    Recebe uma referência `lab` a um objeto da classe Labirinto.

    Percorre o labirinto em busca de um caractere PACMAN definido 
    no módulo constantes.py. Ao encontrar o caractere, a função o 
    substitui por VAZIO no labirinto, e cria e retorna um objeto 
    da classe Pacman que representa o Pac-Man.

    O objeto Labirinto __deve__ ser acessado apenas através dos métodos
    da sua classe, conforme a sua definição no módulo labirinto.py.

    Para criar um objeto Pacman veja a definição da sua classe no 
    módulo pacman.py.
    '''
    for i in range(len(lab.lab)):
        for j in range(len(lab.lab[0])):
            if lab.lab[i][j]=='C':
                lab.lab[i][j]=' '
                print("crie_pacman(): Pac-Man encontrado na posição [%d][%d]"%(i,j))                
                pacman=Pacman(i,j,lab)
   
                
    return pacman
                
    
            

#----------------------------------------------------------------------
def crie_fantasmas(lab):
    '''(Labirinto) -> lista de Fantasma

    Recebe uma referência `lab` a um objeto da classe Labirinto.

    Percorre o labirinto em busca de caracteres FANTASMA definidos no 
    módulo constantes.py. Ao encontrar um destes caracteres, a função 
    o substitui por um PACDOT no labirinto, cria um objeto da classe 
    Fantasma que representa esse fantasma e o acrescenta à lista que 
    será retornada pela função. 

    O objeto Labirinto __deve__ ser acessado apenas através dos métodos
    da sua classe, conforme a sua definição no módulo labirinto.py.

    Para criar um objeto Fantasma veja a definição da sua classe no 
    módulo fantasma.py.
    '''
    fantasmas=[]
    for i in range(len(lab.lab)):
        for j in range(len(lab.lab[0])):
            if lab.lab[i][j]=='F':
                lab.lab[i][j]='.'
                fant=Fantasma(i,j,lab)
                fantasmas.append(fant)
        
    return fantasmas
            
    
#----------------------------------------------------------------------
def houve_colisao(pac_man, fantasmas):
    '''(Pacman, lista de Fantasma) -> bool

    Recebe uma referência `pac_man` a um objeto da classe Pacman e
    uma lista `fantasmas` de referências a objetos da classe Fantasma.
    A função verifica se algum fantasma ocupa a mesma posição do Pac-Man,
    em caso afirmativo retorna True, do contrário retorna False. 
    '''
    p=0
    
    while p<len(fantasmas):
        if pac_man.lin==fantasmas[p].lin and pac_man.col==fantasmas[p].col:
            return True
        p+=1
        
    return False
            
        
        


#-----------------------------------------------------------------
# Início do espaço reservado para eventuais funções auxiliares
# usadas neste módulo
#



# fim do espaço reservado para eventuais funções auxiliares
# usadas neste módulo
#-----------------------------------------------------------------

# chamada da função main() deve ser a última linha do módulo    
main()
