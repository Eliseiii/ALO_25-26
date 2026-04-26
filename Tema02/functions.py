def f(x):
    return x**3+2*x**2-3*x+4

def derivata(x):
   h=1e-6
   return (-f(x+2*h)+8*f(x+h)-8*f(x-h)+f(x-2*h))/(12*h)

def derivata_sec(x):
    h=1e-6
    return (-f(x+2*h)+16*f(x+h)-30*f(x)+16*f(x-h)-f(x-2*h))/(12*h**2)

def delta(x, y):

    h=1e-5
    numitor = derivata(x) - derivata(y)
    
    if abs(numitor) < h:
        if abs(derivata(x)) < h/100:
            return 0.0
        else:
            return 1e-5
    
    return (x-y)*derivata(x)/numitor