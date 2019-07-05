import requests
import numpy as np
import pandas as pd
import os
import time
import argparse
from time import sleep
from bs4 import BeautifulSoup
INVALID_FILETYPE_MSG = "Error: Invalid file format. %s must be a .txt file."
INVALID_PATH_MSG = "Error: Invalid file path/name. Path %s does not exist."
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
            ht['1']=ht['1']+no_of_redirects
            return soup,url
        else:
            return soup
    else:
        return 0
def jsparser_links(r,url):
    soup=nopening_url(r,url)
    if(soup==0):
        return 0 
    soup_str=str(soup)                                        #Converting the BeautifulSoup object into string 
    data=read_js_list()                                                #Reading in the js keywords into a list
    length_of_jsdoc=len(soup_str)                                     #Finding the total length of the document
    js['1']=js['1']+length_of_jsdoc
    iframes=soup.find_all('iframe')                                              #Finding the number of iframes
    no_of_jsiframes=len(iframes)
    js['2']=js['2']+no_of_jsiframes
    a=0
    for x in data:                                                             #Counting the number of keywords used
        a=a+soup_str.count(str(x)) 
    js['3']=js['3']+a
    escape=soup_str.count('escape') #escape  
    js['4']=js['4']+escape
    unescape=soup_str.count('unescape')  #unescape
    js['5']=js['5']+unescape
    link=soup.find_all('link')
    linko=len(link)      #link
    js['6']=js['6']+linko
    execo=soup_str.count('exec')  #exec
    js['7']=js['7']+execo
    search=soup_str.count('search')  #search
    js['8']=js['8']+search
    evalo=soup_str.count('eval')  #eval
    js['9']=js['9']+evalo
    decode=soup_str.count('decodeURI') #decode
    js['10']=js['10']+decode
    encode=soup_str.count('encodeURI') #encode
    js['11']=js['11']+encode
    concat=soup_str.count('concat')  #concatenation
    js['12']=js['12']+concat
    settimeout=soup_str.count('setTimeout') #setTimeout
    js['13']=js['13']+settimeout
    parseint=soup_str.count('parseInt')  #parseInt
    js['14']=js['14']+parseint
    fromcharcode=soup_str.count('fromCharCode')  #fromCharCode
    js['15']=js['15']+fromcharcode
    activexobject=soup_str.count('ActiveXObject') #activeXobject
    js['16']=js['16']+activexobject
    indexof=soup_str.count('indexOf')  #indexof
    js['17']=js['17']+indexof
    substring=soup_str.count('substring')  #substring
    js['18']=js['18']+substring
    replace=soup_str.count('replace')  #replace
    js['19']=js['19']+replace
    addeventlistener=soup_str.count('addEventListener') #addeventlistener
    js['20']=js['20']+addeventlistener
    attachevent=soup_str.count('attachEvent')  #attachevent
    js['21']=js['21']+attachevent
    createelement=soup_str.count('createElement')  #createelement
    js['22']=js['22']+createelement
    getelementbyid=soup_str.count('getElementById')  #getelementbyid
    js['23']=js['23']+getelementbyid
    documentwrite=soup_str.count('document.write') #documentwrite
    js['24']=js['24']+documentwrite
    blankspaces=soup_str.count(' ')  #blankspaces
    js['25']=js['25']+blankspaces
    lstrings=0
    s=soup_str.split(' ')
    for word in s:
        if(len(word)>200):
            lstrings=lstrings+1  #longstrings>200
    js['26']=js['26']+lstrings
    chars=''.join(set(soup_str))
    noofuchars=len(chars)  #noofuniquecharacters
    js['27']=js['27']+noofuchars
    split=soup_str.count('split')  #split
    js['28']=js['28']+split
    onbeforeunload=soup_str.count('onbeforeunload')  #onbeforeunload
    js['29']=js['29']+onbeforeunload
    onload=soup_str.count('onload')  #onload
    js['30']=js['30']+onload
    onerror=soup_str.count('onerror')  #onerror
    js['31']=js['31']+onerror
    onunload=soup_str.count('onunload')  #onunload
    js['32']=js['32']+onunload
    onbeforeload=soup_str.count('onbeforeload')  #onbeforeload
    js['33']=js['33']+onbeforeload
    onmouseover=soup_str.count('onmouseover')  #onmouseover
    js['34']=js['34']+onmouseover
    dispatchevent=soup_str.count('dispatchEvent')  #dispatchevent
    js['35']=js['35']+dispatchevent
    fireevent=soup_str.count('fireEvent')  #fireevent
    js['36']=js['36']+fireevent
    setattribute=soup_str.count('setAttribute')  #setattribute
    js['37']=js['37']+setattribute
    windowlocation=soup_str.count('window.location')  #windowlocation
    js['38']=js['38']+windowlocation
    charat=soup_str.count('charAt')  #charat
    js['39']=js['39']+charat
    consolelog=soup_str.count('console.log')  #consolelog
    js['40']=js['40']+consolelog
    function=soup_str.count('function')  #function
    js['41']=js['41']+function
    mathrandom=soup_str.count('Math.random')  #mathrandom
    js['42']=js['42']+mathrandom
    charcodeat=soup_str.count('charCodeAt')  #charcodeat
    js['43']=js['43']+charcodeat
    tostring=soup_str.count('toString')  #tostring
    js['44']=js['44']+tostring
    noofdigits=sum(c.isdigit() for c in soup_str)  #noofdigits
    js['45']=js['45']+noofdigits
    bslash=["\'",'\"','\&','\\','\n','\r','\t','\b','\f']
    noofbslash=0
    for item in bslash:
        if item in soup_str:
            noofbslash=noofbslash+1  #noofbackslash
    js['46']=js['46']+noofbslash
    pipe=soup_str.count('|')
    js['47']=js['47']+pipe
    pchars=soup_str.count('%')
    js['48']=js['48']+pchars
    cchars=soup_str.count('.')
    js['49']=js['49']+cchars
    dchars=soup_str.count(',')
    js['50']=js['50']+dchars
    hchars=soup_str.count('#')
    js['51']=js['51']+hchars
    plchars=soup_str.count('+')
    js['52']=js['52']+plchars
    ichars=soup_str.count("'")
    js['53']=js['53']+ichars
    fsb=soup_str.count('(')
    js['54']=js['54']+fsb
    feb=soup_str.count(')')
    js['55']=js['55']+feb
    ssb=soup_str.count('{')
    js['56']=js['56']+ssb
    seb=soup_str.count('}')
    js['57']=js['57']+seb
    tsb=soup_str.count('[')
    js['58']=js['58']+tsb
    teb=soup_str.count(']')
    js['59']=js['59']+teb
    sofdigits=(100*noofdigits)/length_of_jsdoc  #shareofdigits
    js['60']=js['60']+sofdigits
    sofbslash=(100*noofbslash)/length_of_jsdoc  #shareofbackslash
    js['61']=js['61']+sofbslash
    sofpipe=(100*pipe)/length_of_jsdoc  #shareofpipe
    js['62']=js['62']+sofpipe
    sofpchars=(100*pchars)/length_of_jsdoc  #shareofpercentagechars
    js['63']=js['63']+sofpchars
    return 0
