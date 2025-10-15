global estoque_comida
global estoque_bebida

estoque_bebida = {"refrigerante": 10, "suco de uva": 8, "achocolatado": 7, "leite": 5, "café": 5, "suco de laranja": 5, "suco de morango": 5, "suco de acerola": 5, "suco de melancia": 5, "suco de maça": 5}
estoque_comida = {"sanduiche": 5, "bolo": 6, "cafe": 15, "brigadeiro": 5, "uva": 5, "banana": 5, "strogonoff de peixe": 5, "strogonoff de carne": 5, "strogonoff de frango": 5, "strogonoff de camarão": 5,}

def mostrar_estoque():
  opcao = input("Deseja mostrar o estoque de comida ou bebida? ")
  if opcao == "comida":
    print(f"Estoque de comida: {estoque_comida}")
  elif opcao == "bebida":
    print(f"Estoque de bebida: {estoque_bebida}")
  menu()
#
def adicionar_produto():
  produto = input("Digite o nome do produto que deseja adicionar: ")
  quantidade = int(input("Digite a quantidade a ser adicionada: "))
  opcao = input('Deseja adicionar o produto ao estoque de comida ou bebida? ')
  if opcao == 'comida':
    if produto in estoque_comida:
      estoque_comida[produto] += quantidade
    else:
        estoque_comida[produto] = quantidade

  if opcao == 'bebida':
    if produto in estoque_bebida:
        estoque_bebida[produto] += quantidade
    else:
      estoque_bebida[produto] = quantidade
  else:
    print('Opção inválida.')
  menu()

def remover_produto():
  produto = input("Digite o nome do produto que deseja remover: ")
  quantidade = int(input("Digite a quantidade a ser removida: "))
  opcao = input("Deseja remover o produto do estoque de comida ou bebida? ")
  if opcao == "comida":
    if produto in estoque_comida:
      if estoque_comida[produto] >= quantidade:
        estoque_comida[produto] -= quantidade
        if estoque_comida[produto] == 0:
          del estoque_comida[produto]
      else:
        print("Quantidade insuficiente em estoque.")
    else:
        print("Produto não encontrado no estoque.")
  elif opcao == "bebida":
    if produto in estoque_bebida:
      if estoque_bebida[produto] >= quantidade:
        estoque_bebida[produto] -= quantidade
        if estoque_bebida[produto] == 0:
          del estoque_bebida[produto]
      else:
        print("Quantidade insuficiente em estoque.")
    else:
      print("Produto não encontrado no estoque.")
  else:
    print("Opção inválida.")
  menu()

def consultar_produto():
  opcao = input("Deseja consultar o estoque de comida ou bebida? ")
  if opcao == "comida":
    produto = input("Digite o nome do produto que deseja consultar: ")
    if produto in estoque_comida:
      print(f"Produto: {produto}, Quantidade: {estoque_comida[produto]}")
    elif produto not in estoque_comida:
      print("Produto não encontrado no estoque.")
  elif opcao == "bebida":
    produto = input("Digite o nome do produto que deseja consultar: ")
    if produto in estoque_bebida:
        print(f"Produto: {produto}, Quantidade: {estoque_bebida[produto]}")
    elif produto not in estoque_bebida:
        print("Produto não encontrado no estoque.")
  else:
    print("Opção inválida.")
    menu()
  menu()

def menu():
  print("\n=======MENU=======\n1.Mostrar Estoque\n2.Adicionar Produto\n3.Remover Produto\n4.Consultar Produto\n5.Salvar Relatório\n6.Repor Automático\n7.Sair")
  print("==================")
  opcao = input('Escolha a opção que deseja: ')
  if opcao == '1':
    mostrar_estoque()
  elif opcao == '2':
    adicionar_produto()
  elif opcao == '3':
    remover_produto()
  elif opcao == '4':
    consultar_produto()
  elif opcao == '5':
    salvar_relatorio()
  elif opcao == '6':
    repor_automatico()
  elif opcao == '7':
    print("Saindo do programa...")
    exit()
  else:
    print('Opção inválida')
    menu()

def salvar_relatorio():
  opcao = input("Deseja salvar o relatório? ")
  if opcao == 'sim':
    with open('estoque.txt', 'w') as f:
      f.write('Estoque de comida:\n')
      for produto, quantidade in estoque_comida.items():
        f.write(f'{produto}: {quantidade}\n')
      f.write('\nEstoque de bebida:\n')
      for produto, quantidade in estoque_bebida.items():
        f.write(f'{produto}: {quantidade}\n')
  elif opcao == 'não':
    print("Voltando...")
  else:
    print('Opção inválida')
    menu()
  menu()
def repor_automatico():
  opcao = input("Deseja repor o estoque automaticamente? ")
  if opcao == "sim":
      opcao = input("Deseja repor o estoque de comida ou bebida? ")
      if opcao == "comida":
        for produto, quantidade in estoque_comida.items():
          if quantidade < 3:
            estoque_comida[produto] += 5
      if opcao == "bebida":
        for produto, quantidade in estoque_bebida.items():
          if quantidade < 3:
            estoque_bebida[produto] += 5
  elif opcao == "não":
      print("Voltando...")
  else:
      print('Opção inválida')
      menu()
  menu()

menu()