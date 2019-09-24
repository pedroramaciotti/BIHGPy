import numpy as np
from scipy.special import comb
from scipy.special import beta
import matplotlib.pyplot as plt
from scipy.special import gamma

import time


import bihgpy

# parameters of the prior distribution (beta-binomial)
a=1
b=1

# parameters of the hyper-geometric distribution an outcome of the experiment
N=50000
n=2000
k=0


# computing the bayesian inference
K_dom,K_img = bihgpy.K_posterior_distribution(N,n,k,a,b)

# Confidence interval
alpha=0.01
ub  = bihgpy.upper(N,n,k,alpha/2,a,b)
lb  = bihgpy.lower(N,n,k,alpha/2,a,b)
ub2 = bihgpy.upper(N,n,k,alpha,a,b)
mean = bihgpy.K_posterior_mean(N,n,k,a=1,b=1)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(K_dom/N,K_img)
#ax.axvline(lb/N,color='r')
ax.axvline(ub2/N,color='r')
plt.show()

#alphas = [0.001,0.01,0.05]
#fraction_ok = 0.05
#
#N_min = 10
#n_min = 2
#N_max = 1000
#Ns = np.arange(N_min,N_max+1)
#
#results = {}
#
#for alpha in alphas:
#    results[alpha] = np.zeros(Ns.size)
#    for i,N in enumerate(Ns):
##        print('******* %d ********'%N)
#        for n in np.arange(n_min,N_max+1):
##            print('n = %d, ub = %d, fraction = %.3f'%(n,bihgpy.upper(N,n,0,alpha,a,b),bihgpy.upper(N,n,0,alpha,a,b)/N))
#            if bihgpy.upper(N,n,0,alpha,a,b)/N<=fraction_ok:
#                break
#        results[alpha][i]=n
#        
#                
#        
#fig = plt.figure()
#ax = fig.add_subplot(1,1,1)
#for alpha in alphas:
#    ax.plot(Ns,results[alpha])
#ax.legend(alphas)
#plt.show()




