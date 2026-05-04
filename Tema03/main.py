import numpy as np# type: ignore
import random
import functions as f

def main():

    n=int(input("n="))
    eps=1e-6

    A=[]
    b=[]

    op=input("1. tastatura\n2. fisier\n3. generare\n")
    if op=="1":
        A = np.array([input(f"A[{i}]= ").split() for i in range(n)], dtype=float)
        b=np.array(input("b= ").split(), dtype=float)


    elif op=="2":
        try:
         d=np.loadtxt("input.txt")
         A=d[:n]
         b=d[n]
        except FileNotFoundError:
            return
        

    elif op=="3":
        A=f.gen_matrix(n)
        b=np.random.randn(n) 

        f.afisare(A)
        f.afisare(b)
        print("\nAm generat A si b\n")


    A_init=np.array(A)
    b_init=np.array(b)


    if f.desc_LU(A,n):
        print("merge descompunerea\n")
        f.afisare(A)

    det=f.det(A,n)
    print(f"Determinantul lui A: {det:.6f}")

    y=f.sub_dir(A,b,n)
    x=f.sub_inv(A,y,n)

    if x:
        norma=f.verificare(A_init, b_init, x, n)
        print(f"Norma ||A_init*x -b_init||2 este: {norma:.32f}")

        A_lib=np.array(A_init)
        b_lib=np.array(b_init)

        x_lib=np.linalg.solve(A_lib, b_lib)
        A_inv_lib=np.linalg.inv(A_lib)

        dif_norme=f.norma2(np.array(x)-x_lib)
        print(f"Diferenta solutiilor calculate de mine si de librarie:{dif_norme:.32f}\n")

        dif_sol_si_ai_b=f.norma2(np.array(x) -np.dot(A_inv_lib, b_lib))
        print(f"Diferenta dintre solutie si inversa*b: {dif_sol_si_ai_b:.32f}")
    else:
        print("Sistemul nu are solutie unica (matricea singulara)")

if __name__ == "__main__":
    main()