import math
from math import pi, tan
import random
import time

c1=1/3.0
c2=2/15.0
c3=17/315.0
c4=62/2835.0

print(f"c1={c1}, c2={c2}, c3={c3}, c4={c4}")

def polinom(x):
    x_2 = x**2
    return c1+x_2*(c2+x_2*(c3+c4*x_2))

def my_tan(x):
    return x + polinom(x)*(x**3)

x = float(input("Scrie x: "))
print(tan(x)," ", my_tan(x))

N=10000
dif_timp = []
nr=[random.uniform(-pi/2,pi/2) for i in range(N)]

if abs(x) >= pi/4:
        semn = 1 if x > 0 else -1
        predef = tan(x)
        aprox = semn* 1/my_tan(pi/2 - abs(x))
else:
        predef = tan(x)
        aprox = my_tan(x)
print(f"Diferenta pentru x={x} este: {abs(predef - aprox)}")

start_time = time.time()
for x in nr:
    if abs(x) >= pi/4:
        semn = 1 if x > 0 else -1
        predef = tan(x)
        aprox = semn* 1/my_tan(pi/2 - abs(x))
    else:
        predef = tan(x)
        aprox = my_tan(x)
    dif_timp.append(abs(predef - aprox))
end_time = time.time()

timp = end_time - start_time
print(f"Timpul de executie pentru metoda polinom este: {timp} secunde")

m=sum(dif_timp)/N
print(f"Media diferentelor pentru metoda polinom este: {m}")