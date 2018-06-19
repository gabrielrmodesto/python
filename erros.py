# -*- coding: UTF-8 -*-

try:
	open("nao_Existe.txt","r")
	print('O arquivo foi aberto')
	arquivo.close()
except IOError as erro:
	print('Deu IOError: %s' % erro)