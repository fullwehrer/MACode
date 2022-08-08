
import numpy as np
import matplotlib.pyplot as plt
plt.style.use(['robert'])




#choose setup A or B
setup ='A'




#Messwerte zur Kalibrierung

#19.11.21
#star_calib_1  
generator_star_calib_1=[0,5,80]
witec_star_calib_1=[0.0047,0.09,3.852]
grossaufbau_star_calib_1=[0.00127,0.05221,1.43761]

#star_calib_3 
generator_star_calib_3=[0,10,0,15,20,0,25,30,0,40]
witec_star_calib_3=[-0.0014,0.3328,0.0018,0.7091,0.7576,0.0016,1.04226,1.3659,-0.00226,1.935]
grossaufbau_star_calib_3=[-0.00148,0.16071,-0.00320,0.32808,0.34827,-0.00466,0.46651,0.59621,-0.00706,0.81023]

#star_calib_4 
generator_star_calib_4=[50,60,70,80,0]
witec_star_calib_4=[2.4481,2.95100,3.44404,3.8883,-0.00027]
grossaufbau_star_calib_4=[1.00009,1.16368,1.31115,1.43240,0.00011]


#22.11.21 14:30
#star_calib_y_2 
generator_star_calib_y_2=[0,5,10,15,0,20]
witec_star_calib_y_2=[-0.00735,0.11375,0.32093,0.64772,0.01688,0.73939]
grossaufbau_star_calib_y_2=[0.00050,0.06065,0.16375,0.31926,-0.00197,0.35468]

#star_calib_y_3
generator_star_calib_y_3=[0,20,25,30,40,50,60,70,80,0]
witec_star_calib_y_3=[-0.01014,0.74983,1.01867,1.32130,1.88986,2.38676,2.88005,3.36225,3.77836,-0.01699]
grossaufbau_star_calib_y_3=[-0.00268,0.35681,0.47001,0.59674,0.81288,0.98616,1.14986,1.29560,1.41337,-0.00419]


#22.11.21 14:30
#star_calib_z
generator_star_calib_4=[0,80,70,60,50,0,40,30,25,20,0,15,10,5,0]
witec_star_calib_4=[-0.00511,3.87641,3.33992,2.82724,2.33140,-0.00276,1.86871,1.32528,1.01511,0.73634,-0.00075,0.74028,0.36558,0.13068,0.00132]
grossaufbau_star_calib_4=[0.00066,1.45393,1.30263,1.14432,0.97726,0.00322,0.80743,0.59686,0.46922,0.35022,0.00290,0.35171,0.18079,0.07059,0.00117]

witec_a=witec_star_calib_1+witec_star_calib_3+witec_star_calib_4+witec_star_calib_y_2+witec_star_calib_y_3+witec_star_calib_4
gross=grossaufbau_star_calib_1+grossaufbau_star_calib_3+grossaufbau_star_calib_4+grossaufbau_star_calib_y_2+grossaufbau_star_calib_y_3+grossaufbau_star_calib_4



#KLEIN

#klein_calib_3 1.12.21 18:00
gen_3=[0,5,10,15,20,0,25,30,40,50,0,60,70,80,0]
klein_3=[0.00191,0.07135,0.19630,0.38316,0.37980,0.00901,0.51671,0.66064,0.89856,1.09342,0.01382,1.28334,1.44860,1.58136,0.01713]
witec_3 =[-0.00700,0.11201,0.34525,0.71659,0.70699,-0.00976,0.99004,1.30331,1.84235,2.30868,0.00991,2.78750,3.22998,3.60923,-0.00849]

#lost6 2.12.21 15:18
gen_lost6=[0,80,70,60,0,50,40,30,25,0,20,15,10,5,0]
klein_lost6=[0.00120,1.66552,1.47198,1.28174,0.00563,1.09985,0.89926,0.6635096,0.51870889,0.0080611,0.3711069,0.4018662,0.20907,0.0808235,-0.0012346]
witec_lost6=[-0.00261,3.90736,3.34800,2.82392,-0.00120,2.36191,1.87573,1.33607,1.01766,-0.00195,0.72223,0.78647,0.39409,0.14514,-0.00495]

