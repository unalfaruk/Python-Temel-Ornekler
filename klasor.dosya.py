import os
import time
klasor="C:/Program Files/Common Files/System"
for i in os.listdir(klasor):
    dosya=os.path.join(klasor,i)
    durum=os.stat(dosya)
    zaman=time.ctime(durum[8])
    if os.path.isdir(dosya):
        print("<Dosya> \t", zaman,"\t", i)
    elif os.path.isfile(dosya):
        print("<Klasör> \t", zaman,"\t", i)
