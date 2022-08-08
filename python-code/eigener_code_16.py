
##Please select###############################################################################################


##measure? and if yes, how?
from tkinter.constants import FALSE
#from matplotlib.markers import MarkerStyle


measure = True #do a measurement? (True/False) 
timelimit = 300#time for the measurement in seconds (float). DO NOT select too short as user input duration also counts into this time.
use_meas_counter = False #use a number of measurement instead of time as limit for measuring loop? (True/False) 
noofmeasurements = 1000# define number of measurements taken in case of use_meas_counter = True. (integer)
sporadic = False# take sporadic measurements only? (for long term measurements) (True/False)
savecont = False # save continuously every minute or so? (True/False)


##name the data?
namedata = True #if not selected, filename will be "data" and timestamp


##if measure, what?
manual_measurement = False #make parallel measurements by manual_measurement
absorption_measurement = True # do an absorption measurement?(True/False) -- OVERRIDES all following settings in this section
#
mcp3208 = False #use MCP3208 A/D converter?(True/False) 
wavePrec = False #use Waveshare (ADS1256) A/D converter?(True/False) 
max31865 = False # use Adafruit max31865 PT100 temperature measurement module?(True/False) 
ads1115 = True #use ADS1115 A/D converter?(True/False) 
zeroF = True # add zeroing data to the overall data file? (True/False)
timestamps = True #add a timestamp for each measurement?(True/False) 
mcp9808 = False # use Adafruit mcp9808 temperature measurement module?(True/False)
bmp280 = False # use Adafruit bmp280 pressure measurement module?(True/False)
led = True # use LED?(True/False)
darksignal = True # do a dark signal reading at all? (True/False)
darksignal_spor=False # do an occasional reading of the dark signal? (True/False)


## use gain amplification?
gain = 4 # gain amplification of the ADS1115

##plot? and if yes, how?
plot = True #display plots?(True/False) 
use_plotcounter = False #plot with numbers instead of time on x-axis?(True/False) 
posx = 100 # x-position of plot
posy = 100 # y-position of plot

## LED dim mode
pwm = False # analog is always on but can be set to max then use PWM
duty = 0 # duty cycle of PWM signal. 0 is LED full on

##End of selection###############################################################################################


import matplotlib
import matplotlib.pyplot as plt

import numpy as np

import time
from datetime import datetime

import RPi.GPIO as GPIO #initialisation of LED and Fan
ledpin = 24
pwmpin = 19
fanpin = 23
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledpin, GPIO.OUT)
GPIO.output(ledpin, GPIO.LOW) # make sure LED is off on startup
GPIO.setup(pwmpin, GPIO.OUT)
if pwm:
    led_pwm = GPIO.PWM(pwmpin,1000)
    led_pwm.start(100)
    GPIO.output(ledpin, GPIO.HIGH)
else: GPIO.output(pwmpin, GPIO.LOW)
    
GPIO.setup(fanpin, GPIO.OUT)
GPIO.output(fanpin, GPIO.LOW) # make sure Fan is off on startup

import csv




if (manual_measurement and sporadic):
    print('Please check selected options. Manual and sporadic dont mix well')
    exit() 
if (not sporadic and savecont):
    print('Are you sure you need continuous saving?')
    time.sleep(10)
if (sporadic and not savecont):
    print('Please consider enabling continuous saving in case the long term measurement is halted')
    time.sleep(10)


if not ads1115: darksignal = False

if absorption_measurement:
    mcp3208 = False 
    wavePrec = False 
    max31865 = False 
    ads1115 = True 
    zeroF = True 
    timestamps = True
    mcp9808 = True
    bmp280 = True
    namedata = True
    led=True
    darksignal = True
    


if not ads1115: darksignal = False


measpack = 10 # number of measurements made in succession


if plot: 
    plt.style.use(['robert'])
    #print(plt.style.available)


if (not measure and plot):
    import tkinter as tk
    from tkinter import filedialog




if mcp3208:
    import gpiozero
    


