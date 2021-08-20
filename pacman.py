# as constantes que podem ser usadas estão em constantes.py
# para usá-las não é necessário escrever "constantes."
from constantes import * 

# os métodos da classe Labirinto poderão ser usados:
#    dimensao(), get(), put(), direcoes_possiveis(), matriz(), ... 
from labirinto import *

# descomente a linha a seguir se você usa alguma função do módulo extras
# import extras

#-----------------------------------------------------------------
class Pacman():
    '''Classe utilizada para representar Pac-Mans.

    Cada objeto desta classe tem 6 atributos de estado: 
       `lin`, `col`, `dir`, `pts`, `vidas` e `lab`:

        * `lin` e `col`: inteiros que indicam a posição [lin][col] 
              do Pac-Man;

        * `dir`: caractere (= str) em 'wasdp' que indica a direção 
              do último movimento do Pac-Man.
              Inicialmente é 'p' (= PARADO).
 
        * `pts`: inteiro que indica o número de pac-dots comidos 
              pelo Pac-Man. 
              Inicialmente esse valor é zero.

        * `vidas`: inteiro que indica o número de vidas que restam ao
              Pac-Man. 
              Inicialmente esse valor é três.

        * `lab`: referência (apelido) para um objeto da classe
               Labirinto que representa o labirinto do jogo.
               Cada posição do labirinto contém um dos caracteres
               em CARACTERES_LABIRINTO (= '+. ').
    '''

    #--------------------------------------------------------------
    def __init__(self, lin, col, lab):
        '''(Pacman, int, int, Labirinto) -> None

        Construtor: recebe inteiros `lin`, `col` e referências/apelidos: 

            - `self`: para o objeto Pacman que está sendo construído e
            - `lab` : para um objeto da classe Labirinto.

        O método cria e retorna um objeto que representa um Pac-Man. 

        O Pac-Man criado ocupa a posição [lin][col] do labirinto e
            otem 0 pontos  

        Inicialmente a sua direção é 'p' (= PARADO) e o número de 
            vidas é três.

        Atenção: self.lab deve ser um apelido do parâmetro lab e 
            __não__ um clone.

        Método mágico/especial: usado pelo Python quando criamos
            escrevemos Pacman(). Não tem `return`.
        '''
        self.lab=lab
        self.lin=lin
        self.col=col
        self.pts=0
        self.vidas=3
        self.dir='p'
        print("Pacman.__init__(): criado Pacman: posição [%d][%d], direção '%s', pontos %d, vidas %d"%(self.lin,self.col,self.dir,self.pts,self.vidas))
        
    #--------------------------------------------------------------        
    def __str__(self):
        '''(Pacman) -> str

        Recebe um Pacman referenciado por `self` e constrói e retorna 
        o string com infomações sobre o Pac-Man.

        Método mágico/especial: usado pelo Python quando utilizamos 
            print() para exibir informações sobre o Pac-Man.
            Esse também é o string retornado pela função nativa str().
        '''
        
        return str("Pacman: posição [%d][%d],direção '%s',pontos %d,vidas %d"%(self.lin,self.col,self.dir,self.pts,self.vidas))
       
        
       
      
    
    #--------------------------------------------------------------
    def posicao(self):
        '''(Pacman) -> int, int

        Recebe um Pacman referenciado por `self` e retorna dois inteiros 
        lin e col tais que o Pac-Man está na posição [lin][col].
        '''
        return self.lin,self.col

    
    #--------------------------------------------------------------
    def direcao(self):
        '''(Pacman) -> str

        Recebe um Pacman referenciado por `self` e retorna um string
        representando a direção do último movimento do Pac-Man.
        '''
        return self.dir
    #--------------------------------------------------------------
    def pontos(self):
        '''(Pacman) -> int

        Recebe um Pacman referenciado por `self` e retorna o 
        número de pacdots comidos (= pontos) pelo Pac-Man.
        '''
        return self.pts

        
    #--------------------------------------------------------------
    def no_vidas(self):
        '''(Pacman) -> int

        Recebe um Pacman referenciado por `self` e retorna 
        o número de vidas que restam ao Pac-Man.
        '''
        return self.vidas

    #--------------------------------------------------------------
    def morra(self):
        '''(Pacman) -> None

        Recebe um Pacman referenciado por `self` e diminui de uma vida
        o número de vidas que restam ao Pac-Man.
        '''
        self.vidas-=1

    #--------------------------------------------------------------
    def reposicione(self, lin, col):
        '''(Pacman) -> None

        Recebe um Pacman referenciado por `self` e inteiros `lin` e
        `col` e reposiciona o Pac-Man na posição [lin][col].

        Pré-condição: o método supõe que a posicão [lin][col] do labirinto
            contém VAZIO. Isso não precisa ser verificado.
        '''
        self.lin=lin
        self.col=col
        
        
    #--------------------------------------------------------------
    def mova(self, direcao):
        '''(Pacman, str) -> None

        Recebe um Pacman referenciado por `self` e um string `direcao` 
        representando uma direção e, se possível, move o Pac-Man na 
        direção dada, atualizando seus pontos e o labirinto se necessário.
 
        O método imprime uma mensagem indicando se o movimento é possível
        ou não. Se o movimento é possível o método deve imprimir uma
        uma mensagem indicando qual foi o movimento. 

        Veja as mensagens no roteiro.
        
        Sugestão: inspire-se na sua função movimentaPacMan() do EP2.
        '''
        n_lin,n_col=self.lab.dimensao()
        
        if direcao==CIMA:
            if self.lin!=0:
                if self.lab.get(self.lin-1,self.col)!='+' and self.lab.get(self.lin-1,self.col)=='.':
                    print("Pacman.mova(): Pac-Man moveu-se de [%d][%d]"%(self.lin,self.col),"para [%d][%d]"%(self.lin-1,self.col))
                    self.dir='w'
                    self.lin-=1
                    self.pts+=1
                    self.lab.put(self.lin,self.col,' ')
                   
                    
                elif self.lab.get(self.lin-1,self.col)!='+' and self.lab.get(self.lin-1,self.col)==' ':
                    print("Pacman.mova(): Pac-Man moveu-se de [%d][%d]"%(self.lin,self.col),"para [%d][%d]"%(self.lin-1,self.col))
                    self.dir='w'
                    self.lin-=1
                        
                elif self.lab.get(self.lin-1,self.col)=='+':
                    print("Pacman.mova(): movimento do Pac-Man de [%d][%d]"%(self.lin,self.col),"para [%d][%d]"%(self.lin-1,self.col),"não é possível")
                    self.dir='w'
            
            else:
                if self.lab.get(n_lin-1,self.col)!='+' and self.lab.get(n_lin-1,self.col)=='.':
                    print("Pacman.mova(): Pac-Man moveu-se de [%d][%d]"%(self.lin,self.col),"para [%d][%d]"%(n_lin-1,self.col))
                    self.dir='w'
                    self.pts+=1
                    self.lin=n_lin-1
                    self.lab.put(self.lin,self.col,' ')
                
                elif self.lab.get(n_lin-1,self.col)!='+' and self.lab.get(n_lin-1,self.col)==' ':
                    print("Pacman.mova(): Pac-Man moveu-se de [%d][%d]"%(self.lin,self.col),"para [%d][%d]"%(n_lin-1,self.col))
                    self.dir='w'
                    self.lin=n_lin-1
                
                elif self.lab.get(n_lin-1,self.col)=='+':
                    print("Pacman.mova(): movimento do Pac-Man de [%d][%d]"%(self.lin,self.col),"para [%d][%d]"%(n_lin-1,self.col),"não é possível")
                
        if direcao==BAIXO:
            if self.lin!=n_lin-1:
                if self.lab.get(self.lin+1,self.col)!='+' and self.lab.get(self.lin+1,self.col)=='.':
                    print("Pacman.mova(): Pac-Man moveu-se de [%d][%d]"%(self.lin,self.col),"para [%d][%d]"%(self.lin+1,self.col))
                    self.dir='s'
                    self.lin+=1
                    self.pts+=1
                    self.lab.put(self.lin,self.col,' ')
                elif self.lab.get(self.lin+1,self.col)!='+' and self.lab.get(self.lin+1,self.col)==' ':
                    print("Pacman.mova(): Pac-Man moveu-se de [%d][%d]"%(self.lin,self.col),"para [%d][%d]"%(self.lin+1,self.col))
                    self.dir='s'
                    self.lin+=1
                
                elif self.lab.get(self.lin+1,self.col)=='+':
                    print("Pacman.mova(): movimento do Pac-Man de [%d][%d]"%(self.lin,self.col),"para [%d][%d]"%(self.lin+1,self.col),"não é possível")
                
            else:
                if self.lab.get(0,self.col)!='+' and self.lab.get(0,self.col)=='.':
                    print("Pacman.mova(): Pac-Man moveu-se de [%d][%d]"%(self.lin,self.col),"para [%d][%d]"%(0,self.col))
                    self.dir='s'
                    self.lin=0
                    self.pts+=1
                    self.lab.put(self.lin,self.col,' ')
                
                elif self.lab.get(0,self.col)!='+' and self.lab.get(0,self.col)==' ':
                    print("Pacman.mova(): Pac-Man moveu-se de [%d][%d]"%(self.lin,self.col),"para [%d][%d]"%(0,self.col))
                    self.dir='s'
                    self.lin=0
                
                elif self.lab.get(0,self.col)=='+':
                     print("Pacman.mova(): movimento do Pac-Man de [%d][%d]"%(self.lin,self.col),"para [%d][%d]"%(0,self.col),"não é possível")
                     
        if direcao==ESQUERDA:
            if self.col!=0:
                if self.lab.get(self.lin,self.col-1)!='+' and self.lab.get(self.lin,self.col-1)=='.':
                    print("Pacman.mova(): Pac-Man moveu-se de [%d][%d]"%(self.lin,self.col),"para [%d][%d]"%(self.lin,self.col-1))
                    self.dir='a'
                    self.col-=1
                    self.pts+=1
                    self.lab.put(self.lin,self.col,' ')
                    
                    
                elif self.lab.get(self.lin,self.col-1)!='+' and self.lab.get(self.lin,self.col-1)==' ':
                    print("Pacman.mova(): Pac-Man moveu-se de [%d][%d]"%(self.lin,self.col),"para [%d][%d]"%(self.lin,self.col-1))
                    self.dir='a'
                    self.col-=1
                    
                elif self.lab.get(self.lin,self.col-1)=='+':
                    print("Pacman.mova(): movimento do Pac-Man de [%d][%d]"%(self.lin,self.col),"para [%d][%d]"%(self.lin,self.col-1),"não é possível")
                    
            
            else:
                if self.lab.get(self.lin,n_col-1)!='+' and self.lab.get(self.lin,n_col-1)=='.':
                    print("Pacman.mova(): Pac-Man moveu-se de [%d][%d]"%(self.lin,self.col),"para [%d][%d]"%(self.lin,n_col-1))
                    self.dir='a'
                    self.col=n_col-1
                    self.pts+=1
                    self.lab.put(self.lin,self.col,' ')
                elif self.lab.get(self.lin,n_col-1)!='+' and self.lab.get(self.lin,n_col-1)==' ':
                    print("Pacman.mova(): Pac-Man moveu-se de [%d][%d]"%(self.lin,self.col),"para [%d][%d]"%(self.lin,n_col-1))
                    self.dir='a'
                    self.col=n_col-1
                    
                elif self.lab.get(self.lin,n_col-1)=='+':
                    print("Pacman.mova(): movimento do Pac-Man de [%d][%d]"%(self.lin,self.col),"para [%d][%d]"%(self.lin,n_col-1),"não é possível")
                    
        if direcao==DIREITA:
            if self.col!=n_col-1:
                if self.lab.get(self.lin,self.col+1)!='+' and self.lab.get(self.lin,self.col+1)=='.':
                    print("Pacman.mova(): Pac-Man moveu-se de [%d][%d]"%(self.lin,self.col),"para [%d][%d]"%(self.lin,self.col+1))
                    self.dir='d'
                    self.col+=1
                    self.pts+=1
                    self.lab.put(self.lin,self.col,' ')
                    
                    
                elif self.lab.get(self.lin,self.col+1)!='+' and self.lab.get(self.lin,self.col+1)==' ':
                    print("Pacman.mova(): Pac-Man moveu-se de [%d][%d]"%(self.lin,self.col),"para [%d][%d]"%(self.lin,self.col+1))
                    self.dir='d'
                    self.col+=1
                    
                elif self.lab.get(self.lin,self.col+1)=='+':
                    print("Pacman.mova(): movimento do Pac-Man de [%d][%d]"%(self.lin,self.col),"para [%d][%d]"%(self.lin,self.col+1),"não é possível")
                    
            else:
                if self.lab.get(self.lin,0)!='+' and self.lab.get(self.lin,0)=='.':
                    print("Pacman.mova(): Pac-Man moveu-se de [%d][%d]"%(self.lin,self.col),"para [%d][%d]"%(self.lin,0))
                    self.dir='d'
                    self.col=0
                    self.pts+=1
                    self.lab.put(self.lin,self.col,' ')
                    
                    
                elif self.lab.get(self.lin,0)!='+' and self.lab.get(self.lin,0)==' ':
                    print("Pacman.mova(): Pac-Man moveu-se de [%d][%d]"%(self.lin,self.col),"para [%d][%d]"%(self.lin,0))
                    self.dir='d'
                    self.col=0
                    
                elif self.lab.get(self.lin,0)=='+':
                    print("Pacman.mova(): movimento do Pac-Man de [%d][%d]"%(self.lin,self.col),"para [%d][%d]"%(self.lin,0),"não é possível")
                    
                    
                    
                
            
