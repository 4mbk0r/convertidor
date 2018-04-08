
def converto10(numero,base_origen):
	new_num=0;
	p = len(numero);
	numero= numero.upper()
	for x in range(p):
		if 'A' <= numero[x] <= 'Z' :
			digito = ord(numero[x])-ord('A')+10;
		else:
			digito = int(numero[x])

		new_num=digito*pow(base_origen,p-x-1)+new_num;
		#print ( numero[x] )
		pass
	return new_num;
	pass
