import numpy as np


# Write the solution of Question-1 below
M = np.zeros((100, 100))


M += np.diag([9] * 100)         
M += np.diag([8] * 99, k=1)     
M += np.diag([8] * 99, k=-1)    
M += np.diag([7] * 98, k=2)     
M += np.diag([7] * 98, k=-2)    








# Write the solution of Question-2 below
Mc = np.copy(M)
Mc = np.where(Mc == 0, 1e-6, Mc)









# Write the solution of Question-3 below
Mr = np.copy(Mc)
Mr = np.reshape(Mr, (2500, 4), order='F')