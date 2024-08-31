from matplotlib import pyplot as plt
from matplotlib import rc
import numpy as np

# set up the plot parameters
fsize = 30

params = {'legend.fontsize': fsize*0.925,          
          'axes.labelsize': fsize,
          'axes.titlesize':fsize*1.25,
          'xtick.labelsize':fsize,
          'ytick.labelsize':fsize }
plt.rcParams.update(params)

rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)

# create the data
t = np.linspace(0,1,1000)
f1 = t*np.exp(-4*t)
f2 = 0.3*np.exp(-5*t)*(0.4*np.cos(np.pi*t)-0.1*np.sin(0.5*np.pi*t))


# build the figure
plt.figure(figsize=(20,10))
plt.plot(t,f1,label="$v_1(t)$")
plt.plot(t,f2,label="$v_2(t)$")

plt.legend()
plt.xlabel("time [ms]")
plt.ylabel("voltage [V]")
plt.title("voltage through resistor")
plt.grid()

plt.savefig("fig_ex.pdf",bbox_inches="tight")
plt.show()
