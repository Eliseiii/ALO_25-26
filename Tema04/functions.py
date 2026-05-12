import numpy as np # type: ignore

def inmultire(A, x, n): #ex 1
    b=np.zeros(n)
    for i in range(n):
        s=0.0
        for j in range(n):
          s+=A[i][j]*x[j]
        b[i]=s 
    
    return b

def householder(A, b, n, eps):#ex 2
   
    Q=np.eye(n) # I ul

    for r in range(n-1):
      sigma=0.0

      for i in range(r,n):
         sigma+=A[i][r]**2
    
      if sigma<eps:
         break
      
      if A[r][r]<0:
        k=-np.sqrt(sigma)
      else:
         k=np.sqrt(sigma)

      beta=sigma-k*A[r][r]
      u=np.zeros(n)

      u[r]=A[r][r]-k
      for i in range(r+1,n):
         u[i]=A[i][r]

      for j in range(r,n):#tranformarea lui A
        s=0.0
        for i in range(r,n):
            s+=u[i]*A[i][j]
        s/=beta

        for i in range(r,n):
         A[i][j]-=s*u[i]
        
      s=0.0
      for i in range(r,n):
        s+=u[i]*b[i]
      s/=beta

      for i in range(r,n):
           b[i]-=s*u[i]

      for i in range(n):
         s=0.0
         for ii in range(r,n):
            s+=u[ii]*Q[i][ii]
         s/=beta
         for ii in range(r,n):
            Q[i][ii]-=s*u[ii]

    
    return Q, A

def subst_inv(R,y):
   n=len(y)
   x=np.zeros(n)

   for i in reversed(range(n)):
      s=0.0
      for j in range(i+1,n):
         s+=R[i][j]*x[j]
      x[i]=(y[i]-s)/R[i][i]
    
   return x

def norma2(x,n):
    s=0.0
    for i in range(n):
        s+=x[i]**2
    
    return np.sqrt(s)

def norma2_mat(x,n):
    s=0.0
    for i in range(n):
        for j in range(n):
            s+=x[i][j]**2
    
    return np.sqrt(s)


def inversa(Q, R, n):
   
    for i in range(n):
       if abs(R[i][i])<1e-6:
           raise ValueError("Matricea e singulara")
           return None
       
    A_inv=np.zeros((n,n))

    for i in range(n):
        b=np.zeros(n)

        for j in range(n):
            b[j]=Q[j][i]
        
        y=subst_inv(R, b)
        for j in range(n):
            A_inv[j][i]=y[j]
    
    return A_inv

        

    
    