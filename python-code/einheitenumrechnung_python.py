##Rechnet die bei "c" im Code eingegebene Konzentration in µg/ml in dasmolare verhältnis (=vol%/100) um


c=200 #concentration in µg/ml
R= 8.3145*1000
T=273.15
P=pow(10,5)
M_O_3=48*1000

gamma=c*R*T/(P*M_O_3)
print(gamma)