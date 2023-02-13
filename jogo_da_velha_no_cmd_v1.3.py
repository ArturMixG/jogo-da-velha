import random

# ----- configuracoes ------
pontosX = 0
pontosO = 0
q1 = '1'
q2 = '2'
q3 = '3'
q4 = '4'
q5 = '5'
q6 = '6'
q7 = '7'
q8 = '8'
q9 = '9'
jogadas = 0
empates = 0


# ----- imagens ------
def img_tela_inicio():
    print('''
___________________________________
|                                 |
|    J O G O   D A   V E L H A    |         
|                                 |
|         ________________        |  
|    1-  |player vs player|       |
|        |________________|       |                  
|         ________________        |                 
|    2-  |  player vs IA  |       |
|        |________________|       |
|                                 |
|_________________________________| 
''')
def img_tela_escolher_IA():
    print('''
___________________________________
|                                 |
|            /menu - menu         |         
|                                 |
|           1 - Fácil             |  
|                                 |
|           2 - Médio             |                  
|                                 |                 
|           3 - Difícil           |
|                                 |
|                                 |
|_________________________________| 
''')
def img_jogo_da_velha():
    print(f'''
____________________________________
|                                  |            
|  x = {pontosX}      |      |       o = {pontosO} |
|          {q1}  |   {q2}  |   {q3}         |                 
|       ______|______|______       |
|             |      |             |                  
|          {q4}  |   {q5}  |   {q6}         |   /menu-  menu                 
|       ______|______|______       |
|             |      |             |
|          {q7}  |   {q8}  |   {q9}         |
|             |      |             |
|__________________________________| 
''')
def img_X_venceu():
    print(f'''
___________________________________
|                                  |            
|  x = {pontosX}      |      |       o = {pontosO} |
|          {q1}  |   {q2}  |   {q3}         |                 
|__________________________________| 
|                                  |
|         X    V E N C E U         |      
|                                  | 
|      1- de novo     2- menu      |
|__________________________________|
|             |      |             |
|__________________________________| 
''')
def img_O_venceu():
    print(f'''
___________________________________
|                                  |            
|  x = {pontosX}      |      |       o = {pontosO} |
|          {q1}  |   {q2}  |   {q3}         |                 
|__________________________________| 
|                                  |
|         O    V E N C E U         |      
|                                  | 
|      1- de novo     2- menu      |
|__________________________________|
|             |      |             |
|__________________________________| 
''')
def img_empate():
    print(f'''
___________________________________
|                                  |            
|  x = {pontosX}      |      |       o = {pontosO} |
|          {q1}  |   {q2}  |   {q3}         |                 
|__________________________________| 
|                                  |
|            E M P A T E           |      
|                                  | 
|      1- de novo     2- menu      |
|__________________________________|
|             |      |             |
|__________________________________| 
''')
# ------ jogada ------
def jogadaX():

    global q1
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global jogadas

    def condicaoX():
        global q1
        global q2
        global q3
        global q4
        global q5
        global q6
        global q7
        global q8
        global q9
        if opcao == '1':
            q1 = 'X'
        elif opcao == '2':
            q2 = 'X'
        elif opcao == '3':
            q3 = 'X'
        elif opcao == '4':
            q4 = 'X'
        elif opcao == '5':
            q5 = 'X'
        elif opcao == '6':
            q6 = 'X'
        elif opcao == '7':
            q7 = 'X'
        elif opcao == '8':
            q8 = 'X'
        elif opcao == '9':
            q9 = 'X'
        elif opcao == '/menu':
            tela_inicio()
    jogadas += 1
    opcao = input('jogador X: ')
    if opcao == '1':
        if q1 == '1':    
            q1 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()
                

    elif opcao == '2':
        if q2 == '2':    
            q2 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()    
    elif opcao == '3':
        if q3 == '3':    
            q3 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()    
    elif opcao == '4':
        if q4 == '4':    
            q4 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()    
    elif opcao == '5':
        if q5 == '5':    
            q5 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()    
    elif opcao == '6':
        if q6 == '6':    
            q6 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()    
    elif opcao == '7':
        if q7 == '7':    
            q7 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()    
    elif opcao == '8':
        if q8 == '8':    
            q8 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()    
    elif opcao == '9':
        if q9 == '9':    
            q9 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()  
    elif opcao == '/menu':
        tela_inicio()  
    else:
        while opcao != '/menu' and opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5' and opcao != '6' and opcao != '7' and opcao != '8' and opcao != '9':
            print('ERRO! Escolha uma opcao existente.')
            opcao = input('jogador X: ')
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()
    verificador()
def jogadaO():
    global q1
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global jogadas
    global opcao
    


    def condicaoO():
        global q1
        global q2
        global q3
        global q4
        global q5
        global q6
        global q7
        global q8
        global q9
        if opcao == '1':
            q1 = 'O'
        elif opcao == '2':
            q2 = 'O'
        elif opcao == '3':
            q3 = 'O'
        elif opcao == '4':
            q4 = 'O'
        elif opcao == '5':
            q5 = 'O'
        elif opcao == '6':
            q6 = 'O'
        elif opcao == '7':
            q7 = 'O'
        elif opcao == '8':
            q8 = 'O'
        elif opcao == '9':
            q9 = 'O'
        elif opcao == '/menu':
            tela_inicio()
    jogadas += 1
    opcao = input('jogador O: ')
    if opcao == '1':
        if q1 == '1':    
            q1 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador O: ')
            condicaoO()
                
                
    elif opcao == '2':
        if q2 == '2':    
            q2 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador O: ')
            condicaoO()
    elif opcao == '3':
        if q3 == '3':    
            q3 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador O: ')
            condicaoO()    
    elif opcao == '4':
        if q4 == '4':    
            q4 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador O: ')
            condicaoO()    
    elif opcao == '5':
        if q5 == '5':    
            q5 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador O: ')
            condicaoO()    
    elif opcao == '6':
        if q6 == '6':    
            q6 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador O: ')
            condicaoO()    
    elif opcao == '7':
        if q7 == '7':    
            q7 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador O: ')
            condicaoO()    
    elif opcao == '8':
        if q8 == '8':    
            q8 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador O: ')
            condicaoO()    
    elif opcao == '9':
        if q9 == '9':    
            q9 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador O: ')
            condicaoO()   
    elif opcao == '/menu':
        tela_inicio() 
    else:
        while opcao != '0' and opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5' and opcao != '6' and opcao != '7' and opcao != '8' and opcao != '9':
            print('ERRO! Escolha uma opcao existente.')
            opcao = input('jogador O: ')
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador O: ')
            condicaoO()
    verificador()

