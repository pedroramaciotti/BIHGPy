import numpy as np
from scipy.special import comb
from scipy.special import beta
import matplotlib.pyplot as plt
from scipy.special import gamma

import bihgpy

# parameters of the prior distribution (beta-binomial)
a=1
b=1

# parameters of the hyper-geometric distribution an outcome of the experiment
N=50
n=20
k=2

# computing the bayesian inference

K_dom,K_img = bihgpy.posterior_density(N,n,k,a,b)

# Confidence interval
alpha=0.05
ub = bihgpy.upper(N,n,k,alpha/2,a,b)
lb = bihgpy.lower(N,n,k,alpha/2,a,b)
mean = bihgpy.posterior_mean(N,n,k,a=1,b=1)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(K_dom/N,K_img)
ax.axvline(lb/N,color='r')
ax.axvline(ub/N,color='r')
plt.show()


