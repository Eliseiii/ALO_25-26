from exercitiul1 import precizie_masina as pm
import random

u,p=pm()
x=1.0
y=u*10
z=u*10

def verificare_adunare(x,y,z):
    op1=x+(y+z)
    op2=(x+y)+z

    print(f"op1 = {op1}, op2 = {op2}")
    if op1 != op2:
        print("Adunarea nu este asociativa")
    else:
        print("Adunarea este asociativa")

verificare_adunare(x,y,z)

def verificare_inmultire(x,y,z):
    op1=x*(y*z)
    op2=(x*y)*z

    if op1 != op2:
        return True

gasit = False
incercari = 0

while not gasit:
   
    x = random.uniform(0.1, 1.0)
    y = random.uniform(0.1, 1.0)
    z = random.uniform(0.1, 1.0)
    
    gasit = verificare_inmultire(x, y, z)
    incercari += 1
    if gasit:
        op1 = x*(y*z)
        op2 = (x*y)*z
        print(f"op1 = {op1}, op2 = {op2}")
        print(f"Numere gasite: x={x}, y={y}, z={z}")
        
print(f"Numar de incercari: {incercari}")