def jogadaIAfacil():
    global q1
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global jogadas
    global opcao
    


    def condicaoO():
        global q1
        global q2
        global q3
        global q4
        global q5
        global q6
        global q7
        global q8
        global q9
        if opcao == '1':
            q1 = 'O'
        elif opcao == '2':
            q2 = 'O'
        elif opcao == '3':
            q3 = 'O'
        elif opcao == '4':
            q4 = 'O'
        elif opcao == '5':
            q5 = 'O'
        elif opcao == '6':
            q6 = 'O'
        elif opcao == '7':
            q7 = 'O'
        elif opcao == '8':
            q8 = 'O'
        elif opcao == '9':
            q9 = 'O'
    
    
    opcoes = ['1', '2', '3', '4', '5','6', '7', '8', '9']
    opcao = random.choice(opcoes)
    

    jogadas += 1
    opcao = random.choice(opcoes)
    if opcao == '1':
        if q1 == '1':    
            q1 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                opcao = random.choice(opcoes)
            condicaoO()
                
                
    elif opcao == '2':
        if q2 == '2':    
            q2 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                opcao = random.choice(opcoes)
            condicaoO()
    elif opcao == '3':
        if q3 == '3':    
            q3 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                opcao = random.choice(opcoes)
            condicaoO()    
    elif opcao == '4':
        if q4 == '4':    
            q4 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                opcao = random.choice(opcoes)
            condicaoO()    
    elif opcao == '5':
        if q5 == '5':    
            q5 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                opcao = random.choice(opcoes)
            condicaoO()    
    elif opcao == '6':
        if q6 == '6':    
            q6 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                opcao = random.choice(opcoes)
            condicaoO()    
    elif opcao == '7':
        if q7 == '7':    
            q7 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                opcao = random.choice(opcoes)
            condicaoO()    
    elif opcao == '8':
        if q8 == '8':    
            q8 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                opcao = random.choice(opcoes)
            condicaoO()    
    elif opcao == '9':
        if q9 == '9':    
            q9 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                opcao = random.choice(opcoes)
            condicaoO()   
    verificadorIAfacil()
def jogadaXIAfacil():
    

    global q1
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global jogadas

    def condicaoX():
        global q1
        global q2
        global q3
        global q4
        global q5
        global q6
        global q7
        global q8
        global q9
        if opcao == '1':
            q1 = 'X'
        elif opcao == '2':
            q2 = 'X'
        elif opcao == '3':
            q3 = 'X'
        elif opcao == '4':
            q4 = 'X'
        elif opcao == '5':
            q5 = 'X'
        elif opcao == '6':
            q6 = 'X'
        elif opcao == '7':
            q7 = 'X'
        elif opcao == '8':
            q8 = 'X'
        elif opcao == '9':
            q9 = 'X'
        elif opcao == '/menu':
            tela_inicio()
    jogadas += 1
    opcao = input('jogador X: ')
    if opcao == '1':
        if q1 == '1':    
            q1 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()
                

    elif opcao == '2':
        if q2 == '2':    
            q2 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()    
    elif opcao == '3':
        if q3 == '3':    
            q3 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()    
    elif opcao == '4':
        if q4 == '4':    
            q4 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()    
    elif opcao == '5':
        if q5 == '5':    
            q5 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()    
    elif opcao == '6':
        if q6 == '6':    
            q6 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()    
    elif opcao == '7':
        if q7 == '7':    
            q7 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()    
    elif opcao == '8':
        if q8 == '8':    
            q8 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()    
    elif opcao == '9':
        if q9 == '9':    
            q9 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()  
    elif opcao == '/menu':
        tela_inicio()  
    else:
        while opcao != '/menu' and opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5' and opcao != '6' and opcao != '7' and opcao != '8' and opcao != '9':
            print('ERRO! Escolha uma opcao existente.')
            opcao = input('jogador X: ')
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()
    verificadorIAfacil()

def jogadaIAmedio():
    global q1
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global jogadas
    global opcao
    


    def condicaoO():
        global q1
        global q2
        global q3
        global q4
        global q5
        global q6
        global q7
        global q8
        global q9
        if opcao == '1':
            q1 = 'O'
        elif opcao == '2':
            q2 = 'O'
        elif opcao == '3':
            q3 = 'O'
        elif opcao == '4':
            q4 = 'O'
        elif opcao == '5':
            q5 = 'O'
        elif opcao == '6':
            q6 = 'O'
        elif opcao == '7':
            q7 = 'O'
        elif opcao == '8':
            q8 = 'O'
        elif opcao == '9':
            q9 = 'O'
    
    #------ criando IA---------
    def IA():
        global opcao

        # --- ataque ---

        # horizontal
        if q1 == 'O' and q2 == 'O' and q3 == '3':
            opcao = '3'
        elif q2 == 'O' and q3 == 'O'and q1 == '1':
            opcao = '1'
        elif q1 == 'O' and q3 == 'O' and q2 == '2':
            opcao = '2'
        elif q4 == 'O' and q5 == 'O'and q6 == '6':
            opcao = '6'
        elif q5 == 'O' and q6 == 'O'and q4 == '4':
            opcao = '4'
        elif q4 == 'O' and q6 == 'O' and q5 == '5':
            opcao = '5'
        elif q7 == 'O' and q8 == 'O'and q9 == '9':
            opcao = '9'
        elif q8 == 'O' and q9 == 'O'and q7 == '7':
            opcao = '7'
        elif q7 == 'O' and q9 == 'O' and q8 == '8':
            opcao = '8'

        # vertical
        elif q1 == 'O' and q4 == 'O'and q7 == '7':
            opcao = '7'
        elif q4 == 'O' and q7 == 'O'and q1 == '1':
            opcao = '1'
        elif q1 == 'O' and q7 == 'O' and q4 == '4':
            opcao = '4'
        elif q2 == 'O' and q5 == 'O'and q8 == '8':
            opcao = '8'
        elif q5 == 'O' and q8 == 'O'and q2 == '2':
            opcao = '2'
        elif q2 == 'O' and q8 == 'O' and q5 == '5':
            opcao = '5'
        elif q3 == 'O' and q6 == 'O'and q9 == '9':
            opcao = '9'
        elif q6 == 'O' and q9 == 'O'and q3 == '3':
            opcao = '3'
        elif q3 == 'O' and q9 == 'O' and q6 == '6':
            opcao = '6'

        # diagonal
        elif q1 == 'O' and q5 == 'O'and q9 == '9':
            opcao = '9'
        elif q5 == 'O' and q9 == 'O'and q1 == '1':
            opcao = '1'
        elif q7 == 'O' and q5 == 'O'and q3 == '3':
            opcao = '3'
        elif q5 == 'O' and q3 == 'O'and q7 == '7':
            opcao = '7'
        elif q1 == 'O' and q9 == 'O' and q5 == '5':
            opcao = '5'
        elif q3 == 'O' and q7 == 'O' and q5 == '5':
            opcao = '5'
        # --- defesa ---

        # horizontal
        elif q1 == 'X' and q2 == 'X' and q3 == '3':
            opcao = '3'
        elif q2 == 'X' and q3 == 'X'and q1 == '1':
            opcao = '1'
        elif q1 == 'X' and q3 == 'X' and q2 == '2':
            opcao = '2'
        elif q4 == 'X' and q5 == 'X'and q6 == '6':
            opcao = '6'
        elif q5 == 'X' and q6 == 'X'and q4 == '4':
            opcao = '4'
        elif q4 == 'X' and q6 == 'X' and q5 == '5':
            opcao = '5'
        elif q7 == 'X' and q8 == 'X'and q9 == '9':
            opcao = '9'
        elif q8 == 'X' and q9 == 'X'and q7 == '7':
            opcao = '7'
        elif q7 == 'X' and q9 == 'X' and q8 == '8':
            opcao = '8'
        
        # vertical
        elif q1 == 'X' and q4 == 'X'and q7 == '7':
            opcao = '7'
        elif q4 == 'X' and q7 == 'X'and q1 == '1':
            opcao = '1'
        elif q1 == 'X' and q7 == 'X' and q4 == '4':
            opcao = '4'
        elif q2 == 'X' and q5 == 'X'and q8 == '8':
            opcao = '8'
        elif q5 == 'X' and q8 == 'X'and q2 == '2':
            opcao = '2'
        elif q2 == 'X' and q8 == 'X' and q5 == '5':
            opcao = '5'
        elif q3 == 'X' and q6 == 'X'and q9 == '9':
            opcao = '9'
        elif q6 == 'X' and q9 == 'X'and q3 == '3':
            opcao = '3'
        elif q3 == 'X' and q9 == 'X' and q6 == '6':
            opcao = '6'
        
        # diagonal
        elif q1 == 'X' and q5 == 'X'and q9 == '9':
            opcao = '9'
        elif q5 == 'X' and q9 == 'X'and q1 == '1':
            opcao = '1'
        elif q7 == 'X' and q5 == 'X'and q3 == '3':
            opcao = '3'
        elif q5 == 'X' and q3 == 'X'and q7 == '7':
            opcao = '7'
        elif q1 == 'X' and q9 == 'X' and q5 == '5':
            opcao = '5'
        elif q3 == 'X' and q7 == 'X' and q5 == '5':
            opcao = '5'
        
        

        else:
            opcoes = ['1', '2', '3', '4', '5','6', '7', '8', '9']
            opcao = random.choice(opcoes)
    

    jogadas += 1
    IA()
    if opcao == '1':
        if q1 == '1':    
            q1 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                IA()
            condicaoO()
                
                
    elif opcao == '2':
        if q2 == '2':    
            q2 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                IA()
            condicaoO()
    elif opcao == '3':
        if q3 == '3':    
            q3 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                IA()
            condicaoO()    
    elif opcao == '4':
        if q4 == '4':    
            q4 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                IA()
            condicaoO()    
    elif opcao == '5':
        if q5 == '5':    
            q5 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                IA()
            condicaoO()    
    elif opcao == '6':
        if q6 == '6':    
            q6 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                IA()
            condicaoO()    
    elif opcao == '7':
        if q7 == '7':    
            q7 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                IA()
            condicaoO()    
    elif opcao == '8':
        if q8 == '8':    
            q8 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                IA()
            condicaoO()    
    elif opcao == '9':
        if q9 == '9':    
            q9 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                IA()
            condicaoO()   
    verificadorIAmedio()
