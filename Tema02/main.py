import random
import functions


def metoda_secantei():

    eps=1e-5
    kmax=1000
    x0=random.uniform(0.1, 10.0)
    x1=random.uniform(0.1, 10.0)
    x00=x0
    x11=x1

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
            print(f"Metoda secantei a convergat la solutia: {x1:.16f} in {k} iteratii.")
        else:
            print("Metoda secantei nu a convergat.")
    else:
        print(f"Algoritmul a eșuat (Divergență sau kmax atins).")



    # Metoda secantei cu derivata neeficienta
    
    k1=0
    dee=1.0
    while True:

        dee = functions.delta_inf(x11, x00)

        if dee == 0.0:
            break

        xx=x11 - dee

        if abs(dee)<eps:
            x11=xx
            break

        x00, x11 = x11, xx
        k1=k1+1

        if k1>=kmax or abs(x11)>10**8:
            break

    if abs(dee)<eps or dee==0.0:
        if functions.derivata_sec(x11) > 0:
            print(f"Metoda secantei cu derivata neeficienta a convergat la solutia: {x11:.16f} in {k1} iteratii.")
        else:
            print("Metoda secantei cu derivata neeficienta nu a convergat.")
    else:
        print(f"Algoritmul a eșuat (Divergență sau kmax atins).")

    print(f"Diferenta dintre solutiile obtinute: {abs(x11-x1):.16e}")



if __name__ == "__main__":
    metoda_secantei()