def html_parser(url,soup):
    soup_str=str(soup)                                                 #Converting the BeautifulSoup object into string 
    length_of_doc=len(soup_str)                                        #Finding the total length of the document
    iframes=soup.find_all('iframe')                                    #Finding the number of iframes
    no_of_iframes=len(iframes)
    iframe_src=[url+i["src"] for i in soup.find_all("iframe",src=True)] #Number of iframes links
    no_of_iframelinks=len(iframe_src)
    js_src=[url+i["src"] for i in soup.find_all("script",src=True)]     #Number of Javascript links
    no_of_jslinks=len(js_src)
    tags=[]                                                             #Finding the types and number of tags 
    for tag in soup.find_all(True):
        tags.append(tag.name)
    uniq,counts=np.unique(tags,return_counts=True)
    tag_n_count=dict(zip(uniq,counts))
    tag_types=len(uniq)       #types of tags
    j=0                                                            
    ttags=0
    for i in tag_n_count:
        ttags=ttags+tag_n_count[i]          #Total number of tags used 
    hidden_objs=soup_str.count('"hidden"')                              #Finding the number of hidden objects occurences
    concat=soup_str.count('concat')                                     #Finding the number of string concatenation functions
    ht['5']=ht['5']+length_of_doc
    ht['6']=ht['6']+no_of_iframes
    ht['7']=ht['7']+no_of_iframelinks
    ht['8']=ht['8']+no_of_jslinks
    ht['9']=ht['9']+tag_types
    ht['10']=ht['10']+ttags
    ht['11']=ht['11']+hidden_objs
    ht['12']=ht['12']+concat
    data=read_js_list()                     #Reading in the js keywords into a list
    a=0
    for x in data:                          #Counting the number of javascript keywords
        a=a+soup_str.count(str(x))
    escape=soup_str.count('escape')
    unescape=soup_str.count('unescape')  
    link=soup.find_all('link')
    linko=len(link)
    execo=soup_str.count('exec')
    search=soup_str.count('search')
    evalo=soup_str.count('eval')
    decode=soup_str.count('decodeURI')
    encode=soup_str.count('encodeURI')
    concat=soup_str.count('concat')
    return 0
