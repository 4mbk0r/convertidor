from base_n_to_decimal import converto10
from decimal_to_base_n import *
numero = input("inserte el numero \n").upper();
base_origen = int(input("inserte base de origen \n"))
base_destino = int(input("inserte base de destino \n"))
print ( converto10(numero, base_origen) )
print ( convertobase( converto10(numero, base_origen), base_destino) )
