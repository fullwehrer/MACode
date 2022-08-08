import matplotlib.pyplot as plt
import matplotlib.ticker
print(plt.style.available)
plt.style.use(['robert'])

import numpy as np
# x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
# plt.plot(x, np.sin(x))       # Plot the sine of each x point
# plt.show()                   # Display the plot

datei=open('SCIA_O3.DAT', 'r')
# all_lines = datei.readlines()
# num_lines = 0
# for zeile in datei:
#     print(datei.read(7))
#     num_lines = num_lines + 1
# wavelength = np.array(10)
# cross = np.array(10)
# print(range(num_lines))
# for i in range(num_lines):
#     tmp=all_lines[i]
#     print(range(num_lines))
#     #wavelength[zeile] = (tmp[0:13])
#     #cross[zeile] = (tmp[67:80])

zaehler = 0
wavelength = []
cross = []
for zeile in datei:
    zaehler += 1
    tmp_line =(datei.readline()) 
    
    
    wavelength.append(float(tmp_line[0:13]))
    cross.append(float(tmp_line[67:82]))


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
datei.close

x=wavelength
y=cross

###log-abbildung
## for y-axis log ticks
fig, ax=plt.subplots()
ax.plot(x,y, label='logarithmic')
ax.set_yscale("log")
locmaj = matplotlib.ticker.LogLocator(base=10,numticks=12) 
ax.yaxis.set_major_locator(locmaj)
locmin = matplotlib.ticker.LogLocator(base=10.0,subs=(0.2,0.4,0.6,0.8),numticks=12)
ax.yaxis.set_minor_locator(locmin)
ax.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())

##for x-axis more ticks
loc = matplotlib.ticker.MultipleLocator(base=100) # this locator puts ticks at regular intervals of 100
ax.xaxis.set_major_locator(loc)


plt.title("Absorption Spectrum of Ozone")
plt.xlabel("wavelength [nm]")
plt.ylabel("absorption cross section [cm²/molec.]")



ax2=ax.twinx()
next(ax2._get_lines.prop_cycler)
ax2.plot(x,y, label='linear')



lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines1 + lines2, labels1 + labels2)

plt.show()


# ###linear-abbildung
# fig, ax=plt.subplots()
# ax.plot(x,y)
# loc = matplotlib.ticker.MultipleLocator(base=100) # this locator puts ticks at regular intervals of 100
# ax.xaxis.set_major_locator(loc)
# plt.title("Absorption Spectrum of Ozone (linear)")
# plt.xlabel("wavelength [nm]")
# plt.ylabel("absorption cross section [cm²/molec.]")
# plt.show()


fig, ax=plt.subplots()
ax.plot([0.4,2],[0.2,0.8])
#plt.title("Absorption Spectrum of Ozone")
plt.xlabel("concentration [vol\%]")
plt.ylabel("absorbance [AU]")
plt.show()