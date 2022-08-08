##Zusammenstellung der Messergebnisse und deren grafische Darstellung
##Code enthält bereits die Messwerte
##im code kann zwischen Setup A und B gewählt werden



import numpy as np
import matplotlib.pyplot as plt
#plt.style.use(['robert'])


#choose setup A or B
setup ='A'




#Messwerte zur Prüfung

#23.11.21
#mess_1 13:30
generator_mess_1  =[0,0,5,10,15,20,25,30,40,50,60,70,80,0,0]
witec_mess_1  =[-0.00025,-0.00044,0.10665,0.32340,0.66624,0.77748,1.04104,1.35457,1.91390,2.42011,2.92646,3.42816,3.88400,0.00255,-0.00083]
grossaufbau_mess_1  =[-0.00001,0.00055,0.05698,0.16284,0.31839,0.36804,0.48128,0.60825,0.82395,1.00527,1.17220,1.32385,1.45060,0.00756,0.00503]

#mess_2 14:00
generator_mess_2=[0,0,80,70,60,50,40,30,25,20,15,10,5,0]
witec_mess_2=[-0.00049,-0.00005,3.95870,3.43386,2.90050,2.39836,1.89560,1.34601,1.03831,0.76713,0.71068,0.35626,0.13472,0.00235]
grossaufbau_mess_2=[0.00086,0.00118,1.46176,1.31752,1.15580,0.98664,0.80957,0.59981,0.47409,0.36041,0.33520,0.17735,0.06812,0.00382]

#mess_3 14:25
generator_mess_3=[0,30,40,50,60,70,80,0,5,10,15,20,25]
witec_mess_3=[-0.00040,1.37364,1.92818,2.41958,2.91372,3.38827,3.82507,0.00557,0.14063,0.37109,0.71915,0.77809,1.04809]
grossaufbau_mess_3=[-0.00013,0.60951,0.82205,0.99771,1.16014,1.30440,1.42632,0.00506,0.07403,0.18328,0.33989,0.36548,0.47270]

#24.11.21
#mess_4 15:10
generator_mess_4=[0,5,10,15,20,25,30,40,50,60,70,80,0,0]
witec_mess_4=[-0.00237,0.12487,0.35251,0.68756,0.76673,1.02952,1.34310,1.89200,2.38815,2.88203,3.37550,3.80396,0.00161,-0.00116]
grossaufbau_mess_4=[0.00075,0.066152,0.17948,0.33267,0.36819,0.48122,0.61084,0.82401,1.00331,1.16843,1.32021,1.44156,0.01001,0.00899]

#mess_5 15:25
generator_mess_5=[0,80,70,60,50,40,30,25,20,15,10,5,0,0]
witec_mess_5=[-0.00220,3.82109,3.32145,2.81621,2.32120,1.85110,1.31732,1.00498,0.72404,0.75284,0.37822,0.14038,-0.00065,-0.00159]
grossaufbau_mess_5=[-0.00012,1.43741,1.29503,1.13801,0.97143,0.80034,0.59275,0.46420,0.34468,0.35725,0.18864,0.07386,0.00115,0.00073]


generator=generator_mess_1+generator_mess_2+generator_mess_3+generator_mess_4+generator_mess_5
witec_A=witec_mess_1+witec_mess_2+witec_mess_3+witec_mess_4+witec_mess_5
gross=grossaufbau_mess_1+grossaufbau_mess_2+grossaufbau_mess_3+grossaufbau_mess_4+grossaufbau_mess_5




#KLEIN
#klein_mess_1  2.12.21 17:45
gen_mess_1=[0,5,10,15,20,0,25,30,40,0,50,60,70,80]
klein_mess_1=[0.0002289,0.07417,0.20663,0.40329,0.37821,0.00380,0.51885,0.67229,0.92086,0.00502,1.12738,1.32649,1.50822,1.66330]
witec_klein_mess_1=[-0.00178,0.13435,0.38537,0.78604,0.73482,0.00200,1.03266,1.36807,1.94280,0.00170,2.44798,2.96376,3.47154,3.93783]

