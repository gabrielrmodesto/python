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

	@staticmethod
	def gerar_perfil(nome_arquivo):
		arquivo = open(nome_arquivo,'r')
		perfis = []
		for linha in arquivo:
			valores = linha.split(',')
			perfis.append(Perfil(*valores))
		arquivo.close()
		return perfis

class Perfil_Vip(Perfil):
	'Classe padrao para perfis de usuario'
	def __init__(self,nome,telefone,empresa,apelido=''):
		super(Perfil_Vip, self).__init__(nome,telefone,empresa)
		self.apelido = apelido

	def obter_creditos(self):
		return super(Perfil_Vip, self).obter_curtidas() * 10.0