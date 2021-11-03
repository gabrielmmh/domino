pergunta=str(input('Deseja jogar domino dos Deuses?  Responda com "sim" ou "nao"  '))
if pergunta == 'nao':
    print('Então pq tentou?')
    
if pergunta == 'sim':
    num_players=int(input('Contando você, quantas pessoas irão jogar? (2 a 4 jogadores) '))
    players=[]
    while num_players>0:
        players.append(num_players)
        num_players-=1
        
