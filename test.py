import requests
import numpy as np
import pandas as pd
import os
import time
import argparse
import pycurl
from time import sleep
from bs4 import BeautifulSoup
INVALID_FILETYPE_MSG = "Error: Invalid file format. %s must be a .txt file."
INVALID_PATH_MSG = "Error: Invalid file path/name. Path %s does not exist."
def opening_url(curl,url):
    curl.setopt(curl.URL,url)
    try:
        arr=curl.perform_rb()
        arr=arr.decode('utf-8','ignore')
        soup=BeautifulSoup(arr,'html.parser')
        url=curl.getinfo(curl.EFFECTIVE_URL)
        return soup,url
    except pycurl.error:
	    return 0"""
def nopening_url(r,url):
    page=r.get(url)                                       #Retrieving the page 
    time.sleep(1)
    if(page.status_code==200):                            #Check for the correct response
        soup=BeautifulSoup(page.content,'html.parser')    #Making of the BeautifulSoup object
        return soup
    else:
        return 0
def opening_url(r,url):
    page=r.get(url,allow_redirects=True)                                #Retrieving the page 
    time.sleep(1)
    if(page.status_code==200):                            #Check for the correct response
        soup=BeautifulSoup(page.content,'html.parser')    #Making of the BeautifulSoup object
        no_of_redirects=len(page.history)
        if(no_of_redirects>1):
            redirects=[]
            for resp in page.history:
                redirects.append(resp.url)
            url=redirects[len(redirects)-1]
            return soup,url
        else:
            return soup
    else:
        return 0"""
def jsparser_links(r,url,df):
    soup=opening_url(r,url)
    if(soup==0):
        return 0 
    js=dict.fromkeys(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26',
                        '27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51',
                        '52','53','54','55','56','57','58','59','60','61','62','63'],0)
    soup_str=str(soup)                                        #Converting the BeautifulSoup object into string 
    data=read_js_list()                                                #Reading in the js keywords into a list
    js['1']=len(soup_str)                                     #Finding the total length of the document
    iframes=soup.find_all('iframe')                                              #Finding the number of iframes
    js['2']=len(iframes)
    a=0
    for x in data:                                                             #Counting the number of keywords used
        if(soup_str.count(str(x))):
            a=a+1
    js['3']=a
    js['4']=soup_str.count('escape') #escape  
    js['5']=soup_str.count('unescape')  #unescape
    link=soup.find_all('link')
    js['6']=len(link)      #link
    js['7']=soup_str.count('exec')  #exec
    js['8']=soup_str.count('search')  #search
    js['9']=soup_str.count('eval')  #eval
    js['10']=soup_str.count('decodeURI') #decode
    js['11']=soup_str.count('encodeURI') #encode
    js['12']=soup_str.count('concat')  #concatenation
    js['13']=soup_str.count('setTimeout') #setTimeout
    js['14']=soup_str.count('parseInt')  #parseInt
    js['15']=soup_str.count('fromCharCode')  #fromCharCode
    js['16']=soup_str.count('ActiveXObject') #activeXobject
    js['17']=soup_str.count('indexOf')  #indexof
    js['18']=soup_str.count('substring')  #substring
    js['19']=soup_str.count('replace')  #replace
    js['20']=soup_str.count('addEventListener') #addeventlistener
    js['21']=soup_str.count('attachEvent')  #attachevent
    js['22']=soup_str.count('createElement')  #createelement
    js['23']=soup_str.count('getElementById')  #getelementbyid
    js['24']=soup_str.count('document.write') #documentwrite
    js['25']=soup_str.count(' ')  #blankspaces
    lstrings=0
    s=soup_str.split(' ')
    for word in s:
        if(len(word)>200):
            lstrings=lstrings+1  #longstrings>200
    js['26']=lstrings
    chars=''.join(set(soup_str))
    js['27']=len(chars)  #noofuniquecharacters
    js['28']=soup_str.count('split')  #split
    js['29']=soup_str.count('onbeforeunload')  #onbeforeunload
    js['30']=soup_str.count('onload')  #onload
    js['31']=soup_str.count('onerror')  #onerror
    js['32']=soup_str.count('onunload')  #onunload
    js['33']=soup_str.count('onbeforeload')  #onbeforeload
    js['34']=soup_str.count('onmouseover')  #onmouseover
    js['35']=soup_str.count('dispatchEvent')  #dispatchevent
    js['36']=soup_str.count('fireEvent')  #fireevent
    js['37']=soup_str.count('setAttribute')  #setattribute
    js['38']=soup_str.count('window.location')  #windowlocation
    js['39']=soup_str.count('charAt')  #charat
    js['40']=soup_str.count('console.log')  #consolelog
    js['41']=soup_str.count('function')  #function
    js['42']=soup_str.count('Math.random')  #mathrandom
    js['43']=soup_str.count('charCodeAt')  #charcodeat
    js['44']=soup_str.count('toString')  #tostring
    js['45']=sum(c.isdigit() for c in soup_str)  #noofdigits
    bslash=["\'",'\"','\&','\\','\n','\r','\t','\b','\f']
    noofbslash=0
    for item in bslash:
        if item in soup_str:
            noofbslash=noofbslash+1  #noofbackslash
    js['46']=noofbslash
    js['47']=soup_str.count('|')
    js['48']=soup_str.count('%')
    js['49']=soup_str.count('.')
    js['50']=soup_str.count(',')
    js['51']=soup_str.count('#')
    js['52']=soup_str.count('+')
    js['53']=soup_str.count("'")
    js['54']=soup_str.count('(')
    js['55']=soup_str.count(')')
    js['56']=soup_str.count('{')
    js['57']=soup_str.count('}')
    js['58']=soup_str.count('[')
    js['59']=soup_str.count(']')
    df=df.append({'url':url,'lengthofdocument':js['1'],'iframes':js['2'],'noofkeywords':js['3'],'escape':js['4'],'unescape':js['5'],
                        'link':js['6'],'exec':js['7'],'search':js['8'],'eval':js['9'],'decode':js['10'],'encode':js['11'],'concat':js['12'],
                        'settimeout':js['13'],'parseint':js['14'],'fromcharcode':js['15'],'activexobject':js['16'],'indexof':js['17'],
                        'substring':js['18'],'replace':js['19'],'addeventlistener':js['20'],'attachevent':js['21'],'createelement':js['22'],
                        'getelememtbyid':js['23'],'documentwrite':js['24'],'blankspaces':js['26'],'longstrings':js['27'],'noofuniquechars':js['28'],
                        'split':js['28'],'onbeforeunload':js['29'],'onload':js['30'],'onerror':js['31'],'onunload':js['32'],'onbeforeload':js['33'],
                        'onmouseover':js['34'],'dispatchevent':js['35'],'fireevent':js['36'],'setattribute':js['37'],'windowlocation':js['38'],
                        'charat':js['39'],'consolelog':js['40'],'function':js['41'],'mathrandom':js['42'],'charcodeat':js['43'],'tostring':js['44'],
                        'noofdigits':js['45'],'noofbackslash':js['46'],'a':js['47'],'b':js['48'],'c':js['49'],'d':js['50'],'e':js['51'],'f':js['52'],
                        'g':js['53'],'h':js['54'],'i':js['55'],'j':js['56'],'k':js['57'],'l':js['58'],'m':js['59'],'category':0},ignore_index=True)
    return df
