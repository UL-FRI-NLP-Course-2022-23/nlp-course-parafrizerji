import datetime
import numpy as np
import random
import requests
from requests.structures import CaseInsensitiveDict
import datetime
import numpy as np
from json import JSONDecodeError

# Clarin
url = "http://localhost:4000/api/translate"
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

steviloOdstavkovZaPrevod = 4

# prebere še neprevedene odstavke
neprevedeniOdstavki = np.load('neprevedeniSloOdstavki.npy',allow_pickle=True).tolist()

# preberem že prevedene stavke, če obstajajo
try:
    tabelaPrevedenihOdstavkov = np.load('prevedeniOdstavki.npy',allow_pickle=True).tolist()
except:
    print("Ni še datoteke s prevedenimi odstavki")
    tabelaPrevedenihOdstavkov = []


# Število neprevedenih in prevedenih odstavkov
print(len(neprevedeniOdstavki))
print(len(tabelaPrevedenihOdstavkov))

zacetek = datetime.datetime.now()
for i in range(steviloOdstavkovZaPrevod):
    stavekZaPrevod = neprevedeniOdstavki[i] 
    print(i)
    print(stavekZaPrevod)
    
    if len(stavekZaPrevod) > 2000:
        print("Stavek je predolg")
        continue
    
    # spremenljivke za prevedene odstavke
    stavekSloAnClarin = ""
    stavekSloAnSloClarinClarin = ""
    
    # vrstica s odstavki, ki se doda v tabelo prevedenih odstavkov
    vrstica = [""]*3
    vrstica[0] = stavekZaPrevod
    resp = ""
    # prevod iz slovenščine v angleščino preko clarina v angleščino in potem iz angleščine nazaj v slovenščino preko Clarin
    try:
        data = '{ "src_language":"sl","tgt_language":"en","text":"'+stavekZaPrevod+'"}'
        data = data.encode("utf-8")
        resp = requests.post(url, headers=headers, data=data)
        #print(resp.text)
        stavekSloAnClarin = eval(resp.text)['result']
        vrstica[1] = stavekSloAnClarin
        data = '{ "src_language":"en","tgt_language":"sl","text":"'+stavekSloAnClarin+'"}'
        data = data.encode("utf-8")
        resp = requests.post(url, headers=headers, data=data)
        stavekSloAnSloClarinClarin = eval(resp.text)['result']
        vrstica[2] = stavekSloAnSloClarinClarin
        print(resp.text)
    except:
        print("Nekaj šlo narobe prevajanje CLARIN")
        print(resp)      
    
    print()
    
    
    tabelaPrevedenihOdstavkov.append(vrstica)

for i in range(steviloOdstavkovZaPrevod):
    neprevedeniOdstavki.pop(0)

konec = datetime.datetime.now()
print(konec-zacetek)



# Število neprevedenih in prevedenih stavkov
print(len(neprevedeniOdstavki))
print(len(tabelaPrevedenihOdstavkov))



# Shranjevanje skupine neprevedenih odstavkov
np.save('neprevedeniSloOdstavki',np.asanyarray(neprevedeniOdstavki,dtype=object))

# Shranjevanje skupine prevedenih stavkov
np.save('prevedeniOdstavki',np.asanyarray(tabelaPrevedenihOdstavkov,dtype=object))