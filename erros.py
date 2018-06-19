# -*- coding: UTF-8 -*-
from models import *
try:
	arquivo = open('perfis.csv','r')
	valores = arquivo.readline().split(',')
	Perfil(*valores)
	arquivo.close()
except (IOError, TypeError) as erro:
	print('Deu IOError: %s' % erro)
# except TypeError as erro:
# 	print('Deu TypeError: %s' % erro)