def html_parser(url,soup,df):
    soup_str=str(soup)                                                 #Converting the BeautifulSoup object into string 
    ht=dict.fromkeys(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],0)
    tags=[]                                                             #Finding the types and number of tags 
    for tag in soup.find_all(True):
        tags.append(tag.name)
    uniq,counts=np.unique(tags,return_counts=True)
    tnc=dict(zip(uniq,counts))
    ttags=0
    for i in tnc:
        ttags=ttags+tnc[i]                                              #Total number of tags used 
    ht['1']=url
    a=soup.find_all('iframe',src=True)
    b=soup.find_all('script',src=True)
    c=soup.find_all('embed',src=True)
    ht['2']=len(a)
    ht['3']=len(b)
    ht['4']=len(c)
    if('iframe' in tnc):
        ht['5']=tnc['iframe']
    if('applet' in tnc):
        ht['6']=tnc['applet']
    if('link' in tnc):
        ht['7']=tnc['link']
    if('meta' in tnc):
        ht['8']=tnc['meta']
    if('noframes' in tnc):
        ht['9']=tnc['noframes']
    if('frameset' in tnc):
        ht['10']=tnc['frameset']
    if('source' in tnc):
        ht['11']=tnc['source']
    if('form' in tnc):
        ht['12']=tnc['form']
    if('embed' in tnc):
        ht['13']=tnc['embed']
    d=soup.find_all('script')
    s=0
    for i in d:
        s=s+len(i)
    ht['14']=s
    ht['15']=soup_str.count('&#')
    ht['16']=soup_str.count('"hidden"')
    df=df.append({'url':ht['1'],'iframelinks':ht['2'],'jslinks':ht['3'],'embeddedlinks':ht['4'],'iframes':ht['5'],'applet':ht['6'],
                            'link':ht['7'],'meta':ht['8'],'noframes':ht['9'],'frameset':ht['10'],'source':ht['11'],'form':ht['12'],'embed':ht['13'],
                            'script':ht['14'],'encodings':ht['15'],'hidden':ht['16'],'category':0},ignore_index=True)
    return df
def read_js_list():
    global data
    with open('lp.txt','r') as fp:
        dataa=fp.read()
    dataa=str(dataa)
    dataa=dataa.replace('\n',' ')
    dataa=dataa.replace('\t',' ')
    data=(dataa.split(' '))
    return data