if wavePrec:
    ##begin AD
    import sys
    import os
    from pipyadc.ADS1256_definitions import *
    from pipyadc import ADS1256

    POTI = POS_AIN0|NEG_AINCOM
    # Light dependant resistor of the same board:
    LDR  = POS_AIN1|NEG_AINCOM
    # The other external input screw terminals of the Waveshare board:
    EXT2, EXT3, EXT4 = POS_AIN2|NEG_AINCOM, POS_AIN3|NEG_AINCOM, POS_AIN4|NEG_AINCOM
    EXT5, EXT6, EXT7 = POS_AIN5|NEG_AINCOM, POS_AIN6|NEG_AINCOM, POS_AIN7|NEG_AINCOM

    # You can connect any pin as well to the positive as to the negative ADC input.
    # The following reads the voltage of the potentiometer with negative polarity.
    # The ADC reading should be identical to that of the POTI channel, but negative.
    POTI_INVERTED = POS_AINCOM|NEG_AIN0

    # For fun, connect both ADC inputs to the same physical input pin.
    # The ADC should always read a value close to zero for this.
    SHORT_CIRCUIT = POS_AIN0|NEG_AIN0

    # Specify here an arbitrary length list (tuple) of arbitrary input channel pair
    # eight-bit code values to scan sequentially from index 0 to last.
    # Eight channels fit on the screen nicely for this example..
    #CH_SEQUENCE = (POTI, LDR, EXT2, EXT3, EXT4, EXT7, POTI_INVERTED, SHORT_CIRCUIT)
    CH_SEQUENCE = (EXT5, EXT7)


    ads = ADS1256()
    ads.cal_self()
    

    ##end AD







if max31865:
    ##begin temp
    import time
    import board
    import digitalio
    import adafruit_max31865

    spi = board.SPI()
    cs = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.
    max31865sensor = adafruit_max31865.MAX31865(spi, cs)
    ##end temp

if ads1115:
    import board
    import busio
    i2c = busio.I2C(board.SCL, board.SDA)
    import adafruit_ads1x15.ads1115 as ADS
    from adafruit_ads1x15.analog_in import AnalogIn
    ads15 = ADS.ADS1115(i2c)
    ads15.gain = gain
    print(ads15.gain)

if mcp9808:
    import board
    import busio
    i2c = busio.I2C(board.SCL, board.SDA)
    import adafruit_mcp9808
    mcp98 = adafruit_mcp9808.MCP9808(i2c)

if bmp280:
    import board
    import busio
    i2c = busio.I2C(board.SCL, board.SDA)
    import adafruit_bmp280
    bmp=adafruit_bmp280.Adafruit_BMP280_I2C(i2c)



    















