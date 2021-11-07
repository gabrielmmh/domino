# Nao esquecer de desligar o jogo atraves de 'jogar = False'

#posiciona a peca na mesa
def adiciona_na_mesa(peca,mesa):
    y=len(mesa)
    if y==0:
        mesa.append(peca)
        
    else:
        e = peca[0]
        d = peca[1]

        y=len(mesa)
        esq = mesa[0][0]
        

        di= mesa[y-1][1]
        

        if d == esq:
            mesa.insert(0,peca)
        if d == di:
            peca=[d,e]
            mesa.append(peca)
        
        if e == di:
            mesa.append(peca)
        if e == esq:
            peca = [d,e]
            mesa.insert(0,peca)
        
        
    return mesa
#calcula os pontos do jogadores
def soma_pecas(lista):
    soma=0
    for pecas in lista:
        soma+=sum(pecas)
    return soma

# Identifica o indice da mao dos jogadores 
def posicoes_possiveis(mesa,lista_pecas):
    possivel=[]
    i=0
    if len(mesa) == 0:
        while i < len(lista_pecas):
            possivel.append(i)
            i+=1
            
        return possivel
    else:
        esquerda=mesa[0][0]
        direita=mesa[len(mesa)-1][1]
        
        for pecas in lista_pecas:
            if pecas[0] == esquerda or pecas[1] == esquerda or pecas[0] == direita or pecas[1] == direita:
                possivel.append(lista_pecas.index(pecas))
        
        return possivel


import random
jogar = True
while jogar:
    pergunta=str(input('Deseja jogar domino dos Deuses?  Responda com "sim" ou "nao"  '))
    if pergunta == 'nao':
        print('Então pq tentou?')
        jogar = False
        
        
    if pergunta == 'sim':
        
        num_players=int(input('Para quantos queres perder? (2 a 4 jogadores) '))

        # criando as peças
        pecas=[]
        a=0
        b=0
        
        while len(pecas)<28:
            x=[]
            a=random.randint(0,6)
            b=random.randint(0,6)
            x.append(a)
            x.append(b)
            
            if x not in pecas:
                pecas.append(x)
        random.shuffle(pecas)

        # pecas finalizdas armazenadas em  lista --> 'pecas' utilizando a , b

        # Criando as variaveis do jogo
        jogadores={}
        monte=[]
        mesa=[]

        situacao_do_jogo={
            'jogadores':jogadores,
            'monte':monte,
            'mesa':mesa
        }

        # Criando as 'maos' no dic jogadores de acordo com o num de players
        i=0
        while i < num_players:
            jogadores[i]=[]
            i+=1
        
        # Dividindo as peças entre os jogadores
        d=0
        cont=0
        while len(jogadores[num_players-1])<7:
            jogadores[d].append(pecas[0])
            pecas.pop(0)
            cont+=1
            if cont > 0 and cont % 7 == 0:
                d += 1
        
        # O resto vai para o monte
        for p in pecas:
            monte.append(p)
        

        # Imprime a mao dos players    
        i=0
        while i < num_players:
            print('Peças do Player {}: {}'.format(i, jogadores[i]))
            i += 1
        
        #Loop ate existir um vencedor
        # Vence quem nao tiver pecas na mao, logo
        mais_rodadas  = True
        pontos={}
        print('Mesa:  {} '.format(mesa))

        while mais_rodadas:
            

           
             
            print('Mesa:  {} '.format(mesa))

            #condicao -->  if pecas possiveis nao existir and  len(mesa) == 0
            i=0
            while i < num_players:
                if i in jogadores.keys():
                    #############################################################
                    if i == num_players - 1:
                        # situacao em que e o round do player fisico
                        
                        print('Sua vez doidao, voce tem {} \nSuas peca(s) sao: {}'.format(len(jogadores[i]),(jogadores[i])))

                        
                        
                        possui_carta = True 
                        while possui_carta:
                            possivel=posicoes_possiveis(mesa,jogadores[i])
                            
                            if len(possivel) == 0 and len(monte)==0:
                                # jogador nao pode mais continuar
                                print('Parabens por ser horrivel \nPlayers {} esta eliminado \nCaso nessa rodada nenhum tenha colocado uma peca, vc ainda pode ganhar'.format(i))
                                soma=soma_pecas(jogadores[i])
                                pontos[i]=soma
                                del jogadores[i]


                                possui_carta = False

                                



                            if len(possivel) == 0 and len(monte) > 0:
                                
                                print('Voce n tem uma q serve, vai pegar do monte')
                                jogadores[i].append(monte[0])
                                monte.pop(0)

                            else:
                                correto = True
                                while correto:
                                    print(mesa)
                                    print('As pecas possiveis sao: {} '.format(possivel))
                                    q=int(input('Escolha uma peca(lembrando que a posicao da primeira peca em sua mao e 0):  '))
                                    if q not in possivel:
                                        print('Escolhe direito pff, nao te aguento mais')
                                    if q in possivel:
                                        
                                        adiciona_na_mesa(jogadores[i][q],mesa)
                                        jogadores[i].pop(q)

                                        
                                        

                                        print(mesa)
                                        correto  = False
                                        possui_carta = False

                                # a = peca escolhida, agr alocar a peca




                        


                    ################################################
                    else:
                        #vez do computador

                        print('Vez do Jogador {}, \nEle tem: {} peca(s) '.format(i,len(jogadores[i])))

                        possui_carta = True
                        while possui_carta:
                            possivel=posicoes_possiveis(mesa,jogadores[i])
                            
                            if len(possivel) == 0 and len(monte)==0:
                                # jogador nao pode mais continuar
                                print('Parabens por ser horrivel \nPlayers {} esta eliminado \nCaso nessa rodada nenhum tenha colocado uma peca, vc ainda pode ganhar'.format(i))
                                soma=soma_pecas(jogadores[i])
                                pontos[i]=soma
                                del jogadores[i]


                                possui_carta = False

                                



                            if len(possivel) == 0 and len(monte) > 0:
                                
                                print('Voce n tem uma q serve, vai pegar do monte')
                                jogadores[i].append(monte[0])
                                monte.pop(0)

                            else:
                                correto = True
                                while correto:
                                    q=random.randint(0,6)
                                    if q not in possivel:
                                        print('Calma que o computador ta burro')
                                    if q in possivel:
                                        
                                        adiciona_na_mesa(jogadores[i][q],mesa)
                                        
                                        
                                            
                                        print(mesa)
                                        

                                        correto  = False
                                        possui_carta = False

                    

    
                vencedores=[]
                #verificando vencedor ( como pode haver mais de 1 'vencedor')
                for player,mao in jogadores.items():

                    if len(mao) == 0:
        
                        print('Parabens ao jogador {}, ele e o unico que presta'.format(player))
                        mais_rodadas = False
                        jogar = False

               
                i+=1
            
                
            

            





        
    # Resposta invalida no inicio do jogo
    if pergunta != 'sim' and pergunta != 'nao':
        print('Responde direito animal')
        jogar = True
    

    



                    