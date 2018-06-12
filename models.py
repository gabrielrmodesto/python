# -*- coding: UTF-8 -*-

class Perfil(object):
	'Classe padrao para perfis de usuario'
	def __init__(self, nome, telefone, empresa):
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa

	def imprimir(self):
		print "Nome: %s\nTelefone: %s\nEmpresa: %s\n" % (self.nome,self.telefone,self.empresa)