def do_measurement():
    
    #determine name of measurement for later savefile
    
    if namedata: 
        print("Please type name for data file. (Timestamp will be attached automatically)")
        name= input() + "_"
    else: name = "data_"
    









    
    

    ## initial values for while loop
    time_last_rep = time.time()
    period = 0
    counter =0
    manual_measurement_value = 0
    meas = True
    time_reached = True # Timelimit is not reached if False
    old_period_bmp= -100001
    old_period_ds= -100001
    old_counter_spor = -1
    savenow = False
    interrupt = False
    old_period_limit = -1
    old_period_save = -1
    meastmp = True

    ## creation of arrays for appending data in measurement loop
    period_data = []
    mcp_data0 = []
    mcp_data1 = []
    wave_data5 = []
    wave_data7 = []
    max31865_data = []
    ads15_data0 =[]
    ads15_data1 =[]
    manual_measurement_data = []
    zerofactor_data= []
    timestamps_data = []
    mcp9808_data =[]
    bmp280_data = []
    darksignal_data0 = []
    darksignal_data1 = []



    rate_data = [] #not for saving; just for immediate information




    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d_%H-%M-%S")
    name = name + date_time

    print("please type >y< if you would like to do a fresh zeroing now. Else type any other letter.")
    dozero = input()
    ds=getDarkSignal()
    if ads1115: zeroFactor=zeroing(dozero == "y",ds)
    else: zeroFactor = 1
    
    
    while meas:
        
        meas=meastmp
        
        #if ((use_meas_counter and (counter % noofmeasurements ==0)) and manual_measurement):
        if manual_measurement:
            if ((use_meas_counter and (counter % noofmeasurements ==0)) or time_reached ):
                ledTurnOff()
                print("Please dial in a new value for the manual_measurement and type in the value here or type >q< to quit.")
                manual_measurement_value = input() #read in manual measurement by user
                # ledTurnOn()
                
                if (manual_measurement_value == "q"): meas = False #stop measurement if user typed "q"
                else: ds=getDarkSignal()
        time_reached = False # always set time_reached to False for first loop of time operation or every repetition of counter operation
        if (not use_meas_counter and (period >= timelimit+old_period_limit)): 
            time_reached = True #check if time limit is reached (if counter is not used)
            old_period_limit = period
        if not manual_measurement:
            if (use_meas_counter and (counter == noofmeasurements)):meas = False
            if (not use_meas_counter and time_reached): meas = False
        if (sporadic and not interrupt): meas = True
        if interrupt: meas=False
        if (savenow or not meas):
            data= np.array([period_data,mcp_data0, mcp_data1, wave_data5, wave_data7, max31865_data, ads15_data0, ads15_data1, manual_measurement_data, zerofactor_data, timestamps_data, mcp9808_data, bmp280_data, darksignal_data0, darksignal_data1 ])
            savedata(savecont, data, name, counter)   
            print('Data saved')

            ## empty data arrays after saving
            period_data = []
            mcp_data0 = []
            mcp_data1 = []
            wave_data5 = []
            wave_data7 = []
            max31865_data = []
            ads15_data0 =[]
            ads15_data1 =[]
            manual_measurement_data = []
            zerofactor_data= []
            timestamps_data = []
            mcp9808_data =[]
            bmp280_data = []
            darksignal_data0 = []
            darksignal_data1 = []

            savenow = False
        try:    
            if not meas: 
                print("measurement terminated")             
            else:
                
                if darksignal and darksignal_spor and (counter % measpack == 0): ds=getDarkSignal()
                    

                manual_measurement_value = float(manual_measurement_value)
                rate = time.time() - time_last_rep
                time_last_rep = time.time()
                #print("Rate:" + str(rate) )
                rate_data.append(rate)

                period = period + rate
                period_data.append(period)





                if darksignal:
                    # if (period >= old_period_ds + 60): # make a new measurement every 60 seconds only and use the old value otherwise to save time
                    #     old_period_ds = period
                    #     if not darksignal_spor and period < 59: ds=getDarkSignal() #only get a first dark signal reading of sporadic dark signal is disabled
                            
                    #     else: ds=getDarkSignal() #get a sporadic reading
                    

                    darksignal_data0.append(ds[0])
                    darksignal_data1.append(ds[1])
                else:
                    darksignal_data0.append(0)
                    darksignal_data1.append(0)

                if mcp3208:
                    #channel 0
                    adw=gpiozero.MCP3208(channel=0)
                    value=adw.value
                    voltage=value*(3.326-0.008)+0.008 #attempt of correcting for minimum voltage
                    mcp_data0.append(voltage)
                    #channel 1
                    adw=gpiozero.MCP3208(channel=1)
                    value=adw.value
                    voltage=value*(3.326-0.008)+0.008 
                    mcp_data1.append(voltage)
                else:
                    mcp_data0.append(0)
                    mcp_data1.append(0)
                    
                if wavePrec:
                    raw_channels = ads.read_sequence(CH_SEQUENCE)
                    voltages     = [i * ads.v_per_digit for i in raw_channels]
                    #channel 5
                    wave_data5.append(voltages[0])
                    #channel 7
                    wave_data7.append(voltages[1])
                else:
                    wave_data5.append(0)
                    wave_data7.append(0)
                    
                if max31865:
                    # Read temperature.
                    tempr = max31865sensor.temperature
                    tempr = tempr + 0.52 # offset correctrion done when using 100 ohm resistor instead of pt100
                    max31865_data.append(tempr)
                else:
                    max31865_data.append(0)

                if ads1115:
                    chan01=get_ads1115()
                    ads15_data0.append(chan01[0])
                    ads15_data1.append(chan01[1])
                else:
                    ads15_data0.append(0)
                    ads15_data1.append(0)

                if manual_measurement:    
                    manual_measurement_data.append(manual_measurement_value)
                else:
                    manual_measurement_data.append(0)

                if zeroF:
                    zerofactor_data.append(zeroFactor)
                else:
                    zerofactor_data.append(0)

                if timestamps:
                    now = datetime.now()
                    date_time = int(now.strftime("%Y%m%d%H%M%S")) # save date and time as integer in the format YYYYMMDDhhmmss                
                    timestamps_data.append(date_time)
                else:
                    timestamps_data.append(0)

                if mcp9808:
                    mcp9808_data.append(mcp98.temperature)
                else:
                    mcp9808_data.append(0)

                if bmp280: 
                    if (period >= old_period_bmp + 60): # make a new measurement every 60 seconds only and use the old value otherwise to save time
                        old_period_bmp = period
                        press_tmp = []
                        for i in range(5):
                            press_tmp.append(bmp.pressure) 
                        press = np.median(press_tmp[:]) # take median from 5 values to have a reliable value to use for the next minute
                    bmp280_data.append(press)
                    #print('pressure: '+ str(press))
                else:
                    bmp280_data.append(0)
                    
                

                if ((counter>= old_counter_spor + measpack) ):
                    if sporadic:
                        old_counter_spor=counter
                        print('just measured - sleping now. Already running '+ str(period) + ' seconds in total.')
                        ledTurnOff()
                        time.sleep(600) # sleep until next measurement
                        if savecont:
                            savenow=True
                        ds=getDarkSignal()
                        
                # if ((period >= old_period_save + 60)or(counter == 0)):    
                #     old_period_save = period
                #     if savecont:
                #         savenow=True
                
                if (((counter+1) % measpack ==0)):
                    t_norm = 273.15 # standard temperature in K
                    p_norm = 1000 # standard pressure in hPa
                    ll=len(period_data)-measpack    
                    tenabs = (np.array(mcp9808_data[ll:])+t_norm)/t_norm* p_norm/np.array(bmp280_data[ll:]) *np.log((np.array(ads15_data1[ll:]) - np.array(darksignal_data1[ll:]))/((np.array(ads15_data0[ll:]) - np.array(darksignal_data0[ll:]))*np.array(zerofactor_data[ll:])))   
                    userread = np.median(tenabs)
                    
                    print('Absorption: ' + str(userread))
                

            counter = counter + 1
        except KeyboardInterrupt: 
            meastmp = False
            interrupt = True
            pass



    ledTurnOff()
    
    print('The following measuring devices were used:')
    print('MCP3208 ADC:' + str(mcp3208))
    print('ADS1256 ADC:' + str(wavePrec))
    print('MAX31865 Temperature Sensor: ' + str(max31865))
    print('ADS1115 ADC: ' + str(ads1115))
    print('MCP9808 Temperature Sensor: ' + str(mcp9808))
    print('BMP280 pressure sensor: ' + str(bmp280))
    print('Sporadic Dark signal measurement: ' + str(darksignal_spor))
    print('The average time for a single measurement loop with the sensors above was ' +str(np.mean(rate_data[1:])) + ' seconds.')
     




    
    