def jogadaXIAmedio():
    

    global q1
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global jogadas

    def condicaoX():
        global q1
        global q2
        global q3
        global q4
        global q5
        global q6
        global q7
        global q8
        global q9
        if opcao == '1':
            q1 = 'X'
        elif opcao == '2':
            q2 = 'X'
        elif opcao == '3':
            q3 = 'X'
        elif opcao == '4':
            q4 = 'X'
        elif opcao == '5':
            q5 = 'X'
        elif opcao == '6':
            q6 = 'X'
        elif opcao == '7':
            q7 = 'X'
        elif opcao == '8':
            q8 = 'X'
        elif opcao == '9':
            q9 = 'X'
        elif opcao == '/menu':
            tela_inicio()
    jogadas += 1
    opcao = input('jogador X: ')
    if opcao == '1':
        if q1 == '1':    
            q1 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()
                

    elif opcao == '2':
        if q2 == '2':    
            q2 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()    
    elif opcao == '3':
        if q3 == '3':    
            q3 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()    
    elif opcao == '4':
        if q4 == '4':    
            q4 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()    
    elif opcao == '5':
        if q5 == '5':    
            q5 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()    
    elif opcao == '6':
        if q6 == '6':    
            q6 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()    
    elif opcao == '7':
        if q7 == '7':    
            q7 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()    
    elif opcao == '8':
        if q8 == '8':    
            q8 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()    
    elif opcao == '9':
        if q9 == '9':    
            q9 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()  
    elif opcao == '/menu':
        tela_inicio()  
    else:
        while opcao != '/menu' and opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5' and opcao != '6' and opcao != '7' and opcao != '8' and opcao != '9':
            print('ERRO! Escolha uma opcao existente.')
            opcao = input('jogador X: ')
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()
    verificadorIAmedio()

def jogadaXIAdificil():
    global q1
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global jogadas

    def condicaoX():
        global q1
        global q2
        global q3
        global q4
        global q5
        global q6
        global q7
        global q8
        global q9
        if opcao == '1':
            q1 = 'X'
        elif opcao == '2':
            q2 = 'X'
        elif opcao == '3':
            q3 = 'X'
        elif opcao == '4':
            q4 = 'X'
        elif opcao == '5':
            q5 = 'X'
        elif opcao == '6':
            q6 = 'X'
        elif opcao == '7':
            q7 = 'X'
        elif opcao == '8':
            q8 = 'X'
        elif opcao == '9':
            q9 = 'X'
        elif opcao == '/menu':
            tela_inicio()
    jogadas += 1
    opcao = input('jogador X: ')
    if opcao == '1':
        if q1 == '1':    
            q1 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()
                

    elif opcao == '2':
        if q2 == '2':    
            q2 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()    
    elif opcao == '3':
        if q3 == '3':    
            q3 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()    
    elif opcao == '4':
        if q4 == '4':    
            q4 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()    
    elif opcao == '5':
        if q5 == '5':    
            q5 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()    
    elif opcao == '6':
        if q6 == '6':    
            q6 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()    
    elif opcao == '7':
        if q7 == '7':    
            q7 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()    
    elif opcao == '8':
        if q8 == '8':    
            q8 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()    
    elif opcao == '9':
        if q9 == '9':    
            q9 = 'X'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()  
    elif opcao == '/menu':
        tela_inicio()  
    else:
        while opcao != '/menu' and opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5' and opcao != '6' and opcao != '7' and opcao != '8' and opcao != '9':
            print('ERRO! Escolha uma opcao existente.')
            opcao = input('jogador X: ')
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                print('a opcao já foi marcada!')
                opcao = input('jogador X: ')
            condicaoX()
    verificadorIAdificil()
