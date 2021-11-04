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
            print(x)
            if x not in pecas:
                pecas.append(x)
        random.shuffle(pecas)

        # pecas finalizdas armazenadas em  lista --> 'pecas' utilizando a , b
    



    if pergunta != 'sim' and pergunta != 'nao':
        print('Responde direito animal')
        jogar = True 



    
    
    
        
