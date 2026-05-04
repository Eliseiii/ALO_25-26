import numpy as np # type: ignore
import math

def gen_matrix(n):
  T=np.random.randn(n,n)
  A=T.T @ T
  return A


def det(A,n): #se calculeaza determinantul matricei A folosind elementele diagonalei principale a lui A dupa descompunere
  d=1.0
  for i in range(n):
    d*=A[i][i]

  return d
  
def desc_LU(A,n): 
  eps=1e-6

  for p in range(n):
    for i in range(p,n):
      s=0.0
      for k in range(p):
        s+=A[p][k]*A[k][i]
      A[p][i]-=s

    if abs(A[p][p])<eps:
      return False
    
    for j in range(p+1,n):
      s=0.0
      for k in range(p):
        s+=A[j][k]*A[k][p]
      A[j][p]=(A[j][p]-s)/A[p][p]

  return True

def sub_dir(A,b,n): #se rezolva sistemul Ly=b
  y=[0.0 for i in range(n)]

  for i in range(n):
        s=0.0
        for j in range(i):
          s+=A[i][j]*y[j]
        y[i]=b[i]-s

  return y

def sub_inv(A, y, n):# se rezolva sistemul Ux=y
  eps=1e-6
  x=[0.0 for i in range(n)]
  for i in reversed(range(n)):
        s=0.0
        for j in range(i+1,n):
          s+=A[i][j]*x[j]
        if abs(A[i][i])>eps:
          x[i]=(y[i]-s)/A[i][i]
        else:
           return None
        
  return x


def norma2(x):
  suma=0.0

  for i in range(len(x)):
    suma+=x[i]**2
      
  return math.sqrt(suma)


def verificare(A_init, b_init, x, n):
  dif=[]
  for i  in range(n):
    s=0.0
    for j in range(n):
      s+=A_init[i][j]*x[j]
    dif.append(s-b_init[i])
  
  return norma2(dif)

def afisare_matrice(A):
  for i in range(len(A)):
    for j in range(len(A[i])):
      print(f"{A[i][j]:.6f}", end=" ")
    print()

def afisare_vector(v):
  for i in range(len(v)):
    print(f"{v[i]:.6f}", end=" ")
  print()