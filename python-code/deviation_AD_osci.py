import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np
plt.style.use(['robert'])
# x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
# plt.plot(x, np.sin(x))       # Plot the sine of each x point
# plt.show()                   # Display the plot



# plt.plot(wavelength, cross)
# plt.title("Absorption Spectrum of Ozone (linear)")
# plt.xlabel("wavelength [nm]")
# plt.ylabel("absorption cross section [cm²/molec.]")
# plt.show()
# plt.semilogy(wavelength, cross)
# plt.title("Absorption Spectrum of Ozone (logarithmic)")
# plt.xlabel("wavelength [nm]")
# plt.ylabel("absorption cross section [cm²/molec.]")
# plt.show()
# plt.plot(wavelength, cross)
# plt.title("Absorption Spectrum of Ozone")
# plt.xlabel("wavelength [nm]")
# plt.ylabel("absorption cross section [cm²/molec.]")
# plt.xlim([275, 280])
# plt.show()

# x=[1,2,3]
x=['0.0037','0.752', '1.494','2.250','3.335']
osci=[0,0,0, 0,0]
mcp=[0.0045-0.0037,0.743-0.752,1.480-1.494,2.227-2.250,3.297-3.335]
wave=[0.00382-0.0037,0.7445-0.752, 1.484-1.494,2.2325-2.250,3.3037-3.335]
ads=[0.00401-0.0037,0.743-0.752,1.481-1.494,2.228-2.250,3.2972-3.335]


# mcp=[0.0045*1.01-0.0037,0.743*1.01-0.752,1.480*1.01-1.494,2.227*1.01-2.250,3.297*1.01-3.335]
# wave=[0.00382*1.01-0.0037,0.7445*1.01-0.752, 1.484*1.01-1.494,2.2325*1.01-2.250,3.3037*1.01-3.335]
# ads=[0.00401*1.01-0.0037,0.743*1.01-0.752,1.481*1.01-1.494,2.228*1.01-2.250,3.2972*1.01-3.335]


###linear-abbildung
fig, ax=plt.subplots()
# ax.plot(x,osci)
ax.plot(x,mcp, label='MCP3208' )
ax.plot(x,wave, label= "ADS1256")
ax.plot(x,ads, label ='ADS1115')
# ,mcp, wave, ads
loc = matplotlib.ticker.MultipleLocator(base=1) # this locator puts ticks at regular intervals of 100
ax.xaxis.set_major_locator(loc)
plt.title("Deviation of ADCs from Oscilloscope Measurement")
plt.xlabel("oscilloscope measurement [V]")
plt.ylabel("deviation [V]")
plt.legend()
plt.show()