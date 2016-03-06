Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Vektor():
	"""Bu bir vektördür."""

	
>>> A=Vektor()
>>> A.x=8
>>> A.y=6
>>> A.__doc__
'Bu bir vektördür.'
>>> class Vektor():
	"""Bu bir vektördür."""
	def __init__(self,x,y):
		print("Veri eklendi.")
		print(x,y)

		
>>> A=Vektor(8,6)
Veri eklendi.
8 6
>>> A.x
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    A.x
AttributeError: 'Vektor' object has no attribute 'x'
>>> class Vektor():
	"""Bu bir vektördür."""
	def __init__(self,x,y):
		print("Veri eklendi.")
		print(x,y)
		self.x=x
		self.y=y

		
>>> A=Vektor(6,8)
Veri eklendi.
6 8
>>> A.x
6
>>> A.y
8
>>> B=Vektor(3,4)
Veri eklendi.
3 4
>>> B.x
3
>>> B.y
4
>>> def vek_boy(V):
	return (V.x**2 + V.y**2)**(1/2)
vek_boy(A)
SyntaxError: invalid syntax
>>> def vekt_boy(V):
	return (V.x**2 + V.y**2)**(1/2)

>>> vek_boy(A)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    vek_boy(A)
NameError: name 'vek_boy' is not defined
>>> def vek_boy(V):
	return (V.x**2 + V.y**2)**(1/2)

>>> vek_boy(A)
10.0
>>> class Vektor():
	"""Bu bir vektördür."""
	def __init__(self,x,y):
		print("Veri eklendi.")
		print(x,y)
		self.x=x
		self.y=y
	def boyu(self):
		boy=(self.x**2+self.y**2)**(1/2)
		return boy

	
>>> A=Vektor(6,8)
Veri eklendi.
6 8
>>> A.boyu()
10.0
>>> A.x=10
>>> A.boyu()
12.806248474865697
>>> class Vektor():
	"""Bu bir vektördür."""
	def __init__(self,x,y):
		print("Veri eklendi.")
		print(x,y)
		self.x=x
		self.y=y
	def boyu(self):
		boy=(self.x**2+self.y**2)**(1/2)
		return boy
	def xaci(self):
		aci=math.degrees(math.tanh(self.x/self.y))
		return aci

	
>>> A.xaci()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    A.xaci()
AttributeError: 'Vektor' object has no attribute 'xaci'
>>> A=Vektor(8,6)
Veri eklendi.
8 6
>>> A.xaci()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    A.xaci()
  File "<pyshell#49>", line 12, in xaci
    aci=math.degrees(math.tanh(self.x/self.y))
NameError: name 'math' is not defined
>>> import math
>>> A.xaci()
49.85086113399414
>>> 
class Vektor():
	"""Bu bir vektördür."""
	def __init__(self,x,y):
		print("Veri eklendi.")
		print(x,y)
		self.x=x
		self.y=y
	def boyu(self):
		boy=(self.x**2+self.y**2)**(1/2)
		return boy
	def xaci(self):
		aci=math.degrees(math.tanh(self.x/self.y))
		return aci
	def tersi(self):
		a=self.x*(-1)
		b=self.y*(-1)
		self.x=a
		self.y=b
		return x,y

	
>>> A=Vektor(8,6)
Veri eklendi.
8 6
>>> A.tersi()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    A.tersi()
  File "<pyshell#62>", line 20, in tersi
    return x,y
NameError: name 'x' is not defined
>>> class Vektor():
	"""Bu bir vektördür."""
	def __init__(self,x,y):
		print("Veri eklendi.")
		print(x,y)
		self.x=x
		self.y=y
	def boyu(self):
		boy=(self.x**2+self.y**2)**(1/2)
		return boy
	def xaci(self):
		aci=math.degrees(math.tanh(self.x/self.y))
		return aci
	def tersi(self):
		a=self.x*(-1)
		b=self.y*(-1)
		self.x=a
		self.y=b
		return a,b

	