def url_parser(url):
    length_of_url=len(url)
    for i in range(0,(len(url)-2)):
        if((url[i]==':')&(url[i+1]=='/')&(url[i+2]=='/')):
            for j in range(i+3,len(url)):
                if(url[j]=='/'):
                    length_of_hostname=j-(i+3)
                    j=len(url)
        if(url[i]=='.'):
            for j in range(i+1,len(url)):
                if(url[j]=='/'):
                    length_of_pdomain=j-(i+1)
                    j=len(url)
            break
    ht['2']=ht['2']+length_of_url
    ht['3']=ht['3']+length_of_hostname
    ht['4']=ht['4']+length_of_pdomain
    return 0
def read_js_list():
    global data
    with open('lp.txt','r') as fp:
        dataa=fp.read()
    dataa=str(dataa)
    dataa=dataa.replace('\n',' ')
    dataa=dataa.replace('\t',' ')
    data=(dataa.split(' '))
    return data
def scraper(r,url):
    sop=opening_url(r,url)                                            #Page retrieval request through the function calling
    if(sop==0):
        return 0
    url_parser(url)
    if(type(sop)==tuple):
        soup=sop[0]
        url=sop[1]
    else:
        soup=sop
    html_parser(url,soup)                            #Function called for the parsing of the necessary HTML elements
    iframe_src=[i["src"] for i in soup.find_all("iframe",src=True)]            #Finding the related iframe files
    js_src=[i["src"] for i in soup.find_all("script",src=True)]            #Finding the related javascript files           
    if(len(iframe_src)):
        for irr in iframe_src:                                                     #Looping through the iframes serially
            if(url.count(irr)<=1):
                ur=url+str(irr)
                scraper(r,ur)
    if(len(js_src)):
        for jrr in js_src:                                      #Looping through the javascript files serially
            if(url.count(jrr)<=1):
                ur=url+str(jrr)
                jsparser_links(r,ur)                               #Function called for the related javascript files parsing
    return 0
