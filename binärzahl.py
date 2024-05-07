
def pruefe1():
    n=input("Gebe eine Zahl größer gleich Null und kleiner 256")
    if n<0 or n>255:
        n=input("Gebe eine Zahl größer gleich Null und kleiner 256")
    return n

def pruefe2():
    n=input("Gebe eine Zahl größer gleich Null und kleiner 256")
    while n<0 or n>255:
        n=input("Gebe eine Zahl größer gleich Null und kleiner 256")
    return n

def binaerzahl1(x):
    s = 0
    i = 0
    while x>0:
        r = x % 2
        s = s + r * 10 ** i
        i = i + 1
        x = x // 2
    return s

def binaerzahl2(x):
    s = 0
    for i in range (0,8):
        r = x % 2
        s = s + r * 10 ** i
        x = x // 2
    return s

def umwandeln():
    a=pruefe2()
    print "Die Zahl", a, "ergibt die Binärzahl", binaerzahl2(a)

umwandeln()