def jogadaIAdificil():
    global q1
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global jogadas
    global opcao
    


    def condicaoO():
        global q1
        global q2
        global q3
        global q4
        global q5
        global q6
        global q7
        global q8
        global q9
        if opcao == '1':
            q1 = 'O'
        elif opcao == '2':
            q2 = 'O'
        elif opcao == '3':
            q3 = 'O'
        elif opcao == '4':
            q4 = 'O'
        elif opcao == '5':
            q5 = 'O'
        elif opcao == '6':
            q6 = 'O'
        elif opcao == '7':
            q7 = 'O'
        elif opcao == '8':
            q8 = 'O'
        elif opcao == '9':
            q9 = 'O'
    
    #------ criando IA---------
    def IA():
        global opcao

        lista = ['1', '2', '3','4','5','6','7','8','9']
        lista1 = ['5']
        lista2 = ['3', '7']
        lista3 = ['2', '4', '6', '8']
        lista4 = ['1', '3', '6', '7','8']
        lista5 = ['1', '3', '4', '8', '9']
        lista6 = ['1', '3', '7', '9']
        lista7 = ['1', '9']
        lista8 = ['2', '4', '6', '8']
        lista9 = ['2', '4', '6', '8']
        lista10 = ['5']
        lista11 = ['5']
        lista12 = ['2', '4', '6', '8']
        lista13 = ['1', '9']
        lista14 = ['1', '2', '4', '9']
        lista15 = ['1', '2', '3','4','7','9']
        lista16 = ['1','5','8']
        # --- ataque ---

        # horizontal
        if q1 == 'O' and q2 == 'O' and q3 == '3':
            opcao = '3'
        elif q2 == 'O' and q3 == 'O'and q1 == '1':
            opcao = '1'
        elif q1 == 'O' and q3 == 'O' and q2 == '2':
            opcao = '2'
        elif q4 == 'O' and q5 == 'O'and q6 == '6':
            opcao = '6'
        elif q5 == 'O' and q6 == 'O'and q4 == '4':
            opcao = '4'
        elif q4 == 'O' and q6 == 'O' and q5 == '5':
            opcao = '5'
        elif q7 == 'O' and q8 == 'O'and q9 == '9':
            opcao = '9'
        elif q8 == 'O' and q9 == 'O'and q7 == '7':
            opcao = '7'
        elif q7 == 'O' and q9 == 'O' and q8 == '8':
            opcao = '8'

        # vertical
        elif q1 == 'O' and q4 == 'O'and q7 == '7':
            opcao = '7'
        elif q4 == 'O' and q7 == 'O'and q1 == '1':
            opcao = '1'
        elif q1 == 'O' and q7 == 'O' and q4 == '4':
            opcao = '4'
        elif q2 == 'O' and q5 == 'O'and q8 == '8':
            opcao = '8'
        elif q5 == 'O' and q8 == 'O'and q2 == '2':
            opcao = '2'
        elif q2 == 'O' and q8 == 'O' and q5 == '5':
            opcao = '5'
        elif q3 == 'O' and q6 == 'O'and q9 == '9':
            opcao = '9'
        elif q6 == 'O' and q9 == 'O'and q3 == '3':
            opcao = '3'
        elif q3 == 'O' and q9 == 'O' and q6 == '6':
            opcao = '6'

        # diagonal
        elif q1 == 'O' and q5 == 'O'and q9 == '9':
            opcao = '9'
        elif q5 == 'O' and q9 == 'O'and q1 == '1':
            opcao = '1'
        elif q7 == 'O' and q5 == 'O'and q3 == '3':
            opcao = '3'
        elif q5 == 'O' and q3 == 'O'and q7 == '7':
            opcao = '7'
        elif q1 == 'O' and q9 == 'O' and q5 == '5':
            opcao = '5'
        elif q3 == 'O' and q7 == 'O' and q5 == '5':
            opcao = '5'
        # --- defesa ---

        # horizontal
        elif q1 == 'X' and q2 == 'X' and q3 == '3':
            opcao = '3'
        elif q2 == 'X' and q3 == 'X'and q1 == '1':
            opcao = '1'
        elif q1 == 'X' and q3 == 'X' and q2 == '2':
            opcao = '2'
        elif q4 == 'X' and q5 == 'X'and q6 == '6':
            opcao = '6'
        elif q5 == 'X' and q6 == 'X'and q4 == '4':
            opcao = '4'
        elif q4 == 'X' and q6 == 'X' and q5 == '5':
            opcao = '5'
        elif q7 == 'X' and q8 == 'X'and q9 == '9':
            opcao = '9'
        elif q8 == 'X' and q9 == 'X'and q7 == '7':
            opcao = '7'
        elif q7 == 'X' and q9 == 'X' and q8 == '8':
            opcao = '8'
        
        # vertical
        elif q1 == 'X' and q4 == 'X'and q7 == '7':
            opcao = '7'
        elif q4 == 'X' and q7 == 'X'and q1 == '1':
            opcao = '1'
        elif q1 == 'X' and q7 == 'X' and q4 == '4':
            opcao = '4'
        elif q2 == 'X' and q5 == 'X'and q8 == '8':
            opcao = '8'
        elif q5 == 'X' and q8 == 'X'and q2 == '2':
            opcao = '2'
        elif q2 == 'X' and q8 == 'X' and q5 == '5':
            opcao = '5'
        elif q3 == 'X' and q6 == 'X'and q9 == '9':
            opcao = '9'
        elif q6 == 'X' and q9 == 'X'and q3 == '3':
            opcao = '3'
        elif q3 == 'X' and q9 == 'X' and q6 == '6':
            opcao = '6'
        
        # diagonal
        elif q1 == 'X' and q5 == 'X'and q9 == '9':
            opcao = '9'
        elif q5 == 'X' and q9 == 'X'and q1 == '1':
            opcao = '1'
        elif q7 == 'X' and q5 == 'X'and q3 == '3':
            opcao = '3'
        elif q5 == 'X' and q3 == 'X'and q7 == '7':
            opcao = '7'
        elif q1 == 'X' and q9 == 'X' and q5 == '5':
            opcao = '5'
        elif q3 == 'X' and q7 == 'X' and q5 == '5':
            opcao = '5'
        
        # quando X comeca:
        elif q1 == 'X' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == '5' and q6 == '6' and q7 == '7' and q8 == '8' and q9 == '9':
            opcao = random.choice(lista1)
        elif q1 == 'X' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == 'X' and q6 == '6' and q7 == '7' and q8 == '8' and q9 == 'O':
            opcao = random.choice(lista2)
        elif q1 == 'X' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == 'O' and q6 == '6' and q7 == '7' and q8 == '8' and q9 == 'X':
            opcao = random.choice(lista3)
        elif q1 == '1' and q2 == 'X' and q3 == '3' and q4 == 'X' and q5 == 'O' and q6 == '6' and q7 == '7' and q8 == '8' and q9 == '9':
            opcao = random.choice(lista4)
        elif q1 == '1' and q2 == 'X' and q3 == '3' and q4 == '4' and q5 == 'O' and q6 == 'X' and q7 == '7' and q8 == '8' and q9 == '9':
            opcao = random.choice(lista5)
        elif q1 == '1' and q2 == 'X' and q3 == '3' and q4 == '4' and q5 == 'O' and q6 == '6' and q7 == '7' and q8 == 'X' and q9 == '9':
            opcao = random.choice(lista6)
        elif q1 == 'O' and q2 == 'X' and q3 == '3' and q4 == '4' and q5 == 'O' and q6 == '6' and q7 == '7' and q8 == 'X' and q9 == 'X':
            opcao = '7'
        elif q1 == '1' and q2 == 'X' and q3 == 'O' and q4 == '4' and q5 == 'O' and q6 == '6' and q7 == 'X' and q8 == 'X' and q9 == '9':
            opcao = '9'
        elif q1 == '1' and q2 == '2' and q3 == 'X' and q4 == '4' and q5 == 'X' and q6 == '6' and q7 == 'O' and q8 == '8' and q9 == '9':
            opcao = random.choice(lista7)
        elif q1 == '1' and q2 == '2' and q3 == 'X' and q4 == '4' and q5 == 'O' and q6 == '6' and q7 == 'X' and q8 == '8' and q9 == '9':
            opcao = random.choice(lista8)
        elif q1 == '1' and q2 == '2' and q3 == '3' and q4 == 'X' and q5 == 'O' and q6 == 'X' and q7 == '7' and q8 == '8' and q9 == '9':
            opcao = '7'
        elif q1 == '1' and q2 == '2' and q3 == 'X' and q4 == '4' and q5 == 'O' and q6 == '6' and q7 == 'X' and q8 == '8' and q9 == '9':
            opcao = random.choice(lista9)
        elif q1 == '1' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == '5' and q6 == '6' and q7 == 'X' and q8 == '8' and q9 == '9':
            opcao = random.choice(lista10)
        elif q1 == '1' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == '5' and q6 == '6' and q7 == '7' and q8 == '8' and q9 == 'X':
            opcao = random.choice(lista11)
        elif q1 == 'X' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == 'O' and q6 == '6' and q7 == '7' and q8 == '8' and q9 == 'X':
            opcao = random.choice(lista12)
        elif q1 == '1' and q2 == '2' and q3 == 'X' and q4 == '4' and q5 == 'X' and q6 == '6' and q7 == 'O' and q8 == '8' and q9 == '9':
            opcao = random.choice(lista13)    
        elif q1 == '1' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == 'X' and q6 == '6' and q7 == '7' and q8 == '8' and q9 == '9':
            opcao = '7'
        elif q1 == '1' and q2 == '2' and q3 == '3' and q4 == 'X' and q5 == 'O' and q6 == '6' and q7 == '7' and q8 == 'X' and q9 == '9':
            opcao = random.choice(lista14)
        elif q1 == '1' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == 'O' and q6 == 'X' and q7 == '7' and q8 == 'X' and q9 == '9':
            opcao = random.choice(lista15)
        elif q1 == 'X' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == '5' and q6 == '6' and q7 == '7' and q8 == '8' and q9 == '9':
            opcao = '5'
        elif q1 == '1' and q2 == '2' and q3 == 'X' and q4 == '4' and q5 == '5' and q6 == '6' and q7 == '7' and q8 == '8' and q9 == '9':
            opcao = '5'
        elif q1 == '1' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == '5' and q6 == '6' and q7 == 'X' and q8 == '8' and q9 == '9':
            opcao = '5'
        elif q1 == '1' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == '5' and q6 == '6' and q7 == '7' and q8 == '8' and q9 == 'X':
            opcao = '5'
        elif q1 == '1' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == 'O' and q6 == 'X' and q7 == 'X' and q8 == '8' and q9 == '9':
            opcao = '9'
        elif q1 == 'X' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == 'O' and q6 == 'X' and q7 == '7' and q8 == '8' and q9 == '9':
            opcao = '3'
        elif q1 == '1' and q2 == '2' and q3 == 'X' and q4 == 'X' and q5 == 'O' and q6 == '6' and q7 == '7' and q8 == '8' and q9 == '9':
            opcao = '1'
        elif q1 == '1' and q2 == '2' and q3 == '3' and q4 == 'X' and q5 == 'O' and q6 == '6' and q7 == '7' and q8 == '8' and q9 == 'X':
            opcao = '7'
        elif q1 == '1' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == '5' and q6 == 'X' and q7 == '7' and q8 == '8' and q9 == '9':
            opcao = '5'
        elif q1 == '1' and q2 == 'X' and q3 == '3' and q4 == '4' and q5 == '5' and q6 == '6' and q7 == '7' and q8 == '8' and q9 == '9':
            opcao = '5'
        elif q1 == '1' and q2 == '2' and q3 == '3' and q4 == 'X' and q5 == '5' and q6 == '6' and q7 == '7' and q8 == '8' and q9 == '9':
            opcao = '5'
        elif q1 == '1' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == '5' and q6 == '6' and q7 == '7' and q8 == 'X' and q9 == '9':
            opcao = '5'

        # quando O comeca:
        elif q1 == '1' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == '5' and q6 == '6' and q7 == '7' and q8 == '8' and q9 == '9':
            opcao = random.choice(lista16)
        elif q1 == 'O' and q2 == 'X' and q3 == '3' and q4 == '4' and q5 == '5' and q6 == '6' and q7 == '7' and q8 == '8' and q9 == '9':
            opcao = '5'
        elif q1 == 'O' and q2 == 'X' and q3 == '3' and q4 == '4' and q5 == 'O' and q6 == '6' and q7 == '7' and q8 == '8' and q9 == 'X':
            opcao = '7'
        elif q1 == 'O' and q2 == '2' and q3 == 'X' and q4 == '4' and q5 == '5' and q6 == '6' and q7 == '7' and q8 == '8' and q9 == '9':
            opcao = '9'
        elif q1 == 'O' and q2 == '2' and q3 == '3' and q4 == 'X' and q5 == '5' and q6 == '6' and q7 == '7' and q8 == '8' and q9 == '9':
            opcao = '5'
        elif q1 == 'O' and q2 == '2' and q3 == '3' and q4 == 'X' and q5 == 'O' and q6 == '6' and q7 == '7' and q8 == '8' and q9 == 'X':
            opcao = '3'
        elif q1 == 'O' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == 'X' and q6 == '6' and q7 == '7' and q8 == '8' and q9 == '9':
            opcao = '9'
        elif q1 == 'O' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == '5' and q6 == 'X' and q7 == '7' and q8 == '8' and q9 == '9':
            opcao = '5'
        elif q1 == 'O' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == '5' and q6 == '6' and q7 == 'X' and q8 == '8' and q9 == '9':
            opcao = '9'
        elif q1 == 'O' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == '5' and q6 == '6' and q7 == '7' and q8 == 'X' and q9 == '9':
            opcao = '5'
        elif q1 == 'O' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == '5' and q6 == '6' and q7 == '7' and q8 == '8' and q9 == 'X':
            opcao = '7'
        elif q1 == 'O' and q2 == '2' and q3 == '3' and q4 == 'X' and q5 == '5' and q6 == '6' and q7 == 'O' and q8 == '8' and q9 == 'X':
            opcao = '3'
        elif q1 == 'X' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == 'O' and q6 == '6' and q7 == '7' and q8 == '8' and q9 == '9':
            opcao = '9'
        elif q1 == 'X' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == 'O' and q6 == 'X' and q7 == '7' and q8 == '8' and q9 == 'O':
            opcao = '7'
        elif q1 == 'X' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == 'O' and q6 == '6' and q7 == '7' and q8 == 'X' and q9 == 'O':
            opcao = '3'
        elif q1 == '1' and q2 == 'X' and q3 == '3' and q4 == '4' and q5 == 'O' and q6 == '6' and q7 == '7' and q8 == '8' and q9 == '9':
            opcao = '7'
        elif q1 == '1' and q2 == '2' and q3 == 'X' and q4 == '4' and q5 == 'O' and q6 == '6' and q7 == '7' and q8 == '8' and q9 == '9':
            opcao = '7'
        elif q1 == '1' and q2 == '2' and q3 == 'X' and q4 == 'X' and q5 == 'O' and q6 == '6' and q7 == 'O' and q8 == '8' and q9 == '9':
            opcao = '9'
        elif q1 == '1' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == 'O' and q6 == '6' and q7 == 'O' and q8 == 'X' and q9 == '9':
            opcao = '1'
        elif q1 == '1' and q2 == '2' and q3 == '3' and q4 == 'X' and q5 == 'O' and q6 == '6' and q7 == '7' and q8 == '8' and q9 == '9':
            opcao = '3'
        elif q1 == '1' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == 'O' and q6 == 'X' and q7 == '7' and q8 == '8' and q9 == '9':
            opcao = '1'
        elif q1 == '1' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == 'O' and q6 == '6' and q7 == 'X' and q8 == '8' and q9 == '9':
            opcao = '3'
        elif q1 == '1' and q2 == 'X' and q3 == 'O' and q4 == '4' and q5 == 'O' and q6 == '6' and q7 == 'X' and q8 == '8' and q9 == '9':
            opcao = '9'
        elif q1 == '1' and q2 == '2' and q3 == 'O' and q4 == '4' and q5 == 'O' and q6 == 'X' and q7 == 'X' and q8 == '8' and q9 == '9':
            opcao = '1'
        elif q1 == '1' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == 'O' and q6 == '6' and q7 == '7' and q8 == 'X' and q9 == '9':
            opcao = '3'
        elif q1 == '1' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == 'O' and q6 == '6' and q7 == '7' and q8 == '8' and q9 == 'X':
            opcao = '1'
        elif q1 == 'O' and q2 == 'X' and q3 == '3' and q4 == '4' and q5 == 'O' and q6 == '6' and q7 == '7' and q8 == '8' and q9 == 'X':
            opcao = '7'
        elif q1 == 'O' and q2 == '2' and q3 == '3' and q4 == 'X' and q5 == 'O' and q6 == '6' and q7 == '7' and q8 == '8' and q9 == 'O':
            opcao = '3'
        elif q1 == 'X' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == '5' and q6 == '6' and q7 == '7' and q8 == 'O' and q9 == '9':
            opcao = '7'
        elif q1 == '1' and q2 == 'X' and q3 == '3' and q4 == '4' and q5 == '5' and q6 == '6' and q7 == '7' and q8 == 'O' and q9 == '9':
            opcao = '4'
        elif q1 == 'X' and q2 == 'X' and q3 == 'O' and q4 == 'O' and q5 == '5' and q6 == 'X' and q7 == '7' and q8 == 'O' and q9 == '9':
            opcao = '7'
        elif q1 == '1' and q2 == 'X' and q3 == '3' and q4 == 'O' and q5 == 'X' and q6 == '6' and q7 == '7' and q8 == 'O' and q9 == '9':
            opcao = '7'
        elif q1 == '1' and q2 == 'X' and q3 == '3' and q4 == 'O' and q5 == '5' and q6 == 'X' and q7 == '7' and q8 == 'O' and q9 == '9':
            opcao = '7'
        elif q1 == '1' and q2 == 'X' and q3 == '3' and q4 == 'O' and q5 == '5' and q6 == '6' and q7 == 'X' and q8 == 'O' and q9 == '9':
            opcao = '1'
        elif q1 == '1' and q2 == 'X' and q3 == '3' and q4 == 'O' and q5 == '5' and q6 == '6' and q7 == '7' and q8 == 'O' and q9 == 'X':
            opcao = '5'
        elif q1 == '1' and q2 == '2' and q3 == 'X' and q4 == '4' and q5 == '5' and q6 == '6' and q7 == '7' and q8 == 'O' and q9 == '9':
            opcao = '9'
        elif q1 == '1' and q2 == '2' and q3 == '3' and q4 == 'X' and q5 == '5' and q6 == '6' and q7 == '7' and q8 == 'O' and q9 == '9':
            opcao = '5'
        elif q1 == '1' and q2 == 'X' and q3 == '3' and q4 == 'X' and q5 == 'O' and q6 == '6' and q7 == '7' and q8 == 'O' and q9 == '9':
            opcao = '9'
        elif q1 == '1' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == 'X' and q6 == '6' and q7 == '7' and q8 == 'O' and q9 == '9':
            opcao = '1'
        elif q1 == 'O' and q2 == 'X' and q3 == '3' and q4 == '4' and q5 == 'X' and q6 == '6' and q7 == '7' and q8 == 'O' and q9 == '9':
            opcao = '7'
        elif q1 == 'O' and q2 == 'X' and q3 == '3' and q4 == 'X' and q5 == 'X' and q6 == 'O' and q7 == '7' and q8 == 'O' and q9 == '9':
            opcao = '9'
        elif q1 == 'O' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == 'X' and q6 == '6' and q7 == '7' and q8 == 'O' and q9 == 'X':
            opcao = '7'
        elif q1 == '1' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == '5' and q6 == 'X' and q7 == '7' and q8 == 'O' and q9 == '9':
            opcao = '9'
        elif q1 == '1' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == '5' and q6 == 'X' and q7 == 'X' and q8 == 'O' and q9 == 'O':
            opcao = '5'
        elif q1 == '1' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == '5' and q6 == '6' and q7 == 'X' and q8 == 'O' and q9 == '9':
            opcao = '1'
        elif q1 == 'O' and q2 == 'X' and q3 == '3' and q4 == '4' and q5 == '5' and q6 == '6' and q7 == 'X' and q8 == 'O' and q9 == '9':
            opcao = '5'
        elif q1 == 'O' and q2 == '2' and q3 == '3' and q4 == 'X' and q5 == '5' and q6 == '6' and q7 == 'X' and q8 == 'O' and q9 == '9':
            opcao = '5'
        elif q1 == 'O' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == '5' and q6 == 'X' and q7 == 'X' and q8 == 'O' and q9 == '9':
            opcao = '5'
        elif q1 == 'O' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == '5' and q6 == '6' and q7 == 'X' and q8 == 'O' and q9 == 'X':
            opcao = '2'
        elif q1 == '1' and q2 == '2' and q3 == '3' and q4 == '4' and q5 == '5' and q6 == '6' and q7 == '7' and q8 == 'O' and q9 == 'X':
            opcao = '3'
        elif q1 == '1' and q2 == 'X' and q3 == 'O' and q4 == '4' and q5 == '5' and q6 == '6' and q7 == '7' and q8 == 'O' and q9 == 'X':
            opcao = '4'
        elif q1 == '1' and q2 == 'X' and q3 == 'O' and q4 == 'O' and q5 == '5' and q6 == 'X' and q7 == '7' and q8 == 'O' and q9 == 'X':
            opcao = '7'   
        elif q1 == '1' and q2 == 'X' and q3 == 'O' and q4 == 'O' and q5 == '5' and q6 == '6' and q7 == 'X' and q8 == 'O' and q9 == 'X':
            opcao = '5'
        elif q1 == 'O' and q2 == 'X' and q3 == 'O' and q4 == '4' and q5 == '5' and q6 == 'X' and q7 == '7' and q8 == 'O' and q9 == 'X':
            opcao = '7'

        else:
            opcao = random.choice(lista)

        
        
        
    

    jogadas += 1
    IA()
    if opcao == '1':
        if q1 == '1':    
            q1 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                IA()
            condicaoO()
                
                
    elif opcao == '2':
        if q2 == '2':    
            q2 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                IA()
            condicaoO()
    elif opcao == '3':
        if q3 == '3':    
            q3 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                IA()
            condicaoO()    
    elif opcao == '4':
        if q4 == '4':    
            q4 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                IA()
            condicaoO()    
    elif opcao == '5':
        if q5 == '5':    
            q5 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                IA()
            condicaoO()    
    elif opcao == '6':
        if q6 == '6':    
            q6 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                IA()
            condicaoO()    
    elif opcao == '7':
        if q7 == '7':    
            q7 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                IA()
            condicaoO()    
    elif opcao == '8':
        if q8 == '8':    
            q8 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                IA()
            condicaoO()    
    elif opcao == '9':
        if q9 == '9':    
            q9 = 'O'
        else:
            while opcao != q1 and opcao != q2 and opcao != q3 and opcao != q4 and opcao != q5 and opcao != q6 and opcao != q7 and opcao != q8 and opcao != q9:
                IA()
            condicaoO()   
    verificadorIAdificil()
