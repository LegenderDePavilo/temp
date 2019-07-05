import pycurl
import time
from bs4 import BeautifulSoup
def opening_url():
    host = "proxy.barc.gov.in"
    port = 8080
    user = "bits_trainee"
    pswd = "Barc%@123"
    proxy_auth_mode = pycurl.HTTPAUTH_DIGEST
    curl = pycurl.Curl()
    curl.setopt(pycurl.USERAGENT,'Foo')
    curl.setopt(pycurl.PROXY, host)
    curl.setopt(pycurl.PROXYPORT, port)
    curl.setopt(pycurl.PROXYAUTH, proxy_auth_mode)
    curl.setopt(pycurl.PROXYUSERPWD, "{}:{}".format(user, pswd))
    curl.setopt(curl.URL,'http://www.tezu.ernet.in/')
    # We use perform_rb to get bytes
    arr = curl.perform_rb()
    # On Python2 this will be str (as str == bytes)
    # On python3 this will be bytes
    print(type(arr))
    print(arr)
    # You can pass bytes to beautifulsoup
    soup1 = BeautifulSoup(arr, 'html.parser')
    # If you want to manually convert, you must pass "ignore" to ignore errors
    # This following statement has no effect on Python2. On Python3, it can
    # cause UnicodeDecodeError if "ignore" is not passed and website data
    # can't be decoded using utf-8
    arr = arr.decode('utf-8', 'ignore')
    # On Python2, type will be unicode
    # On Python3, type will be str (But str == unicode on python3)
    print(type(arr))
    # You can pass text to beautifulsoup
    soup2 = BeautifulSoup(arr, 'html.parser')
    curl.close()
    return
opening_url()
