def ggT(zahl1, zahl2):
    rest = 1
    while rest > 0:
        rest = zahl1 % zahl2
        zahl1 = zahl2
        merke = zahl2
        zahl2 = rest
        
        
    
    return merke

print ggT(544,391)