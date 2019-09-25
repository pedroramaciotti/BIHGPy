from scipy.special import comb
from scipy.special import beta as betafunc
import numpy as np

def alpha(mean,var):
	return mean*mean*((1-mean)/var-1/mean);

def beta(mean,var):
	return alpha(mean,var)*(1/mean-1);

def beta_binomial(N,a,b):

	K_dom = np.arange(0,N+1)
	K_img = np.zeros(K_dom.size)

	for i,K in enumerate(K_dom):
		K_img[i] = ( comb(N,K_dom[i]) * betafunc(K_dom[i]+a, N-K_dom[i]+b) )/ betafunc(a,b)

	return K_dom,K_img;
