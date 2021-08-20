"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome :Renan de Souza Luiz
  NUSP :9836120
  Turma:09
  Prof.:Daniel Batista

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
  
  Exemplo:
  - O algoritmo Quicksort foi baseado em
  http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html
"""

# as constantes que podem ser usadas estão em constantes.py
# para usá-las não é necessário escrever "constantes."
from constantes import * 

# os métodos da classe Labirinto poderão ser usados:
#    dimensao(), get(), put(), direcoes_possiveis(), matriz(), ... 
from labirinto import *

# os métodos da classe Pacman poderão ser usados:
#    posicao(), direcao(), morra(), reposicione(), mova(), ... 
from pacman import * 

# os métodos da classe Fantasma poderão ser usados:
#    posicao(), direcao(), ... 
from fantasma import *

#--------------------------------------------------------------------------
class Console:
    ''' Classe responsável por exibir ao usuário o labirinto junto com 
        o Pac-Man, fantasmas e pacdots.

    Um console é uma unidade que permite que um operador se comunique com 
    um sistema de computador. No caso, a classe Console será responsável pela
    comunicação com o jogador.

    Em uma aplicação gráfica, esta classe seria a responsável por desenhar 
    o "mundo" do jogo.  

    Um objeto dessa classe possui três atributos de estado:

        * `pac_man`: referência (apelido) para um objeto da 
               classe Pacman que representa o Pac-Man do jogo.

        * `fantasmas`: referência (apelido) para uma lista de objetos 
               da classe Fantasma que representam os fantasmas do jogo.

        * `lab`: referência (apelido) para um objeto da classe
               Labirinto que representa o labirinto do jogo;

    ''' 
    def __init__(self, pac_man, fantasmas, lab):
        '''(Console, Pacman, lista de Fantasma, Labirinto) -> None

        Construtor: recebe referências:

            - `self`      para o objeto Console que está sendo construído;
            - `pac_man`   para um objeto da classe Pacman;
            - `fantasmas` para uma lista de objetos da classe Fantasma; e
            - `lab`       para um objeto da classe Labirinto. 

        O método cria e retorna um objeto da classe Console.

        Atenção: self.pac_man, self.fantasmas e self.lab são apelidos dos 
            parâmetros e __não__ clones.

        Método mágico/especial: usado pelo Python quando criamos
            escrevemos Console(). Não tem `return`.
        '''
        self.pac_man=pac_man
        self.fantasmas=fantasmas
        self.lab=lab
        print("Console.__init__(): criado um console:")
        print("Console.__init__(): pac_man: Pacman: posição [%d][%d], direção '%s', pontos %d, vidas %d"%(self.pac_man.lin,self.pac_man.col,self.pac_man.dir,self.pac_man.pts,self.pac_man.vidas))
        p=0
        while p<len(self.fantasmas):
            print("Console.__init__(): fantasma:",self.fantasmas[p])
            p+=1
      
        print("Console.__init__(): lab:\n%s"%(self.lab))
    #-------------------------------------------------------------------     
    def __str__(self):
        '''(Console) -> str

        Recebe uma referência a um objeto da classe Console e 
        cria e retorna um string que representa o Console:

           um labirinto com suas paredes, pacdots, vazios, 
           fantasmas e Pac-Man.

        Sugestões: 
           - inspire-se na sua função imprimeLabirinto() do EP2 
           - se você achar necessário, lembre-se do método matriz() 
             do objeto lab (classe Labirinto) 
        '''
        copia_lab=self.lab.matriz()
        copia_lab[self.pac_man.lin][self.pac_man.col]='C'
        p=0
        while p<len(self.fantasmas):
            copia_lab[self.fantasmas[p].lin][self.fantasmas[p].col]='F'
            if self.pac_man.lin==self.fantasmas[p].lin and self.pac_man.col==self.fantasmas[p].col:
                copia_lab[self.pac_man.lin][self.pac_man.col]='X'
            p+=1
            
        texto=''
        for i in range(len(copia_lab)):
            for j in range(len(copia_lab[0])):
                texto+=copia_lab[i][j]
                
            texto+='\n'
                
            
            
        return texto
        
        
        
        
         
#-----------------------------------------------------------------           
# AREA RESERVADA
#
# Escreva a seguir as suas possíveis funções auxiliares
