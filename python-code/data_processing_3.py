
##Please select###############################################################################################



## plot what?
manual_measurement = False #make parallel measurements by manual_measurement
mcp3208 = False #use MCP3208 A/D converter?(True/False) 
wavePrec = False #use Waveshare (ADS1256) A/D converter?(True/False) 
max31865 = False # use Adafruit max31865 PT100 temperature measurement module?(True/False) 
ads1115 = True #use ADS1115 A/D converter?(True/False) 
zeroF = False # add zeroing data to the overall data file? (True/False)
mcp9808 = False # use Adafruit mcp9808 temperature measurement module?(True/False)
bmp280 = False # use Adafruit bmp280 pressure measurement module?(True/False)


use_plotcounter = False #plot with numbers instead of time on x-axis?(True/False) 


##End of selection###############################################################################################



import matplotlib.pyplot as plt
plt.style.use(['robert'])

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
    
    ax1.set_title("Exemplary Sensor Signal")
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
        ax1.plot(fdata[0], fdata[6], label="main photosensor")
        ax1.plot(fdata[0], fdata[7], label="ref. photosensor")
        
    if (manualyn == True):
        ax2 = ax1.twinx()
        ax2.set_ylabel('concentration [µg/ml]')
        next(ax2._get_lines.prop_cycler) 
        next(ax2._get_lines.prop_cycler) 
        ax2.plot(fdata[0], fdata[8], label="manual measurement" )

    if (baroyn == True):
        ax1.plot(fdata[0], fdata[9], label="Barometer")
    if (mcp9808yn == True):
        ax3 = ax1.twinx()
        ax3.set_ylabel('temperature [°C]')
        next(ax3._get_lines.prop_cycler) 
        next(ax3._get_lines.prop_cycler) 
        next(ax3._get_lines.prop_cycler) 
        ax3.plot(fdata[0], fdata[11], label="temperature")
    if (bmp280yn == True):
        ax1.plot(fdata[0], fdata[12], label="bmp280")

    
    # if use_plotcounter:
    #     plt.xlabel("measurement number [ ]")
    # else: plt.xlabel("time [s]")
    # plt.ylabel("voltage [V]")


    # ax1.legend()
    # ax2.legend()
    lines1, labels1 = ax1.get_legend_handles_labels()
    
    if manual_measurement: 
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax2.legend(lines1 + lines2, labels1 + labels2)
    elif mcp9808yn:
        lines3, labels3 = ax3.get_legend_handles_labels()
        ax3.legend(lines1 + lines3, labels1 + labels3)
    else: ax1.legend(lines1, labels1)

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

    
    fig1, ax1 = plt.subplots()
    
    ax1.set_title("Relative Signal")
    if use_plotcounter:
        ax1.set_xlabel("measurement number [ ]")
    else: ax1.set_xlabel("time [s]")
    ax1.set_ylabel("relative signal [ ]")



    ax2 = ax1.twinx()
    ax2.set_ylabel("voltage [V]")
        
    
    #plt.plot(time_step, pd_ref/pd_main, label="relative signal untreated")
    #plt.plot(time_step, pd_ref/(pd_main*zerofactor), label="relative signal with zeroing")
    #plt.plot(time_step, (pd_ref - pd_ds_ref)/(pd_main - pd_ds_main), label="relative signal with dark signal subtraction")
    
    ax2.plot(time_step, (pd_main-pd_ds_main)*zerofactor, label="main photosensor with zeroing factor")
    ax2.plot(time_step, (pd_ref - pd_ds_ref), label="ref. photosensor")
    
    next(ax1._get_lines.prop_cycler)
    next(ax1._get_lines.prop_cycler) 


    ax1.plot(time_step, (pd_ref - pd_ds_ref)/((pd_main - pd_ds_main)*zerofactor), label="relative signal")

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines1 + lines2, labels1 + labels2)
    # ax1.legend(lines1, labels1)
    

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

    ax3.scatter(manual, v_abs, 3, label='measured data')
    #ax3.boxplot([manual, (temperature+273.15)/t_norm * p_norm/pressure *np.log((pd_ref - pd_ds_ref)/((pd_main - pd_ds_main)*zerofactor))])
    [m,c]=lin_lstsq(v_abs[:4000], manual[:4000])
    [a1, a2, a3]=quad_lstsq(v_abs, manual)
    
    
    x=np.linspace(0,max(v_abs),500)
    next(ax3._get_lines.prop_cycler) 
    ax3.plot(m*x+c, x, label='linear regression')
    ax3.plot(a3*x**2+a2*x+a1,x, label='quadratic regression')
    plt.title("Absorption vs Concentration")
    # if use_plotcounter:
    #     plt.xlabel("measurement number [ ]")
    # else: plt.xlabel("concentration [µg/ml]")
    plt.xlabel("concentration [µg/ml]")
    plt.ylabel("absorption [AU]")
    plt.legend()

    plt.show()

def calc_abs(temp, press, pd_ref, pd_ds_ref, pd_main, pd_ds_main, zerofactor):#calculate absorption
    return (temp+t_norm)/t_norm * p_norm/press *np.log((pd_ref - pd_ds_ref)/((pd_main - pd_ds_main)*zerofactor))

def lin_lstsq(v_abs, manual): # linear regression
    y=manual
    A=np.vstack([v_abs, np.ones(len(v_abs))]).T
    m, c=np.linalg.lstsq(A, y, rcond=None)[0]
    print(m)
    print(c)
    return [m, c]
def quad_lstsq(v_abs, manual):
    from numpy.polynomial import polynomial as P
    y=manual
    x=v_abs
    c=P.polyfit(x,y,2)
    return c

def plotds(filename, mcpyn, waveyn, max31865yn, ads15yn, manualyn, baroyn, mcp9808yn, bmp280yn):
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

    
    fig1, ax1 = plt.subplots()
    
    ax1.set_title("Dark Signal")
    if use_plotcounter:
        ax1.set_xlabel("measurement number [ ]")
    else: ax1.set_xlabel("time [s]")
    ax1.set_ylabel("dark signal [V]")



    
        
    
    #plt.plot(time_step, pd_ref/pd_main, label="relative signal untreated")
    #plt.plot(time_step, pd_ref/(pd_main*zerofactor), label="relative signal with zeroing")
    #plt.plot(time_step, (pd_ref - pd_ds_ref)/(pd_main - pd_ds_main), label="relative signal with dark signal subtraction")
    


    ax1.plot(time_step, pd_ds_main, label="main photodiode")
    ax1.plot(time_step, pd_ds_ref, label="ref. photodiode")

    lines1, labels1 = ax1.get_legend_handles_labels()
    
    ax1.legend(lines1, labels1)
    # ax1.legend(lines1, labels1)
    

    plt.show()








file_path = filedialog.askopenfilename()
plotfile(file_path,mcp3208, wavePrec, max31865, ads1115, manual_measurement, False, mcp9808, bmp280)
plotclean(file_path,mcp3208, wavePrec, max31865, ads1115, manual_measurement, False, mcp9808, bmp280)
plotds(file_path,mcp3208, wavePrec, max31865, ads1115, manual_measurement, False, mcp9808, bmp280)








