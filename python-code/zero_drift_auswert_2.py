import numpy as np
from tkinter import filedialog
file_path = filedialog.askopenfilename()
Tdata= np.loadtxt(file_path, delimiter=",")
fdata1=Tdata.transpose()
file_path = filedialog.askopenfilename()
Tdata= np.loadtxt(file_path, delimiter=",")
fdata2=Tdata.transpose()
file_path = filedialog.askopenfilename()
Tdata= np.loadtxt(file_path, delimiter=",")
fdata3=Tdata.transpose()
file_path = filedialog.askopenfilename()
Tdata= np.loadtxt(file_path, delimiter=",")
fdata4=Tdata.transpose()
file_path = filedialog.askopenfilename()
Tdata= np.loadtxt(file_path, delimiter=",")
fdata5=Tdata.transpose()
import matplotlib.pyplot as plt


plt.style.use(['robert'])

#choose setup A or B
setup ='A'





t_norm = 273.15 # standard temperature in K
p_norm = 1000 # standard pressure in hPa
fig1, ax1 = plt.subplots()
if (setup=='A'):
    ax1.set_title("Zero Drift for Setup A")
    m=2.4311
    c=-0.10122

    a3=0.51444
    a2=1.9140
    a1=0.00076056
elif(setup=='B'):
    ax1.set_title("Zero Drift for Setup B")
    m=2.1760
    c=-0.095042

    a3=0.32845
    a2=1.8003
    a1=-0.0088889
else:
    print('error choosing a setup!!!')
    exit()
ax1.set_xlabel("time [s]")
ax1.set_ylabel("concentration [vol\%]")

time_step1= fdata1[0]
pd_main1 = fdata1[6]
pd_ref1 = fdata1[7]
manual1 = fdata1[8]
pd_ds_main1 = fdata1[13]
pd_ds_ref1 = fdata1[14]
zerofactor1 = fdata1[9]
pressure1 = fdata1[12]
temperature1 = fdata1[11]

time_step2= fdata2[0]
pd_main2 = fdata2[6]
pd_ref2 = fdata2[7]
manual2 = fdata2[8]
pd_ds_main2 = fdata2[13]
pd_ds_ref2 = fdata2[14]
zerofactor2 = fdata2[9]
pressure2 = fdata2[12]
temperature2 = fdata2[11]

time_step3= fdata3[0]
pd_main3 = fdata3[6]
pd_ref3 = fdata3[7]
manual3 = fdata3[8]
pd_ds_main3 = fdata3[13]
pd_ds_ref3 = fdata3[14]
zerofactor3 = fdata3[9]
pressure3 = fdata3[12]
temperature3 = fdata3[11]

time_step4= fdata4[0]
pd_main4 = fdata4[6]
pd_ref4 = fdata4[7]
manual4 = fdata4[8]
pd_ds_main4 = fdata4[13]
pd_ds_ref4 = fdata4[14]
zerofactor4 = fdata4[9]
pressure4 = fdata4[12]
temperature4 = fdata4[11]

time_step5= fdata5[0]
pd_main5 = fdata5[6]
pd_ref5 = fdata5[7]
manual5 = fdata5[8]
pd_ds_main5 = fdata5[13]
pd_ds_ref5 = fdata5[14]
zerofactor5 = fdata5[9]
pressure5 = fdata5[12]
temperature5 = fdata5[11]


abs1=(temperature1+t_norm)/t_norm * p_norm/pressure1 *np.log((pd_ref1 - pd_ds_ref1)/((pd_main1 - pd_ds_main1)*zerofactor1))
abs2=(temperature2+t_norm)/t_norm * p_norm/pressure2 *np.log((pd_ref2 - pd_ds_ref2)/((pd_main2 - pd_ds_main2)*zerofactor2))
abs3=(temperature3+t_norm)/t_norm * p_norm/pressure3 *np.log((pd_ref3 - pd_ds_ref3)/((pd_main3 - pd_ds_main3)*zerofactor3))
abs4=(temperature4+t_norm)/t_norm * p_norm/pressure4 *np.log((pd_ref4 - pd_ds_ref4)/((pd_main4 - pd_ds_main4)*zerofactor4))
abs5=(temperature5+t_norm)/t_norm * p_norm/pressure5 *np.log((pd_ref5 - pd_ds_ref5)/((pd_main5 - pd_ds_main5)*zerofactor5))



conc1=a3*abs1**2+a2*abs1+a1
conc2=a3*abs2**2+a2*abs2+a1
conc3=a3*abs3**2+a2*abs3+a1
conc4=a3*abs4**2+a2*abs4+a1
conc5=a3*abs5**2+a2*abs5+a1


ax1.plot(fdata1[0], conc1, label="series of meas. 1")
ax1.plot(fdata2[0], conc2, label="series of meas. 2")
ax1.plot(fdata3[0], conc3, label="series of meas. 3")
ax1.plot(fdata4[0], conc4, label="series of meas. 4")
ax1.plot(fdata5[0], conc5,'m', label="series of meas. 5")
plt.legend()
plt.show()



fig2, ax2 = plt.subplots()
ax2.set_title("Temperatures during Zero Drift for Setup "+str(setup))
ax2.set_xlabel("time [s]")
ax2.set_ylabel("temperature [°C]")

ax2.plot(fdata1[0], temperature1, label="series of meas. 1")
ax2.plot(fdata2[0], temperature2, label="series of meas. 2")
ax2.plot(fdata3[0], temperature3, label="series of meas. 3")
ax2.plot(fdata4[0], temperature4, label="series of meas. 4")
ax2.plot(fdata5[0], temperature5,'m', label="series of meas. 5")
plt.legend()
plt.show()


fig2, ax2 = plt.subplots()
ax2.set_title("Pressure during Zero Drift for Setup "+str(setup))
ax2.set_xlabel("time [s]")
ax2.set_ylabel("pressure [hPa]")

ax2.plot(fdata1[0], pressure1, label="series of meas. 1")
ax2.plot(fdata2[0], pressure2, label="series of meas. 2")
ax2.plot(fdata3[0], pressure3, label="series of meas. 3")
ax2.plot(fdata4[0], pressure4, label="series of meas. 4")
ax2.plot(fdata5[0], pressure5,'m', label="series of meas. 5")
plt.legend()
plt.show()