>>> A=Vektor(6,8)
Veri eklendi.
6 8
>>> A.tersi()
(-6, -8)
>>> class Vektor():
	"""Bu bir vektördür."""
	def __init__(self,x,y):
		print("Veri eklendi.")
		print(x,y)
		self.x=x
		self.y=y
	def boyu(self):
		boy=(self.x**2+self.y**2)**(1/2)
		return boy
	def xaci(self):
		aci=math.degrees(math.tanh(self.x/self.y))
		return aci
	def tersi(self):
		a=self.x*(-1)
		b=self.y*(-1)
		self.x=a
		self.y=b
		return a,b
	def __repr__(self):
		return("%di + %dj" % (self.x,self.y))

	
>>> A=Vektor(6,8)
Veri eklendi.
6 8
>>> print(A)
6i + 8j
>>> class Vektor():
	"""Bu bir vektördür."""
	def __init__(self,x,y):
		print("Veri eklendi.")
		print(x,y)
		self.x=x
		self.y=y
	def boyu(self):
		boy=(self.x**2+self.y**2)**(1/2)
		return boy
	def xaci(self):
		aci=math.degrees(math.tanh(self.x/self.y))
		return aci
	def tersi(self):
		a=self.x*(-1)
		b=self.y*(-1)
		self.x=a
		self.y=b
		return a,b
	def __repr__(self):
		return("%di + %dj" % (self.x,self.y))
	def __add__(self,oteki):
		return Vektor(self.x+oteki.x, self.y+oteki.y)

	
>>> A=Vektor(6,8)
Veri eklendi.
6 8
>>> B=Vektor(3,4)
Veri eklendi.
3 4
>>> C=A+B
Veri eklendi.
9 12
>>> print(C)
9i + 12j
>>> C.boyu()
15.0
>>> class Vektor():
	"""Bu bir vektördür."""
	def __init__(self,x,y):
		print("Veri eklendi.")
		print(x,y)
		self.x=x
		self.y=y
	def boyu(self):
		boy=(self.x**2+self.y**2)**(1/2)
		return boy
	def xaci(self):
		aci=math.degrees(math.tanh(self.x/self.y))
		return aci
	def tersi(self):
		a=self.x*(-1)
		b=self.y*(-1)
		self.x=a
		self.y=b
		return a,b
	def __repr__(self):
		return("%di + %dj" % (self.x,self.y))
	def __add__(self,oteki):
		return Vektor(self.x+oteki.x, self.y+oteki.y)
	def __sub__(self,oteki):
		return Vektor(self.x-oteki.x, self.y-oteki.y)

	
>>> A=Vektor(6,8)
Veri eklendi.
6 8
>>> B=Vektor(3,4)
Veri eklendi.
3 4
>>> C=A-B
Veri eklendi.
3 4
>>> class Vektor():
	"""Bu bir vektördür."""
	def __init__(self,x,y):
		print("Veri eklendi.")
		print(x,y)
		self.x=x
		self.y=y
	def boyu(self):
		boy=(self.x**2+self.y**2)**(1/2)
		return boy
	def xaci(self):
		aci=math.degrees(math.tanh(self.x/self.y))
		return aci
	def tersi(self):
		a=self.x*(-1)
		b=self.y*(-1)
		self.x=a
		self.y=b
		return a,b
	def __repr__(self):
		return("%di + %dj" % (self.x,self.y))
	def __add__(self,oteki):
		return Vektor(self.x+oteki.x, self.y+oteki.y)
	def __sub__(self,oteki):
		return Vektor(self.x-oteki.x, self.y-oteki.y)
	def __gt__(self,oteki):
		if self.boyu()>oteki.boyu(): return True

		
