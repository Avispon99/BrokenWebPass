import http.client as ht
import urllib.parse as ub 

openConn=ht.HTTPConnection('127.0.0.1:80')
headers = {'Content-Type':'application/x-www-form-urlencoded','Accept':'text/plain'}
param = ub.urlencode({'user':'jhonatan','pass':'shaki11'})
openConn.request('POST','http://localhost/Test_brut/html_te/php/backdoc_2.php',param,headers)
resp=openConn.getresponse()
read_resp=resp.read().decode()
print(resp)
print(read_resp) 



