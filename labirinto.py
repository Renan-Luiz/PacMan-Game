import sys # sys.exit()

# as constantes que podem ser usadas estão em constantes.py
# para usá-las não é necessário escrever "constantes."
from constantes import *  # PACDOT, VAZIO, PACMAN, CARACTERES_VALIDOS ...

# descomente a linha a seguir se você usa alguma função do módulo extras
# import extras

#----------------------------------------------------------------
class Labirinto:
    '''Classe utilizada para representar um labirinto.

    O labirinto é representado através de uma matriz (= lista de listas). 

    Cada objeto dessa classe tem dois atributos de estado:

        * `lab`: é uma matriz (lista de listas) que representa o labirinto.
           Cada posição da matriz pode conter um caractere dos caracteres
           que estão no string CARACTERES_VALIDOS (= '+CF. ', 
           veja o arquivo constantes.py).

        * `pacdots`: é um inteiro que indica o número de pacdots no 
           labirinto.  
 
    Você deverá escrever os métodos sugeridos a seguir.

    '''                              

    #------------------------------------------------------------
    # Não modifique o método a seguir.
    def __init__(self, nome_arquivo):
        '''(Labirinto,str) -> None

        Construtor: recebe uma referência 

            - `self` para o objeto Labirinto que está sendo construído

        e um string `nome_arquivo` com o nome de um arquivo que contém 
        um labirinto. 

        O método examina o arquivo `nome_arquivo` e cria e retorna um 
        objeto da classe Labirinto.
 
        Cada posição do labirinto contém um dos caracteres em
        CARACTERES_VALIDOS (ver constantes.py).

        Se algum problema for detectado uma mensagem deve ser exibida e a 
        execução do programa será interrompida (sys.exit(0)).
        
        Método mágico: retorna, mas não tem `return`.
        '''
        # apelidos para a matriz do labirinto e para o número de pacdots
        lab     = []
        pacdots = 0
        
        # abra o arquivo. 
        try:
            arquivo = open(nome_arquivo, 'r')
        except:
            print("Labirinto.__init__(): ERRO: não consegui abrir o arquivo '%s'" %nome_arquivo)
            sys.exit(0)

        # leia todas as linhas do arquivo
        linhas_arq = arquivo.readlines()
        n = len(linhas_arq) # número de linhas no arquivo

        # feche o arquivo
        arquivo.close()

        # remova os caracteres brancos no final de cada linha
        i = 0
        while i < n and linhas_arq[i] != '':
            linhas_arq[i] = linhas_arq[i].rstrip() 
            i += 1

        # se o labirinto é vazio, imprima mensagem de erro e encerre a execução
        if i == 0:
            print('Labirinto.__init__(): ERRO: labirinto não pode ser vazio')
            sys.exit(0)
            
        # dimensão do labirinto será n_lin x n_col
        n_lin = i # linhas após a primeira em branco serão ignoradas
        n_col = len(linhas_arq[0])
        
        # crie a matriz com o labirinto 
        encontrou_pacman = False
        i = 0
        while i < n_lin:
            # construa a linha i do labirinto
            linha_lab = []
            
            # se as linhas não tem o mesmo tamanho, encerre a execução
            if len(linhas_arq[i]) != n_col:
                print('Labirinto.__init__(): ERRO: linhas devem ter o mesmo tamanho (linha=%d)' %i)
                sys.exit(0)

            j = 0
            while j < n_col:
                # coloque caractere na linha do labirinto (=lista)
                linha_lab.append(linhas_arq[i][j])
                
                # se as linhas tem algum caractere inválido, encerre a execução
                if linhas_arq[i][j] not in CARACTERES_VALIDOS:
                    print("Labirinto.__init__(): ERRO: caractere inválido ('%s') encontrado"
                                 %linhas_arq[i][j])
                    sys.exit(0)
                
                # encontrou um Pac-Man
                if linhas_arq[i][j] == PACMAN:
                    # se já havia encontrado um Pac-Man, encerre a execução
                    if encontrou_pacman:
                        print('Labirinto.__init__(): ERRO: Pac-Man já foi especificado ([%d][%d])' %(i,j))
                        sys.exit(0)
                    encontrou_pacman = True
                elif linhas_arq[i][j] == PACDOT:
                    pacdots += 1
                    
                # vá para o próximo caractere em linhas_arq[i]         
                j += 1

            # coloque linha no labirinto    
            lab.append(linha_lab)

            # vá para a próxima linha
            i += 1

        # se um pacman nao foi encontrado, encerre a execução
        if not encontrou_pacman:
            print('Labirinto.__init__(): ERRO: Pac-Man não foi encontrado no labirinto')
            sys.exit(0)

        # crie os atributos de estado do objeto Labirinto   
        self.lab     = lab
        self.pacdots = pacdots

    #-----------------------------------------------------------------
    def __str__(self):
        '''(Labirinto) -> str

        Recebe um Labirinto referenciado por `self` e cria e 
        retorna um string que poderá ser exibido por print() para
        imprimir um Labirinto.

        Esse também é o string retornado pela função nativa str().

        Para produzir o efeito de uma mudança de linha, coloque 
        no string um '\n'.

        Sugestão: inspire-se na função imprimeLabirinto() do EP2.
            Você deve trocar os prints pela criação de um string.
            Aqui será muito mais simples, pois você não precisa 
            se preocupar com o conteúdo de cada posição.
        '''
        string=''
        for i in range(len(self.lab)):
            for j in range(len(self.lab[0])):
               string=string+self.lab[i][j]
               if j==len(self.lab[0])-1:
                   string=string+'\n'
                   
        return string
        
        
    #-----------------------------------------------------------------
    def dimensao(self):
        '''(Labirinto) -> int, int

        Recebe um Labirinto referenciado por `self` e retorna o 
        número de linhas e colunas do labirinto.
        '''
        for n_lin in range(len(self.lab)):
            n_lin+=1    
            for n_col in range(len(self.lab[0])):
                n_col+=1
        
        return n_lin,n_col
                
            
            
        
        

    #-----------------------------------------------------------------
    def get(self, lin, col):
        '''(Labirinto, int, int) -> str

        Recebe um Labirinto referenciado por `self` e inteiros 
        `lin` e `col` e retorna o caractere que está na posição
        [lin][col] do labirinto 
        '''
        
        
        return self.lab[lin][col]
        
        

    #-----------------------------------------------------------------
    def put(self, lin, col, valor):
        '''(Labirinto, int, int, objeto) -> None

        Recebe um Labirinto referenciado por `self`, inteiros 
        `lin` e `col` e um  objeto `valor` e coloca `valor` na 
        na posição [lin][col] do labirinto.

        Este método deve atualizar o atributo `pacdots`. 
        '''
        self.lab[lin][col]=valor
        n_pacdot=0
        if valor=='.':
            n_pacdot+=1
            
    #-----------------------------------------------------------------        
    def no_pacdots(self):
        '''(labirinto) -> int

        Recebe um Labirinto referenciado por `self` e retorna o número de
        pacdots no labirinto.
        '''
        n_pacdots=0
        for i in range(len(self.lab)):
            for j in range(len(self.lab[0])):
                if self.lab[i][j]=='.':
                    n_pacdots+=1
        
        return n_pacdots
       
        
    #-----------------------------------------------------------------
    def direcoes_possiveis(self,lin,col):
        '''(Labirinto, int, int) -> list

        Recebe um Labirinto referenciado por `self` e inteiros
        `lin` e `col` representando a posição [lin][col] do labirinto.

        O método cria e retorna uma lista com caracteres no string DIRECOES 
        que representam as direções possíveis para as quais um Pac-Man ou 
        Fantasma poderia se movimentar se estivesse na posição [lin][col].
        '''
        direc_poss=[]
        if lin>0:
            if self.lab[lin-1][col]!='+':
                direc_poss.append('w')
        else:
            if self.lab[len(self.lab)-1][col]!='+':
                direc_poss.append('w')                
        
        if col>0:
            if self.lab[lin][col-1]!='+':
                direc_poss.append('a')
        else:
            if self.lab[lin][len(self.lab[0])-1]!='+':
                direc_poss.append('a')
                
        if lin<len(self.lab)-1:      
            if self.lab[lin+1][col]!='+':
                direc_poss.append('s')
        else:
            if self.lab[0][col]!='+':  
                direc_poss.append('s')
        
        if col<len(self.lab[0])-1:
            if self.lab[lin][col+1]!='+':
                direc_poss.append('d')
        else:
            if self.lab[lin][0]!='+':
                direc_poss.append('d')
            
        return direc_poss
    #-----------------------------------------------------------------
    def matriz(self):
        '''(Labirinto) -> matriz (list of list)

        Recebe um Labirinto referenciado por `self` e cria e retorna 
        um clone/cópia da matriz self.lab.
        '''
        novo_lab=[]
        for i in range(len(self.lab)):
            linha_lab=[]
            for j in range(len(self.lab[0])):
                a=self.lab[i][j]
                linha_lab.append(a)
            novo_lab.append(linha_lab)
        
        return novo_lab
        


 