def savedata(savecont, data, name, counter):
    dataT=data.transpose()
    tmpdatafilename="data.csv"
    nameddatafilename='datafolder/'+name +".csv"
    if (not savecont or (counter == 1)): # save file if no continuous saving or first continuous save after first measurement
        if plot: np.savetxt(tmpdatafilename, dataT, delimiter=",")#for immediate use
        np.savetxt(nameddatafilename, dataT, delimiter=",")#for later use
        
    else:
        with open(tmpdatafilename, 'a') as f:
            writer = csv.writer(f)
            for i in dataT:
                writer.writerow(['{:1.18e}'.format(x) for x in i])
        f.close()
        with open(nameddatafilename, 'a') as f:
            writer = csv.writer(f)
            for i in dataT:
                writer.writerow(['{:1.18e}'.format(x) for x in i])


def plotfile(filename, mcpyn, waveyn, max31865yn, ads15yn, manualyn, baroyn, mcp9808yn, bmp280yn):
    Tdata= np.loadtxt(filename, delimiter=",")
    fdata=Tdata.transpose()
    
    
    
    if use_plotcounter: 
            datapoints = len(fdata[0])
            fdata[0] = range(1,datapoints+1)


    fig, ax = plt.subplots()
    mngr = plt.get_current_fig_manager()
    #if (manualyn == True):
    a=False
    if a:
        print('commented out section')
    #    if (mcpyn == True):
    #        plt.plot(fdata[0], fdata[1], label="MCP3208")
    #    if (waveyn == True):
    #        plt.plot(fdata[0], fdata[3], label="ADS1256")
    #    if (max31865yn == True):
    #        plt.plot(fdata[0], fdata[5], label="max31865")
    #    if (ads15yn == True):
    #        plt.plot(fdata[0], fdata[6], label="ADS1115")
    #    if (manualyn == True):
    #        plt.plot(fdata[0], fdata[8], label="manual_measurement")
    #    if (baroyn == True):
    #        plt.plot(fdata[0], fdata[9], label="Barometer")
    #    if (mcp9808yn == True):
    #        plt.plot(fdata[0], fdata[11], label="mcp9808")
    #    if (bmp280yn == True):
    #        plt.plot(fdata[0], fdata[12], label="bmp280")
    else:
        

        if (mcpyn == True):
            plt.plot(fdata[0], fdata[1], label="main MCP3208")
            plt.plot(fdata[0], fdata[2], label="ref. MCP3208")
        # if (waveyn == True):
        #     plt.plot(fdata[0], fdata[3], label="main ADS1256")
        #     plt.plot(fdata[0], fdata[4], label="ref. ADS1256")
        # if (max31865yn == True):
        #     plt.plot(fdata[0], fdata[5], label="max31865")
        if (ads15yn == True):
            plt.plot(fdata[0], fdata[6], label="main ADS1115")
            plt.plot(fdata[0], fdata[7], label="ref. ADS1115")
        if (manualyn == True):
            plt.plot(fdata[0], fdata[8]/100, label="manual measurement")
        # if (baroyn == True):
        #     plt.plot(fdata[0], fdata[9], label="Barometer")
        # if (mcp9808yn == True):
        #     plt.plot(fdata[0], fdata[11], label="mcp9808")
        # if (bmp280yn == True):
        #     plt.plot(fdata[0], fdata[12], label="bmp280")

    plt.title("Sensor Signal")
    if use_plotcounter:
        plt.xlabel("measurement number [ ]")
    else: plt.xlabel("time [s]")
    plt.ylabel("voltage [V]")
    plt.legend()

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
    plt.plot(time_step, pd_ds_main, label="ds main [V]")
    plt.plot(time_step, pd_ds_ref, label="ds ref [V]")
    

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
    

    plt.scatter(manual, np.log((pd_ref - pd_ds_ref)/((pd_main - pd_ds_main)*zerofactor)), 0.5)
  
    plt.title("Absorption vs Concentration")
    # if use_plotcounter:
    #     plt.xlabel("measurement number [ ]")
    # else: plt.xlabel("concentration [µg/ml]")
    plt.xlabel("concentration [µg/ml]")
    plt.ylabel("absorption [AU]")
    # plt.legend()

    plt.show()
