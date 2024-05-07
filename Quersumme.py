n = input("")

def quersumme(zahl):
    qs = 0
    while zahl > 0:
        qs = qs + zahl % 10
        zahl = zahl // 10
    return qs

print quersumme(n)