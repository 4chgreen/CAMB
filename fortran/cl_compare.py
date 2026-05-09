import sys
import numpy as np
import matplotlib.pyplot as plt

lcdm_file = sys.argv[1]
fde_file  = sys.argv[2]

lcdm = np.loadtxt(lcdm_file)
fde  = np.loadtxt(fde_file)

k_lcdm, pk_lcdm = lcdm[:,0], lcdm[:,1]
k_fde,  pk_fde  = fde[:,0],  fde[:,1]

plt.plot(k_lcdm, pk_lcdm/pk_lcdm, label="LCDM")
plt.plot(k_fde, pk_fde/pk_lcdm, label="FDE")

plt.legend()
plt.xlabel("k")
plt.ylabel("ratio")
plt.show()
