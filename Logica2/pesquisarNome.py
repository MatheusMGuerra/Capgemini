#Alimentação do vetor
nomes = []
def aliemntarNomes():
    for i in range(0, 2):
        nomes.append(input('Informe o nome do cliente {}'.format(i+1)))

#Pesquisa
def pesquisarNome():
    encontrado = False
    pesquisa = input('Informe o nome do cliente que deseja buscar no sistema: ')
    for i in range(0, 2):
        if pesquisa == nomes[i]:
            encontrado = True
    nomeEncontrado(encontrado, pesquisa)

def nomeEncontrado(valorLogico, nomeCliente):
    if valorLogico:
        print('{} está cadastrado no sistema.'.format(nomeCliente))
    else:
        print('{} não está cadastrado no sistema.'.format(nomeCliente))


#main
aliemntarNomes()
pesquisarNome()