# ----------------- JOGO -----------------

# ----verificador----
def verificador():
    global q1
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global pontosX
    global pontosO
    global jogadas
    global empates

    # X ganhou?
    def opcoes():
        opcao = input('sua opcao: ')
        if opcao == '1':
            player_vs_player()
        elif opcao == '2':
            tela_inicio()
        else:
            while opcao != '1' and opcao != '2':
                print('ERRO! Escolha um opcao existente.')
                opcao = input('sua opcao: ').strip()
            if opcao == '1':
              player_vs_player()
            elif opcao == '2':
              tela_inicio()
    def opcoesO():
        opcao = input('sua opcao: ')
        if opcao == '1':
            player_vs_playerO()
        elif opcao == '2':
            tela_inicio()
        else:
            while opcao != '1' and opcao != '2':
                print('ERRO! Escolha um opcao existente.')
                opcao = input('sua opcao: ').strip()
            if opcao == '1':
                player_vs_playerO()
            elif opcao == '2':
                tela_inicio()
    def opcoesE():
        opcao = input('sua opcao: ')
        if opcao == '1':
            if empates % 2 == 0:
                player_vs_player()
            elif empates % 2 == 1:
                player_vs_playerO()
        elif opcao == '2':
            tela_inicio()
        else:
            while opcao != '1' and opcao != '2':
                print('ERRO! Escolha um opcao existente.')
                opcao = input('sua opcao: ').strip()
            if opcao == '1':
                if empates % 2 == 0:
                    player_vs_player()
                elif empates % 2 == 1:
                    player_vs_playerO()
            elif opcao == '2':
                tela_inicio()
    if q1 == 'X' and q2 == 'X' and q3 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()
    elif q4 == 'X' and q5 == 'X' and q6 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()
    elif q7 == 'X' and q8 == 'X' and q9 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()
    elif q1 == 'X' and q4 == 'X' and q7 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()
    elif q2 == 'X' and q5 == 'X' and q8 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()
    elif q3 == 'X' and q6 == 'X' and q9 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()
    elif q1 == 'X' and q5 == 'X' and q9 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()
    elif q7 == 'X' and q5 == 'X' and q3 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()

    # O ganhou?
    elif q1 == 'O' and q2 == 'O' and q3 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesO()
    elif q4 == 'O' and q5 == 'O' and q6 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesO()
    elif q7 == 'O' and q8 == 'O' and q9 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesO()
    elif q1 == 'O' and q4 == 'O' and q7 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesO()
    elif q2 == 'O' and q5 == 'O' and q8 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesO()
    elif q3 == 'O' and q6 == 'O' and q9 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesO()
    elif q1 == 'O' and q5 == 'O' and q9 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesO()
    elif q7 == 'O' and q5 == 'O' and q3 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()

    # empate?
    elif jogadas == 9:
        empates += 1
        img_empate()
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesE()
def verificadorIAfacil():
    global q1
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global pontosX
    global pontosO
    global jogadas
    global empates

    # X ganhou?
    def opcoes():
        opcao = input('sua opcao: ')
        if opcao == '1':
            player_vs_IAfacil()
        elif opcao == '2':
            tela_inicio()
        else:
            while opcao != '1' and opcao != '2':
                print('ERRO! Escolha um opcao existente.')
                opcao = input('sua opcao: ').strip()
            if opcao == '1':
                player_vs_IAfacil()
            elif opcao == '2':
                tela_inicio()
    def opcoesO():
        opcao = input('sua opcao: ')
        if opcao == '1':
            player_vs_IAOfacil()
        elif opcao == '2':
            tela_inicio()
        else:
            while opcao != '1' and opcao != '2':
                print('ERRO! Escolha um opcao existente.')
                opcao = input('sua opcao: ').strip()
            if opcao == '1':
                player_vs_IAOfacil()
            elif opcao == '2':
                tela_inicio()
    def opcoesE():
        opcao = input('sua opcao: ')
        if opcao == '1':
            if empates % 2 == 0:
                player_vs_IAfacil()
            elif empates % 2 == 1:
                player_vs_IAOfacil()
        elif opcao == '2':
            tela_inicio()
        else:
            while opcao != '1' and opcao != '2':
                print('ERRO! Escolha um opcao existente.')
                opcao = input('sua opcao: ').strip()
            if opcao == '1':
                if empates % 2 == 0:
                    player_vs_IAfacil()
                elif empates % 2 == 1:
                    player_vs_IAOfacil()
            elif opcao == '2':
                tela_inicio()
    if q1 == 'X' and q2 == 'X' and q3 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()
    elif q4 == 'X' and q5 == 'X' and q6 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()
    elif q7 == 'X' and q8 == 'X' and q9 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()
    elif q1 == 'X' and q4 == 'X' and q7 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()
    elif q2 == 'X' and q5 == 'X' and q8 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()
    elif q3 == 'X' and q6 == 'X' and q9 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()
    elif q1 == 'X' and q5 == 'X' and q9 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()
    elif q7 == 'X' and q5 == 'X' and q3 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()

    # O ganhou?
    elif q1 == 'O' and q2 == 'O' and q3 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesO()
    elif q4 == 'O' and q5 == 'O' and q6 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesO()
    elif q7 == 'O' and q8 == 'O' and q9 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesO()
    elif q1 == 'O' and q4 == 'O' and q7 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesO()
    elif q2 == 'O' and q5 == 'O' and q8 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesO()
    elif q3 == 'O' and q6 == 'O' and q9 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesO()
    elif q1 == 'O' and q5 == 'O' and q9 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesO()
    elif q7 == 'O' and q5 == 'O' and q3 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()

    # empate?
    elif jogadas == 9:
        img_empate()
        empates += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesE()
