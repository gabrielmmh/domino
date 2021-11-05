# Nao esquecer de desligar o jogo atraves de 'jogar = False'

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
        
    # Resposta invalida no inicio do jogo
    if pergunta != 'sim' and pergunta != 'nao':
        print('Responde direito animal')
        jogar = True