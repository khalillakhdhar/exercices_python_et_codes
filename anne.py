annee=0
while annee<2000:
    annee=int(input("donner l'année"))
if((annee%4==0) and (annee%10!=0)):
    print("bisextille pure!")
elif((annee%4==0)):
    print("bisextille")
else:
    print("normale")