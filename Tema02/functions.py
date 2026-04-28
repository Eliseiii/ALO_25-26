def f(x):
    return (1/3)*x**3-2*x**2+2*x+3

def derivata_inf(x):
    h=1e-6
    return (3*f(x)-4*f(x-h)+f(x-2*h))/(2*h)


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

def delta_inf(x, y):

    h=1e-5
    numitor = derivata_inf(x) - derivata_inf(y)
    
    if abs(numitor) < h:
        if abs(derivata_inf(x)) < h/100:
            return 0.0
        else:
            return 1e-5
    
    return (x-y)*derivata_inf(x)/numitor