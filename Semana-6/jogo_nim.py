#
def computador_escolhe_jogada (n,m):
    i = 1
    multi = (m+1) * i #3 
    if n<multi:
        retira_multi = n
    else:
        retira_multi = n-multi #1 2-3 = -1
    while(multi != 0):
        if retira_multi >= m: #1>=2
            pecas = n-m
            print("O computador tirou",m,"peças.")
            print("Agora restam",pecas,"peças no tabuleiro")
            if pecas != 0:
                n = pecas
                usuario_escolhe_jogada(n,m)
            else:
                print("Fim do jogo! O computador ganhou!")
            break 

        if retira_multi < m:#1<2
            pecas = n - retira_multi#4-1 = 3
            print("O computador tirou",retira_multi,"peças.")
            print("Agora restam",pecas,"peças no tabuleiro")
            if pecas != 0:
                n = pecas#n=3
                usuario_escolhe_jogada(n,m)
            else:
                print("Fim do jogo! O computador ganhou!")
            break 
        i = i+1
        multi = (m+1) * i
    
    #pecas = n-m
    #print("O computador tirou",m,"peças.")
    #print("Agora restam",pecas,"peças no tabuleiro")
    
    #if pecas != 0:
    #    n = pecas
    #    usuario_escolhe_jogada(n,m)
    #else:
    #    print("Fim do jogo! O computador ganhou!")
    return


def  usuario_escolhe_jogada(n,m):
    user_pecas = int(input("Digite quantas peças você quer remover na jogada (M)"))
    while (user_pecas>m):
        user_pecas = int(input("Valor inválido!""\nDigite quantas peças você quer remover na jogada (M)"))

    restam = n-user_pecas
    print("Você tirou",user_pecas,"peça.")
    print("Agora restam",restam,"peças no tabuleiro")
    if restam != 0:
        n = restam
        computador_escolhe_jogada(n,m)
    else:
        print("Você ganhou!")
    return

#A função multiplo calcula se o n é multiplo de m+1 e informa quem vai começar o jogo --- ESTÁ FUNCIONANDO
    #n multiplo de m+1 ---> N=3 e M=1, M+1=2 logo N não é multiplo de M+1
    #n multiplo de m+1 ---> N=5 e M=4, M+1=5 logo N é multiplo de M+1
def multiplo (n,m):
    i = 1
    multi = (m+1) * i
    while(multi != 0):
        if multi > n:
            print("Computador começa")
            computador_escolhe_jogada(n,m)
            break
        if multi == n:
            print("Você começa:")
            usuario_escolhe_jogada(n,m)
            break
        i = i+1
        multi = (m+1) * i

#A função partida pede os valores iniciais para o usuário e chama a função múltiplo --- ESTÁ FUNCIONANDO
def partida ():
    n = int(input("Digite quantas peças existem no tabuleiro (N)"))
    m = int(input("Digite quantas peças serão removidas em cada jogada (M)"))
    multiplo(n,m)
    return m,n

def partida_unica():
    partida()
    return

def campeonato():
    partida ()
    return
    
def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    tipo = int(input("1 - para jogar uma partida isolada.""\n2 - para jogar um campeonato.""\n"))

    while((tipo < 1) or (tipo > 2)):
        print("Valor inválido, digite novamente:")
        tipo = int(input("1 - para jogar uma partida isolada.""\n2 - para jogar um campeonato.""\n"))

    if tipo == 1:
        print("Você escolheu partida única:")
        partida_unica()
    if tipo == 2:
        print("Você escolheu campeonato:")
        campeonato()
    return

main()