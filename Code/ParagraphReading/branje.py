import os
import datetime
from requests.structures import CaseInsensitiveDict
import numpy as np

path = "cckresV1_0-text"
dir_list = os.listdir(path)



# Bere stavke in preskoči tiste, ki so krajši od 10 znakov.

vsiStavki = []

for i in sorted(dir_list):
    # preveri, če ima datoteko koncnico txt
    if not (i.endswith(".txt")):
        continue
        
    file = open(path+"/"+i, 'r', encoding="utf8")
    # loči po praznih vrsticah
    odstavki = file.read().split('\n\n')
    for k in odstavki:
        if len(k.strip(" -")) > 100:
            vsiStavki.append(k.replace("'","").replace('"','').replace("“","").replace("»","").replace("«","").replace('”','').replace("\n",""))

# shranjevanje stavkov v izvorni obliki na disk
np.save('neprevedeniSloOdstavki',np.asanyarray(vsiStavki,dtype=object))

# Število nabranih stavkov
print(len(vsiStavki))