def writingfile(df_html,df_js):
    with open('htmlFinal.csv','a') as fh:
        df_html.to_csv(fh,header=False)
    with open('jsFinal.csv','a') as fj:
        df_js.to_csv(fj,header=False)
    #filename="htmlFinal"
    #filename=filename+".csv"
    #df_html.to_csv(filename,index=False,sep=',')
    #filename="jsFinal"
    #filename=filename+".csv"
    #df_js.to_csv(filename,index=False,sep=',')
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
    r=requests.session()
    r.max_redirects=15
    slno=1
    global ht
    global js
    df_html=pd.DataFrame(columns=['url','noofredirects','lengthofurl','lengthofhostname','lengthofprimarydomain','lengthofdocument','noofiframes',
                                  'noofiframelinks','noofjslinks','typesoftags','totaltags','hiddenobjects','concat','category'])
    df_js=pd.DataFrame(columns=['lengthofdocument','noofiframes','noofkeywords','escape','unescape','link','exec','search','eval','decode','encode',
                    'concat','settimeout','parseint','fromcharcode','activexobject','indexof','substring','replace','addeventlistener',
                    'attachevent','createelement','getelememtbyid','documentwrite','blankspaces','longstrings','noofuniquechars','split',
                    'onbeforeunload','onload','onerror','onunload','onbeforeload','onmouseover','dispatchevent','fireevent','setattribute',
                    'windowlocation','charat','consolelog','function','mathrandom','charcodeat','tostring','noofdigits','noofbackslash',
                    'a','b','c','d','e','f','g','h','i','j','k','l','m','shareofdigits','shareofbackslash','shareofpipe','shareofpercentchars',
                    'category'])
    if(args.url is not None):          #Checking if the user provided with the url
        scraper(r,args.url)
        ht=dict.fromkeys(['1','2','3','4','5','6','7','8','9','10','11','12'],0)
        js=dict.fromkeys(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26',
                        '27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51',
                        '52','53','54','55','56','57','58','59','60','61','62','63'],0)
        df_html=df_html.append({'url':args.url,'noofredirects':ht['1'],'lengthofurl':ht['2'],'lengthofhostname':ht['3'],
                                    'lengthofprimarydomain':ht['4'],'lengthofdocument':ht['5'],'noofiframes':ht['6'],'noofiframelinks':ht['7'],
                                    'noofjslinks':ht['8'],'typesoftags':ht['9'],'totaltags':ht['10'],'hiddenobjects':ht['11'],'concat':ht['12'],
                                    'category':0},ignore_index=True)
        df_js=df_js.append({'lengthofdocument':js['1'],'noofiframes':js['2'],'noofkeywords':js['3'],'escape':js['4'],'unescape':js['5'],
                                'link':js['6'],'exec':js['7'],'search':js['8'],'eval':js['9'],'decode':js['10'],'encode':js['11'],'concat':js['12'],
                                'settimeout':js['13'],'parseint':js['14'],'fromcharcode':js['15'],'activexobject':js['16'],'indexof':js['17'],
                                'substring':js['18'],'replace':js['19'],'addeventlistener':js['20'],'attachevent':js['21'],'createelement':js['22'],
                                'getelememtbyid':js['23'],'documentwrite':js['24'],'blankspaces':js['25'],'longstrings':js['26'],
                                'noofuniquechars':js['27'],'split':js['28'],'onbeforeunload':js['29'],'onload':js['30'],'onerror':js['31'],
                                'onunload':js['32'],'onbeforeload':js['33'],'onmouseover':js['34'],'dispatchevent':js['35'],'fireevent':js['36'],
                                'setattribute':js['37'],'windowlocation':js['38'],'charat':js['39'],'consolelog':js['40'],'function':js['41'],
                                'mathrandom':js['42'],'charcodeat':js['43'],'tostring':js['44'],'noofdigits':js['45'],'noofbackslash':js['46'],
                                'a':js['47'],'b':js['48'],'c':js['49'],'d':js['50'],'e':js['51'],'f':js['52'],'g':js['53'],'h':js['54'],'i':js['55'],
                                'j':js['56'],'k':js['57'],'l':js['58'],'m':js['59'],'shareofdigits':js['60'],'shareofbackslash':js['61'],
                                'shareofpipe':js['62'],'shareofpercentchars':js['63'],'category':0},ignore_index=True)
        print('************** ',slno,'th website scraped *************')
        writingfile(df_html,df_js)
    elif(args.filename is not None):                                         #Checking if the user provided with the filename
        check(args.filename)                                                #Checking for the validityof file type and path
        urls=[line.rstrip('\n') for line in open(args.filename)]                         #Extracting the urls form the file
        for url in urls:
            if(url.count('.')==1):
                url='http://www.'+url
                url=url+'/'
            elif(url.count('.')>=2):
                url='http://'+url
                url=url+'/'
            ht=dict.fromkeys(['1','2','3','4','5','6','7','8','9','10','11','12'],0)
            js=dict.fromkeys(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25',
                            '26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49',
                            '50','51','52','53','54','55','56','57','58','59','60','61','62','63'],0)
            scraper(r,url)
            df_html=df_html.append({'url':url,'noofredirects':ht['1'],'lengthofurl':ht['2'],'lengthofhostname':ht['3'],
                                    'lengthofprimarydomain':ht['4'],'lengthofdocument':ht['5'],'noofiframes':ht['6'],'noofiframelinks':ht['7'],
                                    'noofjslinks':ht['8'],'typesoftags':ht['9'],'totaltags':ht['10'],'hiddenobjects':ht['11'],'concat':ht['12'],
                                    'category':0},ignore_index=True)
            df_js=df_js.append({'lengthofdocument':js['1'],'noofiframes':js['2'],'noofkeywords':js['3'],'escape':js['4'],'unescape':js['5'],
                                'link':js['6'],'exec':js['7'],'search':js['8'],'eval':js['9'],'decode':js['10'],'encode':js['11'],'concat':js['12'],
                                'settimeout':js['13'],'parseint':js['14'],'fromcharcode':js['15'],'activexobject':js['16'],'indexof':js['17'],
                                'substring':js['18'],'replace':js['19'],'addeventlistener':js['20'],'attachevent':js['21'],'createelement':js['22'],
                                'getelememtbyid':js['23'],'documentwrite':js['24'],'blankspaces':js['25'],'longstrings':js['26'],
                                'noofuniquechars':js['27'],'split':js['28'],'onbeforeunload':js['29'],'onload':js['30'],'onerror':js['31'], 
                                'onunload':js['32'],'onbeforeload':js['33'],'onmouseover':js['34'],'dispatchevent':js['35'],'fireevent':js['36'],
                                'setattribute':js['37'],'windowlocation':js['38'],'charat':js['39'],'consolelog':js['40'],'function':js['41'],
                                'mathrandom':js['42'],'charcodeat':js['43'],'tostring':js['44'],'noofdigits':js['45'],'noofbackslash':js['46'],
                                'a':js['47'],'b':js['48'],'c':js['49'],'d':js['50'],'e':js['51'],'f':js['52'],'g':js['53'],'h':js['54'],'i':js['55'],
                                'j':js['56'],'k':js['57'],'l':js['58'],'m':js['59'],'shareofdigits':js['60'],'shareofbackslash':js['61'],
                                'shareofpipe':js['62'],'shareofpercentchars':js['63'],'category':0},ignore_index=True)
            print('********* ',slno,'th website scraped**********')
            slno=slno+1
        writingfile(df_html,df_js)
    return 0        
if __name__=='__main__':
    main()
