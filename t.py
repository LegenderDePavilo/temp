import pandas as pd
df_html=pd.DataFrame(columns=['url','noofredirects','lengthofurl','lengthofhostname','lengthofprimarydomain','lengthofdocument','noofiframes',
                                  'noofiframelinks','noofjslinks','typesoftags','totaltags','hiddenobjects','concat','category'])
df_js=pd.DataFrame(columns=['url','lengthofdocument','noofiframes','noofkeywords','escape','unescape','link','exec','search','eval',
                    'decode','encode',
                    'concat','settimeout','parseint','fromcharcode','activexobject','indexof','substring','replace','addeventlistener',
                    'attachevent','createelement','getelememtbyid','documentwrite','blankspaces','longstrings','noofuniquechars','split',
                    'onbeforeunload','onload','onerror','onunload','onbeforeload','onmouseover','dispatchevent','fireevent','setattribute',
                    'windowlocation','charat','consolelog','function','mathrandom','charcodeat','tostring','noofdigits','noofbackslash',
                    'a','b','c','d','e','f','g','h','i','j','k','l','m','shareofdigits','shareofbackslash','shareofpipe','shareofpercentchars',
                    'category'])
dfs=[df_html,df_js]
print(type(df_html),type(df_js),type(dfs),type(dfs[0]),type(dfs[1]))
