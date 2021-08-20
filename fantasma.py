# as constantes que podem ser usadas estão em constantes.py
# para usá-las não é necessário escrever "constantes."
from constantes import *  

# os métodos da classe Labirinto poderão ser usados:
#    dimensao(), get(), put(), direcoes_possiveis(), ... 
from labirinto import *

# módulo para definição da semente para sorteio dos números pseudo
# aleatórios; usada para sortear um movimento possível para um fantasma
import random # random.randrange(), random.choice() 

# descomente a linha a seguir se você usa alguma função do módulo extras
# import extras

#----------------------------------------------------------------------
class Fantasma:
    ''' Classe utilizada para representar um fantasma.

    Cada objeto desta classe tem 4 atributos de estado:
       `lin`, `col`, `direcao` e `lab`:

       * `lin` e `col`: inteiros que indicam a posição [lin][col] 
             do fantasma; 

       * `dir`: caractere (= str) em 'wasd' que indica a direção
             do último movimento do fantasma.

       * `lab`: referência (apelido) para um objeto da classe
               Labirinto que representa o labirinto do jogo;
               Cada posição do labirinto contém um dos caracteres
               em CARACTERES_LABIRINTO (= '+. ').
    '''         
    #--------------------------------------------------------------
    def __init__(self, lin, col, lab):
        '''(Fantasma, int, int, Labirinto) -> None

        Construtor: recebe inteiros `lin`, `col` e referências/apelidos
          
            - `self`: para o objeto Fantasma que está sendo construído e
            - `lab` : para um objeto da classe Labirinto.

        O método cria e retorna um objeto que representa um fantasma.

        O fantasma criado ocupa a posição [lin][col] do labirinto.

        Inicialmente a sua direção deve ser sorteada dentre as direções 
        possíveis.

        Atenção: self.lab deve ser um apelido do parâmetro lab e 
            __não__ um clone.

        O método pode supor que sempre há uma direção possível para o
        fantasma.
        
        Sugestões:
            - para obter as direções possíveis use o método direcoes_possiveis()
              do objeto lab (classe Labirinto)
            - para o sorteio use random.choice(lista) que retorna
              um item sorteado da lista:

        >>> sorteado = random.choice(['a',2,True])
        >>> print(sorteado)
        True
        >>> sorteado = random.choice(['a',2,True])
        >>> print(sorteado)
        'a'
        >>> sorteado = random.choice(['a',2,True])
        >>> print(sorteado)
        'a'
        >>> sorteado = random.choice(['a',2,True])
        >>> print(sorteado)
        2
        >>> sorteado = random.choice(['a',2,True])
        >>> print(sorteado)
        'a'
        >>> 

        Método mágico/especial: usado pelo Python quando criamos
            escrevemos Pacman(). Não tem `return`.
        '''
        self.lab=lab
        self.lin=lin
        self.col=col
        direc_poss=self.lab.direcoes_possiveis(lin,col)
        sorteado = random.choice(direc_poss)
        
        self.dir=sorteado
        
        print("Fantasma.__init__():criado Fantasma: posição [%d][%d]"%(self.lin,self.col),",direção '%s'"%self.dir)
    #--------------------------------------------------------------        
    def __str__(self):
        '''(Fantasma) -> str

        Recebe um Fantasma referenciada por `self` e constrói e retorna 
        o string utilizado por print() para imprimir informações sobre
        o fantasma. 

        Esse também é o string retornado pela função nativa str().
        '''        
        return str("Fantasma: posição [%d][%d], direção '%s'"%(self.lin,self.col,self.dir))

    
    #--------------------------------------------------------------
    def posicao(self):
        '''(Fantasma) -> int, int

        Recebe um Fantasma referenciado por `self` e retorna dois inteiros 
        lin e col tais que o fantasma está na posição [lin][col].
        '''
        return self.lin,self.col

    
    #--------------------------------------------------------------
    def direcao(self):
        '''(Fantasma) -> str

        Recebe um Fantasma referenciado por `self` e retorna um símbolo
        em 'wasd' representando a direção do último movimento do fantasma.
        '''
        return self.dir   


        
    #--------------------------------------------------------------
    def mova(self):
        '''(Fantasma) -> None

        Recebe um Fantasma referenciado por `self` e move o fantasma 
        de acordo com as regras do EP2.

        O método pode supor que sempre há uma direção possível para o
        fantasma.

        Sugestão: inspire-se na sua função movimentaFantasmas() do EP2.
        '''
        n_lin,n_col=self.lab.dimensao()
        direc_poss=self.lab.direcoes_possiveis(self.lin,self.col)
        sor = random.choice(direc_poss)
        if sor=='w' and self.lin!=0:
            print("Fantasma.mova(): fantasma moveu-se de [%d][%d] para [%d][%d]"%(self.lin,self.col,self.lin-1,self.col))
            self.lin-=1
            
            
        elif sor=='w' and self.lin==0:
            print("Fantasma.mova(): fantasma moveu-se de [%d][%d] para [%d][%d]"%(self.lin,self.col,n_lin-1,self.col))
            self.lin=n_lin-1
            
        if sor=='s' and self.lin!=n_lin-1:
            print("Fantasma.mova(): fantasma moveu-se de [%d][%d] para [%d][%d]"%(self.lin,self.col,self.lin+1,self.col))
            self.lin+=1
            
        elif sor=='s' and self.lin==n_lin-1:
            print("Fantasma.mova(): fantasma moveu-se de [%d][%d] para [%d][%d]"%(self.lin,self.col,0,self.col))
            self.lin=0
        
        if sor=='a' and self.col!=0:
            print("Fantasma.mova(): fantasma moveu-se de [%d][%d] para [%d][%d]"%(self.lin,self.col,self.lin,self.col-1))
            self.col-=1
            
        elif sor=='a' and self.col==0:
            print("Fantasma.mova(): fantasma moveu-se de [%d][%d] para [%d][%d]"%(self.lin,self.col,self.lin,n_col-1))
            self.col=n_col-1
            
        if sor=='d' and self.col!=n_col-1:
            print("Fantasma.mova(): fantasma moveu-se de [%d][%d] para [%d][%d]"%(self.lin,self.col,self.lin,self.col+1))
            self.col+=1
            
        elif sor=='d' and self.col==n_col-1:
            print("Fantasma.mova(): fantasma moveu-se de [%d][%d] para [%d][%d]"%(self.lin,self.col,self.lin,0))
            self.col=0
            
            
            
            
            
            
        
            
            
            
            
            
                
        
            
            
        