#klein_mess_2 2.12.21 18:00
gen_mess_2=[0,80,70,60,0,50,40,30,25,0,20,15,10,5,0]
klein_mess_2=[0.00009445,1.67504,1.49988,1.30421,0.00395,1.10683,0.90366,0.661307,0.51213,0.00520,0.37613,0.41416,0.21525,0.08830,0.00477]
witec_klein_mess_2=[-0.00139,3.97058,3.44518,2.90723,0.00326,2.40042,1.90540,1.34756,1.01877,0.00328,0.72796,0.80937,0.40207,0.15344,0.00084]

#klein_mess_3 2.12.21 18:10
gen_mess_3=[0,40,50,0,70,0,80,5,10,15,0,20,25,30,0]
klein_mess_3=[0.00013,0.90631,1.11028,1.30285,1.48096,0.00530,1.63357,0.08905,0.21700,0.41364,0.00463,0.37558,0.50900,0.65773,0.00409]
witec_klein_mess_3=[-0.00156,1.91924,2.41848,2.91582,3.40738,0.00812,3.86099,0.16171,0.40858,0.81228,0.00437,0.73123,1.01572,1.34683,0.00265]

#klein_lost_4 3.12.21 17:10
gen_mess_4=[0,5,10,15,0,20,25,30,40,0,50,60,70,80,0]
klein_mess_4=[0.00907,0.07091,0.19561,0.37223,0.00743,0.40855,0.53919,0.68454,0.92988,0.01302,1.13778,1.33495,1.51684,1.67149,0.01641]
witec_klein_mess_4=[-0.00156,0.11841,0.35253,0.70174,-0.00081,0.77367,1.04634,1.36334,1.92294,0.00307,2.42440,2.92886,3.43005,3.88754,0.00155]

#klein_mess_5 3.12.21 17:25
gen_mess_5=[0,50,40,30,25,0,20,15,10,5,0,80,70,60]
klein_mess_5=[0.00018,1.11758,0.90910,0.66673,0.52096,0.00425,0.38727,0.38379,0.19926,0.07583,0.00445,1.66221,1.48052,1.29015]
witec_klein_mess_5=[-0.00176,2.42928,1.92318,1.36327,1.04173,0.00332,0.75268,0.74611,0.36993,0.12906,-0.00016,3.94258,3.40487,2.88123]


gen=gen_mess_1+gen_mess_2+gen_mess_3+gen_mess_4+gen_mess_5
klein=klein_mess_1+klein_mess_2+klein_mess_3+klein_mess_4+klein_mess_5
witec_B=witec_klein_mess_1+witec_klein_mess_2+witec_klein_mess_3+witec_klein_mess_4+witec_klein_mess_5


if (setup == 'A'):
    ozomat=generator
    device=gross
    witec=witec_A
    # von=21
    # bis=46
    von=25
    bis=55
    zerobis=10
    ohnenull=16
    #regression parameters
    m=2.4311
    c=-0.10122

    a3=0.51444
    a2=1.9140
    a1=0.00076056
elif(setup=='B'):
    ozomat=gen
    device=klein
    witec=witec_B
    von=28
    bis=58
    zerobis=10
    ohnenull=18
    #regression parameters
    m=2.1760
    c=-0.095042

    a3=0.32845
    a2=1.8003
    a1=-0.0088889
else:
    print('error choosing a setup!!!')
    exit()


#create array and sort
a=np.array([ozomat,witec,device])
b=a[:,a[1,:].argsort()]
generator=b[0]
witec=np.array(b[1])
device=np.array(b[2])


print(witec[von:bis])


#regressions
linear=m*device+c
quadrat=a3*device**2+a2*device+a1


fig3, ax3 = plt.subplots()
x=np.linspace(0,len(device),len(device))
ax3.scatter( x,witec, 3, label='reference analyser')
ax3.scatter(x, linear,3,marker="v", label='device with linear regression')
ax3.scatter(x,quadrat,3,marker="x", label='device with quadratic regression')
plt.title("Measurements Setup "+str(setup))
plt.xlabel("ordered measurements [ ]")
plt.ylabel("measured concentration [vol\%]")
plt.legend()

plt.show()


fig3, ax3 = plt.subplots()
x=np.linspace(0,len(device),len(device))
ax3.scatter(witec,np.zeros(len(witec)),3,marker="")
ax3.scatter(witec,  linear-witec, 3,marker="v", label='with linear regression')
ax3.scatter(witec,  quadrat-witec, 3,marker="x", label='with quadratic regression')



