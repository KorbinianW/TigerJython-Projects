n=1991

def anzahl(x):
    anz=0
    while x>0:
        x=x//10
        anz=anz+1
    return anz

def stellenwert(y,s):
    y=y//(10**(s-1))
    y=y%10
    return y

def pruefe():
    x=input("Bitte gebe eine natürliche Zahl größer Null ein")
    if x<=10:
        x=input("Bitte gebe eine natürliche Zahl größer 9 ein")
    return x
        
def gleichheit(n):
    n=pruefe()
    stellenanzahl=anzahl(n)
    vergleich=1
    if stellenanzahl>1:
        ende=stellenanzahl
        anfang=1
        while (ende>stellenanzahl/2) and (vergleich==1):
            if stellenwert(n,ende)==stellenwert(n,anfang):
                vergleich=1
                ende=ende-1
                anfang=anfang+1
            else:
                vergleich=0
        if vergleich==0:
            print "Die Zahl",n, "ist kein Palindrom"
        else:
            print "Die Zahl",n, "ist ein Palindrom"


gleichheit(n)           


                        


