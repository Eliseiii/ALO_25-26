import random
import functions


def metoda_secantei():

    eps=1e-5
    kmax=1000
    x0=random.uniform(0.1, 10.0)
    x1=random.uniform(0.1, 10.0)

    k=0
    de=1.0
    converge=True
    print(f"Valoarea initiala x0: {x0}")
    print(f"Valoarea initiala x1: {x1}")

    while True:

        de = functions.delta(x1, x0)

        if de == 0.0:
             break

        x=x1 - de

        if abs(de)<eps:
            x1=x
            break

        x0, x1 = x1, x
        k=k+1

        if k>=kmax or abs(x1)>10**8:
            break

    if abs(de)<eps or de==0.0:
        if functions.derivata_sec(x1) > 0:
            print(f"Metoda secantei a convergat la solutia: {x1:.6f} in {k} iteratii.")
        else:
            print("Metoda secantei nu a convergat.")
    else:
        print(f"Algoritmul a eșuat (Divergență sau kmax atins).")

if __name__ == "__main__":
    metoda_secantei()