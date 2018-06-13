# -*- coding: UTF-8 -*-

class Perfil(object):
	'Classe padrao para perfis de usuario'
	def __init__(self, nome, telefone, empresa,tipo):
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa
		self.__curtidas = 0
		self.__tipo = tipo

	def imprimir(self):
		print "Nome: %s\nTelefone: %s\nEmpresa: %s\nCurtidas: %s" % (self.nome,self.telefone,self.empresa,self.__curtidas)

	def curtir(self):
		self.__curtidas += 1

	def obter_curtidas(self):
		return self.__curtidas

	def obter_creditos(self):
		return self.__curtidas * 10.0

	def obter_tipo(self):
		return self.__tipo