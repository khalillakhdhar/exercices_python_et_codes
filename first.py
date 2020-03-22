poid=float(input("donner votre poid"))
taille=float(input("donner votre taille"))
imc=poid/(taille*taille)
print("votre indice est de: "+ str(imc))
if(imc<20):
    print("maigre")
elif(imc<25):
    print("idéal")
else:
    print("surpoid")
