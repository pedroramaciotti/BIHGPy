import numpy as np
from scipy.special import comb
from scipy.special import beta
from scipy.special import gamma

from .check import initial_checks

def posterior_point(N,n,K,k,a=1,b=1):
	N,n,K,k = initial_checks(N,n,K,k)
	return comb(a+K,a+k)*comb(b+N-K,b+n-k)/comb(a+b+N+1,a+b+n+1);# Peskun
	# return comb(N-n,K-k)*gamma(a+K+1)*gamma(b+N-K+1)*gamma(a+b+n+2)/(gamma(a+k+1)*gamma(b+n-k+1)*gamma(a+b+N+2));# Developped Peskun

def posterior_density(N,n,k,a=1,b=1):
	"""
	posterior(int,int,int)

    Return the posterior probability distribution the parameter
    of a hyper-geometric distribution given observation.

    Parameters
    ----------
    N : int
        Size of the population.
    n : int
        Size of the sample.
    k : int
        Number of successes observed in the sample.
    a,b : double
    	Parameters of the prior beta-binomial distribution (a=b=1 => uniform)
    Returns
    -------
    K_dom : np.array(int)
        Domain of the probability density function.
    K_img : np.array(double)
    	Image of the probability density function.
	"""
	# performing initial checks
	N,n,K,k = initial_checks(N,n,N,k)

	# Computing the domain of the probability density function
	K_dom = np.arange(k,N-(n-k)+1)
	# Computing the image of the probability density function
	K_img = np.array([posterior_point(N,n,K,k,a,b) for K in K_dom])
	# K_img = K_img/K_img.sum()

	return K_dom,K_img;

def posterior_mean(N,n,k,a=1,b=1):
	
	# performing initial checks
	N,n,K,k = initial_checks(N,n,N,k)

	# Computing the domain of the probability density function
	K_dom = np.arange(k,N-(n-k)+1)
	# Computing the image of the probability density function
	K_img = np.array([posterior_point(N,n,K,k,a,b) for K in K_dom])

	return np.multiply(K_dom,K_img).sum();
