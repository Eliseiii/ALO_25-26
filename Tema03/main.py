import numpy # type: ignore
import copy
import random
import functions

def main():

    n=int(input("n="))
    eps=1e-6

    A=[]
    b=[]

    op=input("1. tastatura\n2. fisier\n3. generare\n")
    if op=="1":
        for i in range(n):
            A.append(list(map(float, input("A["+str(i)+"]= ").split())))
        
        b=list(map(float, input("b= ").split()))


    elif op=="2":
        try:
         with open("input.txt", "r") as f:
            for i in range(n):
                A.append(list(map(float, f.readline().split())))
            b=list(map(float, f.readline().split()))
        except FileNotFoundError:
            return
        

    elif op=="3":
        A=functions.gen_matrix(n)
        b=numpy.random.randn(n) 

        functions.afisare_matrice(A)
        functions.afisare_vector(b)
        print("\nA si b au fost generate aleatoriu.\n")


    A_init=copy.deepcopy(A)
    b_init=copy.deepcopy(b)


    if functions.desc_LU(A,n):
        print("merge descompunerea\n")
        functions.afisare_matrice(A)

    determinant=functions.det(A,n)
    print(f"Determinantul lui A: {determinant:.16f}")

    y=functions.sub_dir(A,b,n)
    x=functions.sub_inv(A,y,n)

    if x:
        norma=functions.verificare(A_init, b_init, x, n)
        print(f"Norma ||A_init*x -b_init||2 este: {norma:.16f}")

        A_lib=numpy.array(A_init)
        b_lib=numpy.array(b_init)

        x_lib=numpy.linalg.solve(A_lib, b_lib)
        A_inv_lib=numpy.linalg.inv(A_lib)

        dif_norme=functions.norma2(numpy.array(x)-x_lib)
        print(f"Diferenta solutiilor calculate de mine si de librarie:{dif_norme:.16f}\n")

        dif_sol_si_ai_b=functions.norma2(numpy.array(x) -numpy.dot(A_inv_lib, b_lib))
        print(f"Diferenta dintre solutie si inversa*b: {dif_sol_si_ai_b:.16f}")
    else:
        print("Sistemul nu are solutie unica (matricea este singulara).")

if __name__ == "__main__":
    main()