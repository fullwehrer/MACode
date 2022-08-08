import matplotlib.pyplot as plt
#plt.style.use(['robert'])

import numpy as np
from tkinter import filedialog

t_norm = 273.15 # standard temperature in K
p_norm = 1000 # standard pressure in hPa





filename = filedialog.askopenfilename()
Tdata= np.loadtxt(filename, delimiter=",")
fdata=Tdata.transpose()


measpack=10


period_data= fdata[0]
ads15_data0 = fdata[6]
ads15_data1 = fdata[7]
manual = fdata[8]
darksignal_data0 = fdata[13]
darksignal_data1 = fdata[14]
zerofactor_data = fdata[9]
bmp280_data = fdata[12]
mcp9808_data = fdata[11]




ll=len(period_data)-measpack 

for x in range(0,int(len(period_data)/measpack)):
    von = x*measpack
    bis = x*measpack+measpack
    tenabs = (np.array(mcp9808_data[von:bis])+t_norm)/t_norm* p_norm/np.array(bmp280_data[von:bis]) *np.log((np.array(ads15_data1[von:bis]) - np.array(darksignal_data1[von:bis]))/((np.array(ads15_data0[von:bis]) - np.array(darksignal_data0[von:bis]))*np.array(zerofactor_data[von:bis])))   
    userread = np.median(tenabs)
    print('manual: '+str(manual[x*measpack])+'- Absorption: ' + str(userread))