#klein_calib_91011 2.12.21 16:55
gen_91011=[0,40,50,60,70,0,80,5,10,15,0,20,25,30,0]
klein_91011=[0.000401,0.926909,1.1315334,1.3288483,1.5023829,0.00108,1.665096,0.0825219,0.2136137,0.4096925,0.0011601,0.3727244,0.51781,0.669472,0.0031042]
witec_91011=[-0.00143,1.98446,2.48828,3.00267,3.48751,-0.00128,3.95573,0.14678,0.40001,0.80290,-0.00165,0.72177,1.03003,1.36476,-0.00135]

witec_b=witec_3+witec_lost6+witec_91011
klein=klein_3+klein_lost6+klein_91011





if (setup == 'A'):
    device=gross
    witec=witec_a
    von=21
    bis=46
elif(setup=='B'):
    device=klein
    witec=witec_b
    von=16
    bis=33
else:
    print('error choosing a setup!!!')
    exit()








#create array and sort
a=np.array([witec,device])
b=a[:,a[0,:].argsort()]
witec=b[0]
device=b[1]


print(witec[von:bis])


def lin_lstsq(v_abs, manual): # linear regression
    y=manual
    A=np.vstack([v_abs, np.ones(len(v_abs))]).T
    m, c=np.linalg.lstsq(A, y, rcond=None)[0]
    print('m=')
    print(m)
    print('c=')
    print(c)
    return [m, c]
def quad_lstsq(v_abs, manual):
    from numpy.polynomial import polynomial as P
    y=manual
    x=v_abs
    c=P.polyfit(x,y,2)
    return c



fig3, ax3 = plt.subplots()
ax3.set_title("Calibration")

#v_abs=calc_abs(temperature, pressure, pd_ref, pd_ds_ref, pd_main, pd_ds_main, zerofactor)

ax3.scatter(witec, device, 3, label='measured data')
#ax3.boxplot([manual, (temperature+273.15)/t_norm * p_norm/pressure *np.log((pd_ref - pd_ds_ref)/((pd_main - pd_ds_main)*zerofactor))])
[m,c]=lin_lstsq(device[von:bis], witec[von:bis])
[a1, a2, a3]=quad_lstsq(device, witec)


x=np.linspace(0,max(device),500)
next(ax3._get_lines.prop_cycler) 
ax3.plot(m*x+c, x, label='linear regression')
ax3.plot(a3*x**2+a2*x+a1,x, label='quadratic regression')
plt.title("Absorption vs Concentration - Setup "+str(setup))
# if use_plotcounter:
#     plt.xlabel("measurement number [ ]")
# else: plt.xlabel("concentration [µg/ml]")
plt.xlabel("concentration [vol\%]")
plt.ylabel("absorption [AU]")
plt.legend()

plt.show()

print('a3, a2, a1')
print(a3)
print(a2)
print(a1)

de=25
a=46


#berechnung residual standard deviation
n=len(device[von:bis])
sum0=0
for i in range(n-1):
    w=witec[21+i]
    g=device[21+i]
    k=m*g+c
    #k=a3*g**2+a2*g+a1
    diff=w-k
    sum0=sum0+(diff)**2
print('Sres=')
print(np.sqrt(1/(n-2)*sum0))


#berechnung R_quadrat
actual=witec[von:bis]
predict=m*device[von:bis]+c

corr_matrix=np.corrcoef(actual, predict)
corr=corr_matrix[0,1]
R_sq=corr**2
print('R**2=')
print(R_sq)



# plt.plot(range(len(witec[21:46])), witec[21:46], label='witec')
# plt.plot(range(len(witec[21:46])), m*gross[21:46]+c, label='eigen')

# plt.show()

#berechnung residual standard deviation
n=len(device)
sum0=0
for i in range(n-1):
    w=witec[i]
    g=device[i]
    #k=m*g+c
    k=a3*g**2+a2*g+a1
    diff=w-k
    sum0=sum0+(diff)**2
print('Sres_gesqad=')
print(np.sqrt(1/(n-2)*sum0))


#berechnung R_quadrat
actual=witec

predict=a3*device**2+a2*device+a1
corr_matrix=np.corrcoef(actual, predict)
corr=corr_matrix[0,1]
R_sq=corr**2
print('R**2_gesquad=')
print(R_sq)