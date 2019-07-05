import pycurl
import time
import argparse
from bs4 import BeautifulSoup
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--url',type=str,help='Specify the file containing urls to be scraped')
    parser.add_argument('--filename',type=str,help='Specify url to be scraped')
    parser.add_argument('--proxy',type=str,help='Specify proxy')
    parser.add_argument('--port',type=str,help='Port number')
    parser.add_argument('--username',type=str,help='Username')
    parser.add_argument('--password',type=str,help='Password of the proxy server')
    args=parser.parse_args()
    if(args.url is None and args.filename is None):
        print('URL or filename not specified')
        quit()
    if(args.url is not None and args.filename is not None):
        print('Cannot intake both url and filename at the same time')
        quit()
    curl = pycurl.Curl()
    curl.setopt(curl.FOLLOWLOCATION, 1)
    curl.setopt(pycurl.USERAGENT,'Foo')
    if(args.proxy is not None and args.port is not None):
        host=args.proxy
        port=args.port
        curl.setopt(pycurl.PROXY,host)
        curl.setopt(pycurl.PROXYPORT,port)
    if(args.username is not None and args.password is not None):
        user=args.username
        pswd=args.password
        proxy_auth_mode=pycurl.HTTPAUTH_DIGEST
        curl.setopt(pycurl.PROXYAUTH, proxy_auth_mode)
        curl.setopt(pycurl.PROXYUSERPWD, "{}:{}".format(user,pswd))
    if(args.filename is not None):                                         #Checking if the user provided with the filenam                                             #Checking for the validityof file type and path
        urls=[line.rstrip('\n') for line in open(args.filename)]                         #Extracting the urls form the file
        for url in urls:
            soup=openurl(curl,url)
            if(soup!=0):
                print(soup.prettify())
    return 0
def openurl(curl,url):
    curl.setopt(curl.URL,url)
    try:
        arr=curl.perform_rb()
    except:
        print('Page retrieve failure')
        return 0
    arr=arr.decode('utf-8', 'ignore')
    soup=BeautifulSoup(arr,'html.parser')
    return soup
if __name__=='__main__':
    main()
