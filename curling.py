import pycurl
import time
from bs4 import BeautifulSoup
def opening_url():
    host = "183.82.116.56"
    port = 8080
    #user = "bits_trainee"
    #pswd = "Barc%@123"
    proxy_auth_mode = pycurl.HTTPAUTH_DIGEST
    #proxy_auth_mode = pycurl.HTTPAUTH_BASIC
    try:
	curl = pycurl.Curl()
	curl.setopt(pycurl.USERAGENT,'Foo')
        #curl.setopt(pycurl.PROXYTYPE,pycurl.PROXYTYPE_SOCKS5)
	curl.setopt(pycurl.PROXY, host)
	curl.setopt(pycurl.PROXYPORT, port)
	curl.setopt(pycurl.PROXYAUTH, proxy_auth_mode)
	#curl.setopt(pycurl.PROXYUSERPWD, "{}:{}".format(user, pswd))
	curl.setopt(curl.URL, 'https://www.google.com')
	arr=(curl.perform_rs())
	time.sleep(10)
	soup=BeautifulSoup(arr,'html.parser')
	print('curlfinished**********************************')
    except pycurl.error:	
	    print('ERROR, couldn\'t connect')
    curl.close()
    return
