Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ogrenciler.append([395,"Faruk ÜNAL"])
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    ogrenciler.append([395,"Faruk ÜNAL"])
NameError: name 'ogrenciler' is not defined
>>> ogrenciler.append([395,"Faruk ÜNAL"])
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    ogrenciler.append([395,"Faruk ÜNAL"])
NameError: name 'ogrenciler' is not defined
>>> ogrenciler=[]
>>> ogrenciler.append([395,"Faruk ÜNAL"])
>>> ogrenciler.append([1428,"Furkan GEZER"])
>>> ogrenciler
[[395, 'Faruk ÜNAL'], [1428, 'Furkan GEZER']]
>>> ogrenciler[0]
[395, 'Faruk ÜNAL']
>>> ogr=ogrenciler[0]
>>> ogr
[395, 'Faruk ÜNAL']
>>> ogr[0]
395
>>> ogr[1]
'Faruk ÜNAL'
>>> for i in ogrenciler:
	print(i[0], "numaralı öğrencinin adı ",i[1])

	
395 numaralı öğrencinin adı  Faruk ÜNAL
1428 numaralı öğrencinin adı  Furkan GEZER
>>> 
