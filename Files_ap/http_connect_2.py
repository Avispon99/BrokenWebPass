import http.client as ht
import urllib.parse as ub 

openConn=ht.HTTPSConnection('www.facebook.com:443')
headers = {'Content-Type':'application/x-www-form-urlencoded','Accept':'text/plain'}
param = ub.urlencode({'email':'100004485976029','pass':'agauluz119'})
openConn.request('POST','https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110',param,headers)
resp=openConn.getresponse()
read_resp=resp.read().decode()
print(resp)
print('xx:',read_resp) 