def scraper(r,url,dfs):
    sop=opening_url(r,url)                                            #Page retrieval request through the function calling
    if(sop==0):
        return 0
    if(type(sop)==tuple):
        soup=sop[0]
        url=sop[1]
    dfs[0]=html_parser(url,soup,dfs[0])                                     #Function called for the parsing of the necessary HTML elements
    iframe_src=[i["src"] for i in soup.find_all("iframe",src=True)]            #Finding the related iframe files
    js_src=[i["src"] for i in soup.find_all("script",src=True)]            #Finding the related javascript files           
    if(len(iframe_src)):
        for irr in iframe_src:                                                     #Looping through the iframes serially
            if(url.count(irr)<=1):
                ur=url+str(irr)
                dfs=[dfs[0],dfs[1]]
                scraper(r,ur,dfs)
    if(len(js_src)):
        for jrr in js_src:                                      #Looping through the javascript files serially
            if(url.count(jrr)<=1):
                ur=url+str(jrr)
                dfs[1]=jsparser_links(r,ur,dfs[1])                               #Function called for the related javascript files parsing
    dfs=[dfs[0],dfs[1]]
    return dfs
def writingfile(df_html,df_js):
    """with open('htmlFinal.csv','a') as fh:
        df_html.to_csv(fh,header=False)
    with open('jsFinal.csv','a') as fj:
        df_js.to_csv(fj,header=False)"""
    filename="htmlFinal"
    filename=filename+".csv"
    df_html.to_csv(filename,index=False,sep=',')
    filename="jsFinal"
    filename=filename+".csv"
    df_js.to_csv(filename,index=False,sep=',')
    print('The files has been written')
    return 0
def validate_file(file_name):
    if not valid_path(file_name):
        print(INVALID_PATH_MSG%(file_name))
        quit()
    elif not valid_filetype(file_name):
        print(INVALID_FILETYPE_MSG%(file_name))
        quit()
    return
def valid_filetype(file_name):
    return file_name.endswith('.txt')   # validate file type
def valid_path(path):
    return os.path.exists(path)        # validate file path
def check(file_name):
    validate_file(file_name)          # validate the file name/path
    return
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
    curl=pycurl.Curl()
    curl.setopt(pycurl.USERAGENT,'Foo')
    curl.setopt(curl.FOLLOWLOCATION, 1)
    if(args.proxy is not None and args.port is not None):
        host="103.205.14.65"
        port=8080
        curl.setopt(pycurl.PROXY, host)
        curl.setopt(pycurl.PROXYPORT, port)
    if(args.username is not None and args.port is not None):
        user="bits_trainee"
        pswd="Barc%@123"
        curl.setopt(pycurl.PROXYUSERPWD, "{}:{}".format(user, pswd))
        proxy_auth_mode=pycurl.HTTPAUTH_DIGEST
    slno=1
    df_html=pd.DataFrame(columns=['url','iframelinks','jslinks','embeddedlinks','iframes','applet','link','meta','noframes','frameset','source',
                                  'form','embed','script','encodings','hidden','category'])
    df_js=pd.DataFrame(columns=['url','lengthofdocument','iframes','noofkeywords','escape','unescape','link','exec','search','eval',
                    'decode','encode','concat','settimeout','parseint','fromcharcode','activexobject','indexof','substring','replace',
                    'addeventlistener','attachevent','createelement','getelememtbyid','documentwrite','blankspaces','longstrings',
                    'noofuniquechars','split','onbeforeunload','onload','onerror','onunload','onbeforeload','onmouseover','dispatchevent',
                    'fireevent','setattribute','windowlocation','charat','consolelog','function','mathrandom','charcodeat','tostring','noofdigits',
                    'noofbackslash','a','b','c','d','e','f','g','h','i','j','k','l','m','category'])
    dfs=[df_html,df_js]
    if(args.url is not None):          #Checking if the user provided with the url
        dfs=scraper(curl,args.url,dfs)
        print('************** ',slno,'th website scraped *************')
        if(dfs!=0):
            writingfile(dfs[0],dfs[1])
    elif(args.filename is not None):                                         #Checking if the user provided with the filename
        check(args.filename)                                                #Checking for the validityof file type and path
        urls=[line.rstrip('\n') for line in open(args.filename)]                         #Extracting the urls form the file
        for url in urls:
            """if(url.count('.')==1):
                url='http://www.'+url
                url=url+'/'
            elif(url.count('.')>=2):
                url='http://'+url
                url=url+'/'"""
            dfs=scraper(curl,url,dfs)
            print('********* ',slno,'th website scraped**********')
            slno=slno+1
        if(dfs!=0):
            writingfile(dfs[0],dfs[1])
    return 0        
if __name__=='__main__':
    main()
