# -*- coding: UTF-8 -*-

class Perfil(object):
	'Classe padrao para perfis de usuario'
	def __init__(self, nome, telefone, empresa):
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa
		self.__curtidas = 0

	def imprimir(self):
		print "Nome: %s\nTelefone: %s\nEmpresa: %s\nCurtidas: %s" % (self.nome,self.telefone,self.empresa,self.__curtidas)

	def curtir(self):
		self.__curtidas += 1

	def obter_curtidas(self):
		return self.__curtidas