numero = input("inserte el numero \n");
base_origen =  int(input("inserte la base de numero \n"))
#base_final = int(input("inserte la base a convertir \n"))
new_num=0;
for x in range(len(numero)):
	
	if 'A' <= numero[x] <= 'Z' : 
		
		digito = ord(numero[x])-ord('A')+10;
	else:
		digito = int(numero[x])
	new_num=digito*pow(base_origen,x)+new_num;
	pass
print (new_num);