def verificadorIAmedio():
    global q1
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global pontosX
    global pontosO
    global jogadas
    global empates
    # X ganhou?
    def opcoes():
        opcao = input('sua opcao: ')
        if opcao == '1':
            player_vs_IAmedio()
        elif opcao == '2':
            tela_inicio()
        else:
            while opcao != '1' and opcao != '2':
                print('ERRO! Escolha um opcao existente.')
                opcao = input('sua opcao: ').strip()
            if opcao == '1':
                player_vs_IAmedio()
            elif opcao == '2':
                tela_inicio()
    def opcoesO():
        opcao = input('sua opcao: ')
        if opcao == '1':
            player_vs_IAOmedio()
        elif opcao == '2':
            tela_inicio()
        else:
            while opcao != '1' and opcao != '2':
                print('ERRO! Escolha um opcao existente.')
                opcao = input('sua opcao: ').strip()
            if opcao == '1':
                player_vs_IAOmedio()
            elif opcao == '2':
                tela_inicio()
    def opcoesE():
        opcao = input('sua opcao: ')
        if opcao == '1':
            if empates % 2 == 0:
                player_vs_IAmedio()
            elif empates % 2 == 1:
                player_vs_IAOmedio()
        elif opcao == '2':
            tela_inicio()
        else:
            while opcao != '1' and opcao != '2':
                print('ERRO! Escolha um opcao existente.')
                opcao = input('sua opcao: ').strip()
            if opcao == '1':
                if empates % 2 == 0:
                    player_vs_IAmedio()
                elif empates % 2 == 1:
                    player_vs_IAOmedio()
            elif opcao == '2':
                tela_inicio()
    if q1 == 'X' and q2 == 'X' and q3 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()
    elif q4 == 'X' and q5 == 'X' and q6 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()
    elif q7 == 'X' and q8 == 'X' and q9 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()
    elif q1 == 'X' and q4 == 'X' and q7 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()
    elif q2 == 'X' and q5 == 'X' and q8 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()
    elif q3 == 'X' and q6 == 'X' and q9 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()
    elif q1 == 'X' and q5 == 'X' and q9 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()
    elif q7 == 'X' and q5 == 'X' and q3 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()

    # O ganhou?
    elif q1 == 'O' and q2 == 'O' and q3 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesO()
    elif q4 == 'O' and q5 == 'O' and q6 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesO()
    elif q7 == 'O' and q8 == 'O' and q9 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesO()
    elif q1 == 'O' and q4 == 'O' and q7 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesO()
    elif q2 == 'O' and q5 == 'O' and q8 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesO()
    elif q3 == 'O' and q6 == 'O' and q9 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesO()
    elif q1 == 'O' and q5 == 'O' and q9 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesO()
    elif q7 == 'O' and q5 == 'O' and q3 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()

    # empate?
    elif jogadas == 9:
        img_empate()
        empates += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesE()
