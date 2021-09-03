import funcoesOrdenacao

def menu_inicio():
  opcao = 0
  while opcao != 4:
    print(''' 
    [ 1 ] Ordenação de lista decrescente;
    [ 2 ] Ordenação de lista com elementos aleatórios;
    [ 3 ] Ordenação de lista crescente;
    [ 4 ] Sair;
    ''')
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
      print('\nTempo de duração de cada método com lista de 100 elementos')
      funcoesOrdenacao.ordena_decrescente(100)
      print('\nTempo de duração de cada método com lista de 1000 elementos')
      funcoesOrdenacao.ordena_decrescente(1000)
      print('\nTempo de duração de cada método com lista de 5000 elementos')
      funcoesOrdenacao.ordena_decrescente(5000)
    elif opcao == 2:
      print('\nTempo de duração em segundos de cada método com lista de 100 elementos')
      funcoesOrdenacao.ordena_aleatorio(100)
      print('\nTempo de duração em segundos de cada método com lista de 1000 elementos')
      funcoesOrdenacao.ordena_aleatorio(1000)
      print('\nTempo de duração em segundos de cada método com lista de 5000 elementos')
      funcoesOrdenacao.ordena_aleatorio(5000)
    elif opcao == 3:
      print('\nTempo de duração em segundos de cada método com lista de 100 elementos')
      funcoesOrdenacao.ordena_crescente(100)
      print('\nTempo de duração em segundos de cada método com lista de 1000 elementos')
      funcoesOrdenacao.ordena_crescente(1000)
      print('\nTempo de duração em segundos de cada método com lista de 5000 elementos')
      funcoesOrdenacao.ordena_crescente(5000)
    elif opcao == 4:
      print('Finalizando...')
    else:
      print('Opção inválida. Tente novamente')
    print('=-=' *20)
  print('Fim do programa! Até logo.')
