import numpy as np # type: ignore
import functions as f
print("1. Fisier/ 2.Random")


o=int(input())
n=int(input("n="))
if o==1:
     try:
         d=np.loadtxt("input.txt")
         A=d[:n]
         s=d[n]
     except FileNotFoundError:
         print("Fisierul nu a fost gasit")
         exit()
    
else:
    A=np.random.randn(n,n)
    s=np.random.randn(n)

print("Matricea A:\n")
print(A)
print("Vectorul s:\n")
print(s)

A_init=np.array(A)
eps=1e-6

b=f.inmultire(A, s, n)
print("b=A*s:\n")
print(b)
b_init=np.copy(b)

Q_h,R_h=f.householder(A, b, n, eps)
print("Matricea Qt:\n")
print(Q_h)
print("Matricea R:\n")
print(R_h)

x_h=f.subst_inv(R_h, b)
print("\nSolutia x:\n")
print(x_h)
m=f.norma2(f.inmultire(A_init, x_h, n)-b_init,n)
print("\n||A_init*x-b_init||2: %.16e" % m)

x_qr = np.linalg.solve(A_init, b_init)
m=f.norma2(f.inmultire(A_init, x_qr, n)-b_init,n)
print("\n||A_init*xQR-b_init||2: %.16e" % m)

m=f.norma2(x_qr-s,n)/f.norma2(s,n)
print("\n||xQR-s||2/||s||2: %.16e" % m)


A_inv_h=f.inversa(Q_h, R_h, n)
A_inv_lib=np.linalg.inv(A_init)

print("\nInversa lui A calculata cu Householder:\n")
print(A_inv_h)

m=f.norma2_mat(A_inv_h-A_inv_lib,n)
print("\n||Ainv_h-A_inv_lib||2: %.16e" % m)