if ads1115:
    def zeroing(newzero,ds): # feed with dark factor corrected intensities taken in a pure oxygen measurement
        #with np.loadtxt('zeroing.csv', delimiter = ',') as zeroingdata:
        
        if newzero:    
            print('getting new zerofactor')
            zeroing_factor = []
            main_signal =[]
            ref_signal = []
            # ds=getDarkSignal()
            for i in range(measpack*1):
                chan01=get_ads1115()
                main_korr=chan01[0]-ds[0] #dark signal correctet value of main diode
                ref_korr = chan01[1]-ds[1] #dark signal correctet value of reference diode
                main_signal.append(main_korr)
                ref_signal.append(ref_korr)
                zeroing_factor.append((ref_korr/main_korr))
            #ledTurnOff()
            main_sig = np.mean(main_signal)
            ref_sig = np.mean(ref_signal)
            result= np.median(zeroing_factor) # the added factor manually adjusts the zeroing factor to match the two signals better
            
            now = datetime.now()
            date_time = int(now.strftime("%Y%m%d%H%M%S"))
            np.savetxt('zeroingtmp.csv', [result],  delimiter =',') #for use by code
            with open('zeroing.csv', 'a') as zeroingfile:
                np.savetxt(zeroingfile, [[result,main_sig, ref_sig, date_time]], delimiter=',') # for reference

        else:
            #with np.loadtxt('zeroing.csv', delimiter=',') as zeroingfile:
            zeroingdata=np.loadtxt('zeroingtmp.csv', delimiter =',')
            result=zeroingdata
            
        return result
