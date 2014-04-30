import numpy as numpy



import pyfits as py
from cobra_sub import smooth
from read_output import *
from pylab import *

setpars()

import matplotlib.pyplot as plt

plt.rcParams["lines.linewidth"] = 2


x = py.getdata("lci801010_x1dsum.fits")

figure(figsize=(10,5.5))
subplot(111)
plot(x["WAVELENGTH"][0][:-8000],smooth(x["FLUX"][0][:-8000]))
ylabel("Flux (erg s$^{-1}$ cm$^{-3}$ \AA$^{-1}$)" , fontsize=12)
xlabel("Wavelength [\AA]", fontsize=15)

line_text = [r'Ly$\alpha$', r'O\textsc{vi}', r'C\textsc{iv}', r'He\textsc{ii}', r'N\textsc{v}', r'O\textsc{i}', r'Si\textsc{iv}']
line_values = [1215, 1032, 1550, 1640, 1243, 1304, 1402]
doublets = [1239, 1306, 1302, 1393, 1548]

text_loc=6e-13

for i in range(len(line_text)):
	text(line_values[i],text_loc,line_text[i],fontsize=14)


vlines(line_values, 3e-13, 5e-13, linewidth=1.5)
vlines(doublets, 3e-13, 5e-13, linewidth=1.5)
#text(1549,fmin,r'O~\textsc{vi}',fontsize=10)	
#axvline(x=1239,ymin=1e-13,ymax=1e-12,color='black')
#text(1560,fmin,r'C~\textsc{iv}',fontsize=10)
#axvline(x=1032,ymin=1e-13,ymax=1e-12,color='black')



semilogy()
xlim(1190,1700)
ylim(5e-16,1e-12)
savefig("hst.eps")
show()