def convertobase(numero, base):
    if numero<=0 :
        return ""
    return convertobase(numero//base,base)+ valor(numero,base)
    pass
def valor(num, base):
    n = num%base
    return ( chr ( n-10+ord('A') ) , str(n) ) [ n <= 9]
    pass