if ads1115:
    def getDarkSignal():
        print('aquiring dark signal')
        warmup()
        ledTurnOff() #turn LED off for dark signal measurement
        
        intens_main=[]
        intens_ref=[]
        for i in range(measpack):
            chan01=get_ads1115()
            intens_main.append(chan01[0])
            intens_ref.append(chan01[1])
        ledTurnOn() # turn LED back on after dark signal measurement
        
        dark_intens_main= np.mean(intens_main)#edited manually to match main and reference curve
        dark_intens_ref=np.mean(intens_ref)
        warmup()
        return [dark_intens_main, dark_intens_ref]
        

def ledTurnOn():
    GPIO.output(ledpin, GPIO.HIGH)
    if pwm: led_pwm.ChangeDutyCycle(duty)
    #GPIO.output(fanpin, GPIO.HIGH)
    time.sleep(2)
def ledTurnOff():
    GPIO.output(ledpin, GPIO.LOW)
    if pwm: led_pwm.ChangeDutyCycle(100)
    GPIO.output(fanpin, GPIO.LOW)
    time.sleep(2)
def warmup():
    wt=50
    ledTurnOn()
    print('warmup, '+str(wt)+'s to go')
    time.sleep(wt/2)
    print('warmup, '+str(wt/2)+'s to go')
    time.sleep(wt/2)
    print('warmup finished')
    
if ads1115:
    def get_ads1115():
        chan0 = AnalogIn(ads15, ADS.P0)
        chan1 = AnalogIn(ads15, ADS.P1)
        return [chan0.voltage, chan1.voltage]




ledTurnOff()


if measure: 
    
    do_measurement()
if plot: 
    if measure:
        plotfile("data.csv",mcp3208, wavePrec, max31865, ads1115, manual_measurement, False, mcp9808, bmp280)
        plotclean("data.csv",mcp3208, wavePrec, max31865, ads1115, manual_measurement, False, mcp9808, bmp280)
        if manual_measurement: plotabs("data.csv",mcp3208, wavePrec, max31865, ads1115, manual_measurement, False, mcp9808, bmp280)

    else: 
        
        file_path = filedialog.askopenfilename()
        plotfile(file_path,mcp3208, wavePrec, max31865, ads1115, manual_measurement, False, mcp9808, bmp280)
        plotabs(file_path,mcp3208, wavePrec, max31865, ads1115, manual_measurement, False, mcp9808, bmp280)








