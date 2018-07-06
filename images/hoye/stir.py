import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.style.use('my.mplstyle')

df=pd.read_csv('signals.csv',names=['sigs','bla'])
sigs=list(df['sigs'])
times=range(len(sigs))
print(len(times))
times=np.array(times)
times=times*5E-3
plt.plot(times,sigs)
plt.xlabel('Time (s)')
plt.ylabel('Signal (A)')
#plt.show()
plt.savefig('stir.png')
