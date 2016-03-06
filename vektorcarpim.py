v1x=input("Vektor 1 x: ")
v1y=input("Vektor 1 y: ")
v1z=input("Vektor 1 z: ")

v1x=int(v1x)
v1y=int(v1y)
v1z=int(v1z)

print("Vektör 1: ",v1x,",",v1y,",",v1z)

v2x=input("Vektor 2 x: ")
v2y=input("Vektor 2 y: ")
v2z=input("Vektor 2 z: ")

v2x=int(v2x)
v2y=int(v2y)
v2z=int(v2z)

print("Vektör 2: ",v2x,",",v2y,",",v2z)

vektor1=[]
vektor2=[]
vektor3=[]

vektor1.append([v1x,v1y,v1z])
vektor2.append([v2x,v2y,v2z])

vektor3.append([v1y*v2z-v1z*v2y,v1x*v2z-v1z*v2x,v1x*v2y-v1y*v2x])
print("Vek 1 x Vek 2: ", vektor3)
