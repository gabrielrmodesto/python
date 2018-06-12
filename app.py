# -*- coding: UTF-8 -*-
import re

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

def alterar(nomes):
	print 'Qual o nome deseja alterar?'
	nome_alterar = raw_input()
	if(nome_alterar in nomes):
		posicao = nomes.index(nome_alterar)
		print 'Novo nome: '
		novo_nome = raw_input()
		nomes[posicao] = novo_nome
	
def procurar(nomes):
	print 'Qual nome voce quer procurar?'
	busca = raw_input()
	if(busca in nomes):
		print 'O nome %s esta cadastrado' % busca
	else:
		print 'O nome %s nao existe' % busca

def procurar_regex(nomes):
	print('Digite a expressao regular')
	regex = raw_input()
	regex_concatenado = ''.join(regex)
	resultado = re.findall(regex, regex_concatenado)
	print resultado

def menu():
	nomes = []
	escolha = ''
	while (escolha != '0'):
		print 'Digite:\n 1 para cadastrar\n 2 para listar\n 3 para remover\n 4 para alterar \n 5 para procurar\n 6 para expressao\n 0 para encerrar'
		escolha = raw_input()
		if(escolha == '1'):
			cadastrar(nomes)
		if(escolha == '2'):
			listar(nomes)
		if(escolha == '3'):
			remover(nomes)
		if(escolha == '4'):
			alterar(nomes)
		if(escolha == '5'):
			procurar(nomes)
		if(escolha == '6'):
			procurar_regex(nomes)

menu()