plt.title("Error for Measurement with Setup "+str(setup))
plt.xlabel("reference analyser measurement [vol\%]")
plt.ylabel("error [vol\%]")
plt.legend()
plt.show()






fig3, ax3 = plt.subplots()
x=np.linspace(0,len(device),len(device))
ax3.scatter(witec,np.zeros(len(witec)),3,marker="")
# ax3.scatter(witec,100*abs(   ( abs(witec) - abs(linear))/witec), 3,marker="v", label='with linear regression')
# ax3.scatter(witec,100*abs(   ( abs(witec) - abs(quadrat))/witec), 3,marker="x", label='with quadratic regression')
ax3.scatter(witec,100*(linear-witec)/witec, 3,marker="v", label='with linear regression')
ax3.scatter(witec,100*(quadrat-witec)/witec, 3,marker="x", label='with quadratic regression')

plt.ylim([-20,20])

plt.title("Relative Error for Measurement with Setup "+str(setup))
plt.xlabel("reference analyser measurement [vol\%]")
plt.ylabel("relative error [\%]")
plt.legend()
plt.show()








#print(witec[von:bis])
print('standard deviation:')
s=np.std(linear[0:zerobis])
print(s)





#berechnung residual standard deviation
n=len(device[von:bis])
sum0=0
for i in range(n-1):
    w=witec[von+i]
    
    k=linear[von+i]
    #print(w - k)
    #diff=witec[21+i]-m*device[21+i]
    diff=w-k
    sum0=sum0+(diff)**2
print('Sres=')
print(np.sqrt(1/(n-2)*sum0))

print('accuracy: (max rel. fehler) derl linearen regression')
print(max(abs(     (     abs(witec[von:bis])  - abs(linear[von:bis] ))  /witec[von:bis])))


print('Precision')
print('Precision')
print('Precision')
zeromean=np.mean(linear[0:zerobis])
print(s/zeromean)
print('repeatability')
print(2*np.sqrt(2)*s)
lod=zeromean+2*s
print('LOD=')
print(lod)
print('LOQ=')
print(lod*3.3)


#print(witec[25:50])

print('QUADRATISCH im linearen bereich')

print('standard deviation quadrat:')
s=np.std(quadrat[0:zerobis])
print(s)

#berechnung residual standard deviation
n=len(device[von:bis])
sum0=0
for i in range(n-1):
    w=witec[von+i]
    
    k=quadrat[von+i]
   
    diff=w-k
    sum0=sum0+(diff)**2
print('Sres_quadrlin=')
print(np.sqrt(1/(n-2)*sum0))

print('accuracyquadratlin: (max rel. fehler) derl quatdratischen regression lin')
print(max(abs(     (     abs(witec[von:bis])  - abs(quadrat[von:bis] ))  /witec[von:bis])))




print('Precisionquadratlin')
zeromean=np.mean(quadrat[0:zerobis])
print(s/zeromean)
print('repeatabilityquadratlin')
print(2*np.sqrt(2)*s)
lod=zeromean+2*s
print('LODquadratlin=')
print(lod)
print('LOQquadratlin=')
print(lod*3.3)



print('QUADRATISCH im vollen bereich')

#berechnung residual standard deviation
n=len(device)
sum0=0
for i in range(n-1):
    w=witec[i]
    
    k=quadrat[i]
   
    diff=w-k
    sum0=sum0+(diff)**2
print('Sres_quadratvoll=')
print(np.sqrt(1/(n-2)*sum0))

print('accuracyquadratvoll: (max rel. fehler) derl quatdratischen regression')
print(max(abs(     (     abs(witec[ohnenull:])  - abs(quadrat[ohnenull:] ))  /witec[ohnenull:])))
print('absolutteil accuracy:')
print(max(abs(abs(witec[0:zerobis])-abs(quadrat[0:zerobis]))))


print('Precisionquadratvoll')
zeromean=np.mean(quadrat[0:zerobis])
print(s/zeromean)
print('repeatabilityquadratvoll')
print(2*np.sqrt(2)*s)
lod=zeromean+2*s
print('LODquadratvoll=')
print(lod)
print('LOQquadratvoll=')
print(lod*3.3)


