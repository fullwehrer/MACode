
##Please select###############################################################################################



## plot what?
manual_measurement = True #make parallel measurements by manual_measurement
mcp3208 = False #use MCP3208 A/D converter?(True/False) 
wavePrec = False #use Waveshare (ADS1256) A/D converter?(True/False) 
max31865 = False # use Adafruit max31865 PT100 temperature measurement module?(True/False) 
ads1115 = True #use ADS1115 A/D converter?(True/False) 
zeroF = True # add zeroing data to the overall data file? (True/False)
mcp9808 = False # use Adafruit mcp9808 temperature measurement module?(True/False)
bmp280 = False # use Adafruit bmp280 pressure measurement module?(True/False)


use_plotcounter = True #plot with numbers instead of time on x-axis?(True/False) 


##End of selection###############################################################################################



import matplotlib.pyplot as plt
#plt.style.use(['robert'])

import numpy as np
from tkinter import filedialog

t_norm = 273.15 # standard temperature in K
p_norm = 1000 # standard pressure in hPa



def plotfile(filename, mcpyn, waveyn, max31865yn, ads15yn, manualyn, baroyn, mcp9808yn, bmp280yn):
    Tdata= np.loadtxt(filename, delimiter=",")
    fdata=Tdata.transpose()
    
    
    
    if use_plotcounter: 
            datapoints = len(fdata[0])
            fdata[0] = range(1,datapoints+1)


    fig1, ax1 = plt.subplots()
    
    ax1.set_title("Sensor Signal")
    if use_plotcounter:
        ax1.set_xlabel("measurement number [ ]")
    else: ax1.set_xlabel("time [s]")
    ax1.set_ylabel("voltage [V]")
           





    if (mcpyn == True):
        ax1.plot(fdata[0], fdata[1], label="main MCP3208")
        ax1.plot(fdata[0], fdata[2], label="ref. MCP3208")
    if (waveyn == True):
        ax1.plot(fdata[0], fdata[3], label="main ADS1256")
        ax1.plot(fdata[0], fdata[4], label="ref. ADS1256")
    if (max31865yn == True):
        ax1.plot(fdata[0], fdata[5], label="max31865")
    if (ads15yn == True):
        ax1.plot(fdata[0], fdata[6], label="main ADS1115")
        ax1.plot(fdata[0], fdata[7], label="ref. ADS1115")
    if (manualyn == True):
        ax2 = ax1.twinx()
        ax2.set_ylabel('concentration [µg/ml]')
        ax2.plot(fdata[0], fdata[8], 'm', label="manual measurement" )

    if (baroyn == True):
        ax1.plot(fdata[0], fdata[9], label="Barometer")
    if (mcp9808yn == True):
        ax3 = ax1.twinx()
        ax3.set_ylabel('Temperature [°C]')
        ax3.plot(fdata[0], fdata[11], label="mcp9808")
    if (bmp280yn == True):
        ax1.plot(fdata[0], fdata[12], label="bmp280")

    
    # if use_plotcounter:
    #     plt.xlabel("measurement number [ ]")
    # else: plt.xlabel("time [s]")
    # plt.ylabel("voltage [V]")


    # ax1.legend()
    # ax2.legend()
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines1 + lines2, labels1 + labels2)

    plt.show()



def plotclean(filename, mcpyn, waveyn, max31865yn, ads15yn, manualyn, baroyn, mcp9808yn, bmp280yn):
    Tdata= np.loadtxt(filename, delimiter=",")
    fdata=Tdata.transpose()
    
    time_step= fdata[0]
    pd_main = fdata[6]
    pd_ref = fdata[7]
    pd_ds_main = fdata[13]
    pd_ds_ref = fdata[14]
    zerofactor = fdata[9]
    
    
    if use_plotcounter: 
            datapoints = len(fdata[0])
            fdata[0] = range(1,datapoints+1)

    

    
    #plt.plot(time_step, pd_ref/pd_main, label="relative signal untreated")
    #plt.plot(time_step, pd_ref/(pd_main*zerofactor), label="relative signal with zeroing")
    #plt.plot(time_step, (pd_ref - pd_ds_ref)/(pd_main - pd_ds_main), label="relative signal with dark signal subtraction")
    plt.plot(time_step, (pd_ref - pd_ds_ref)/((pd_main - pd_ds_main)*zerofactor), label="relative signal zeroing and dark signal subtraction [ ]")
    plt.plot(time_step, (pd_main-pd_ds_main)*zerofactor, label="main ADS1115 with zeroing factor [V]")
    plt.plot(time_step, (pd_ref - pd_ds_ref), label="ref. ADS1115 [V]")
    

    plt.title("relative signal (after dark signal subtraction and zeroing)")
    if use_plotcounter:
        plt.xlabel("measurement number [ ]")
    else: plt.xlabel("time [s]")
    plt.ylabel("I0/I [ ]")
    plt.legend()

    plt.show()

def plotabs(filename, mcpyn, waveyn, max31865yn, ads15yn, manualyn, baroyn, mcp9808yn, bmp280yn):
    Tdata= np.loadtxt(filename, delimiter=",")
    fdata=Tdata.transpose()
    
    time_step= fdata[0]
    pd_main = fdata[6]
    pd_ref = fdata[7]
    manual = fdata[8]
    pd_ds_main = fdata[13]
    pd_ds_ref = fdata[14]
    zerofactor = fdata[9]
    pressure = fdata[12]
    temperature = fdata[11]
    

    fig3, ax3 = plt.subplots()
    ax3.set_title("Sensor Signal")

    v_abs=calc_abs(temperature, pressure, pd_ref, pd_ds_ref, pd_main, pd_ds_main, zerofactor)

    ax3.scatter(manual, v_abs, 3)
    #ax3.boxplot([manual, (temperature+273.15)/t_norm * p_norm/pressure *np.log((pd_ref - pd_ds_ref)/((pd_main - pd_ds_main)*zerofactor))])
    [m,c]=lin_lstsq(file_path)
    
    ax3.plot(m*v_abs+c, v_abs)
    plt.title("Absorption vs Concentration")
    # if use_plotcounter:
    #     plt.xlabel("measurement number [ ]")
    # else: plt.xlabel("concentration [µg/ml]")
    plt.xlabel("concentration [µg/ml]")
    plt.ylabel("absorption [AU]")
    # plt.legend()

    plt.show()

def calc_abs(temp, press, pd_ref, pd_ds_ref, pd_main, pd_ds_main, zerofactor):#calculate absorption
    return (temp+273.15)/t_norm * p_norm/press *np.log((pd_ref - pd_ds_ref)/((pd_main - pd_ds_main)*zerofactor))

def lin_lstsq(filename): # linear regression
    Tdata= np.loadtxt(filename, delimiter=",")
    fdata=Tdata.transpose()

    pd_main = fdata[6]
    pd_ref = fdata[7]
    manual = fdata[8]
    pd_ds_main = fdata[13]
    pd_ds_ref = fdata[14]
    zerofactor = fdata[9]
    pressure = fdata[12]
    temperature = fdata[11]


    y=manual
    abs=calc_abs(temperature, pressure, pd_ref, pd_ds_ref, pd_main, pd_ds_main, zerofactor)
    
    A=np.vstack([abs, np.ones(len(abs))]).T
    m, c=np.linalg.lstsq(A, y, rcond=None)[0]
    return [m, c]

file_path = filedialog.askopenfilename()

plotabs(file_path,mcp3208, wavePrec, max31865, ads1115, manual_measurement, False, mcp9808, bmp280)








