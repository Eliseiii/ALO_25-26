def precizie_masina():
        u = 1
        i = 0
        while 1 + u != 1:
            u = u / 10
            i = i - 1
        return u, i

        
print(precizie_masina())