def verificadorIAdificil():
    global q1
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global pontosX
    global pontosO
    global jogadas
    global empates
    # X ganhou?
    def opcoes():
        opcao = input('sua opcao: ')
        if opcao == '1':
            player_vs_IAdificil()
        elif opcao == '2':
            tela_inicio()
        else:
            while opcao != '1' and opcao != '2':
                print('ERRO! Escolha um opcao existente.')
                opcao = input('sua opcao: ').strip()
            if opcao == '1':
                player_vs_IAdificil()
            elif opcao == '2':
                tela_inicio()
    def opcoesO():
        opcao = input('sua opcao: ')
        if opcao == '1':
            player_vs_IAOdificil()
        elif opcao == '2':
            tela_inicio()
        else:
            while opcao != '1' and opcao != '2':
                print('ERRO! Escolha um opcao existente.')
                opcao = input('sua opcao: ').strip()
            if opcao == '1':
                player_vs_IAOdificil()
            elif opcao == '2':
                tela_inicio()
    def opcoesE():
        opcao = input('sua opcao: ')
        if opcao == '1':
            if empates % 2 == 0:
                player_vs_IAdificil()
            elif empates % 2 == 1:
                player_vs_IAOdificil()
        elif opcao == '2':
            tela_inicio()
        else:
            while opcao != '1' and opcao != '2':
                print('ERRO! Escolha um opcao existente.')
                opcao = input('sua opcao: ').strip()
            if opcao == '1':
                if empates % 2 == 0:
                    player_vs_IAdificil()
                elif empates % 2 == 1:
                    player_vs_IAOdificil()
            elif opcao == '2':
                tela_inicio()
    if q1 == 'X' and q2 == 'X' and q3 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()
    elif q4 == 'X' and q5 == 'X' and q6 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()
    elif q7 == 'X' and q8 == 'X' and q9 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()
    elif q1 == 'X' and q4 == 'X' and q7 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()
    elif q2 == 'X' and q5 == 'X' and q8 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()
    elif q3 == 'X' and q6 == 'X' and q9 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()
    elif q1 == 'X' and q5 == 'X' and q9 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()
    elif q7 == 'X' and q5 == 'X' and q3 == 'X':
        img_X_venceu()
        pontosX += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoes()

    # O ganhou?
    elif q1 == 'O' and q2 == 'O' and q3 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesO()
    elif q4 == 'O' and q5 == 'O' and q6 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesO()
    elif q7 == 'O' and q8 == 'O' and q9 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesO()
    elif q1 == 'O' and q4 == 'O' and q7 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesO()
    elif q2 == 'O' and q5 == 'O' and q8 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesO()
    elif q3 == 'O' and q6 == 'O' and q9 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesO()
    elif q1 == 'O' and q5 == 'O' and q9 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesO()
    elif q7 == 'O' and q5 == 'O' and q3 == 'O':
        img_O_venceu()
        pontosO += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesO()

    # empate?
    elif jogadas == 9:
        img_empate()
        empates += 1
        jogadas = 0
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        opcoesE()
# ----player vs player---- 
def player_vs_player():
    for c in range(1, 6):
        img_jogo_da_velha()
        jogadaX()
        img_jogo_da_velha()
        jogadaO()
