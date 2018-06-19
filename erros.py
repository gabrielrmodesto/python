# -*- coding: UTF-8 -*-
from models import *
arquivo = None
try:
	arquivo = open('perfis.csv','r')
	valores = arquivo.readline().split(',')
	Perfil(*valores)
# except (IOError, TypeError) as erro:
# 	print('Deu IOError: %s' % erro)
finally:
	if(arquivo is not None):
		print('Fechando arquivo')
		arquivo.close()