>>> A=Vektor(6,8)
Veri eklendi.
6 8
>>> B=Vektor(3,4)
Veri eklendi.
3 4
>>> A < B
>>> A > B
True
>>> class Vektor():
	"""Bu bir vektördür."""
	def __init__(self,x,y):
		print("Veri eklendi.")
		print(x,y)
		self.x=x
		self.y=y
	def boyu(self):
		boy=(self.x**2+self.y**2)**(1/2)
		return boy
	def xaci(self):
		aci=math.degrees(math.tanh(self.x/self.y))
		return aci
	def tersi(self):
		a=self.x*(-1)
		b=self.y*(-1)
		self.x=a
		self.y=b
		return a,b
	def __repr__(self):
		return("%di + %dj" % (self.x,self.y))
	def __add__(self,oteki):
		return Vektor(self.x+oteki.x, self.y+oteki.y)
	def __sub__(self,oteki):
		return Vektor(self.x-oteki.x, self.y-oteki.y)
	def __gt__(self,oteki):
		if self.boyu()>oteki.boyu(): return True
	def __mul__(self,oteki):
		bir=self.boyu()
		iki=oteki.boyu()
		cos=(self.x+oteki.x)/(bir+iki)
		return bir*iki*cos

	
>>> C=A*B
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    C=A*B
TypeError: unsupported operand type(s) for *: 'Vektor' and 'Vektor'
>>> class Vektor():
	"""Bu bir vektördür."""
	def __init__(self,x,y):
		print("Veri eklendi.")
		print(x,y)
		self.x=x
		self.y=y
	def boyu(self):
		boy=(self.x**2+self.y**2)**(1/2)
		return boy
	def xaci(self):
		aci=math.degrees(math.tanh(self.x/self.y))
		return aci
	def tersi(self):
		a=self.x*(-1)
		b=self.y*(-1)
		self.x=a
		self.y=b
		return a,b
	def __repr__(self):
		return("%di + %dj" % (self.x,self.y))
	def __add__(self,oteki):
		return Vektor(self.x+oteki.x, self.y+oteki.y)
	def __sub__(self,oteki):
		return Vektor(self.x-oteki.x, self.y-oteki.y)
	def __gt__(self,oteki):
		if self.boyu()>oteki.boyu(): return True
	def __mul__(self,oteki):
		bir=self.boyu()
		iki=oteki.boyu()
		cos=(self.x+oteki.x)/(bir+iki)
		return Vektor(bir*iki*cos)

	
>>> A=Vektor(6,8)
Veri eklendi.
6 8
>>> B=Vektor(3,4)
Veri eklendi.
3 4
>>> C=A*B
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    C=A*B
  File "<pyshell#110>", line 32, in __mul__
    return Vektor(bir*iki*cos)
TypeError: __init__() missing 1 required positional argument: 'y'
>>> class Vektor():
	"""Bu bir vektördür."""
	def __init__(self,x,y):
		print("Veri eklendi.")
		print(x,y)
		self.x=x
		self.y=y
	def boyu(self):
		boy=(self.x**2+self.y**2)**(1/2)
		return boy
	def xaci(self):
		aci=math.degrees(math.tanh(self.x/self.y))
		return aci
	def tersi(self):
		a=self.x*(-1)
		b=self.y*(-1)
		self.x=a
		self.y=b
		return a,b
	def __repr__(self):
		return("%di + %dj" % (self.x,self.y))
	def __add__(self,oteki):
		return Vektor(self.x+oteki.x, self.y+oteki.y)
	def __sub__(self,oteki):
		return Vektor(self.x-oteki.x, self.y-oteki.y)
	def __gt__(self,oteki):
		if self.boyu()>oteki.boyu(): return True
	def __mul__(self,oteki):
		bir=self.boyu()
		iki=oteki.boyu()
		cos=(self.x+oteki.x)/(bir+iki)
		return (bir*iki*cos)

	
>>> A=Vektor(6,8)
Veri eklendi.
6 8
>>> B=Vektor(3,4)
Veri eklendi.
3 4
>>> C=A*B
>>> C
30.0
>>> 