def player_vs_playerO():
    for c in range(1, 6):
        img_jogo_da_velha()
        jogadaO()
        img_jogo_da_velha()
        jogadaX()

        


# ----player vs IA---- 
def player_vs_IA(): 
    img_tela_escolher_IA()
    opcao = input('sua opcao: ')
    if opcao == '1':
        player_vs_IAfacil()
    elif opcao == '2':
        player_vs_IAmedio()
    elif opcao == '3':
        player_vs_IAdificil()
    elif opcao == '/menu':
        tela_inicio()
    else:
        while opcao != '1' and opcao != '2' and opcao != '3' and opcao != '/menu':
            print('ERRO! Escolha uma opcao existente')
            opcao = input('sua opcao: ')
        if opcao == '1':
            player_vs_IAfacil()
        elif opcao == '2':
            player_vs_IAmedio()
        elif opcao == '3':
            player_vs_IAdificil()
        elif opcao == '/menu':
            tela_inicio()


def player_vs_IAfacil():
    for c in range(1, 6):
            img_jogo_da_velha()
            jogadaXIAfacil()
            img_jogo_da_velha()
            jogadaIAfacil()  
def player_vs_IAOfacil():
    for c in range(1, 6):
            img_jogo_da_velha()
            jogadaIAfacil()
            img_jogo_da_velha()
            jogadaXIAfacil() 
   
def player_vs_IAmedio():
    for c in range(1, 6):
        img_jogo_da_velha()
        jogadaXIAmedio()
        img_jogo_da_velha()
        jogadaIAmedio()
def player_vs_IAOmedio():
    for c in range(1, 6):
        img_jogo_da_velha()
        jogadaIAmedio()
        img_jogo_da_velha()
        jogadaXIAmedio()

def player_vs_IAdificil():
    for c in range(1, 6):
        img_jogo_da_velha()
        jogadaXIAdificil()
        img_jogo_da_velha()
        jogadaIAdificil()
def player_vs_IAOdificil():
    for c in range(1, 6):
        img_jogo_da_velha()
        jogadaIAdificil()
        img_jogo_da_velha()
        jogadaXIAdificil()
# ----tela inicio----
def tela_inicio():
    global pontosX
    global pontosO
    global jogadas
    global q1
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global empates
    q1 = '1'
    q2 = '2'
    q3 = '3'
    q4 = '4'
    q5 = '5'
    q6 = '6'
    q7 = '7'
    q8 = '8'
    q9 = '9'
    pontosX = 0
    pontosO = 0
    jogadas = 0
    empates = 0
    img_tela_inicio()
    opcao = input('sua opcao: ').strip()
    if opcao == '1':
        player_vs_player()
    elif opcao == '2':
        player_vs_IA()
    else:
        while opcao != '1' and opcao != '2':
            print('ERRO! Escolha um opcao existente.')
            opcao = input('sua opcao: ').strip()
        if opcao == '1':
            player_vs_player()
        elif opcao == '2':
            player_vs_IA()

tela_inicio()

