# -*- coding: UTF-8 -*-
def cadastrar(nomes):
	print 'Digite seu nome'
	nome = raw_input()
	nomes.append(nome)

def listar(nomes):
	print 'Lista de nomes'
	for nome in nomes:
		print nome

def remover(nomes):
	print 'Quem voce deseja tirar?'
	nome = raw_input()
	nomes.remove(nome)

def menu():
	nomes = []
	escolha = ''
	while (escolha != '0'):
		print 'Digite:\n 1 para cadastrar\n 2 para listar\n 3 para remover \n0 para encerrar'
		escolha = raw_input()
		if(escolha == '1'):
			cadastrar(nomes)
		if(escolha == '2'):
			listar(nomes)
		if(escolha == '3'):
			remover(nomes)

menu()