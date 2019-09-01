import numpy as np
from scipy.special import comb
from scipy.special import beta
from scipy.special import gamma

from .check import initial_checks
from .posterior import posterior_density

def upper(N,n,k,alpha,a=1,b=1):

	# initial check
	N,n,_,k = initial_checks(N,n,N,k)

	if k==n:
		return 1.0;

	# Computing posterior distribution
	K_dom,K_img = posterior_density(N,n,k,a,b)

	# naive bound
	return K_dom[np.argmax(K_img.cumsum() > (1.0-alpha))];

def lower(N,n,k,alpha,a=1,b=1):

	# initial check
	N,n,_,k = initial_checks(N,n,N,k)

	if k==0:
		return 0.0;

	# Computing posterior distribution
	K_dom,K_img = posterior_density(N,n,k,a,b)

	# naive bound
	return K_dom[np.argmax(K_img.cumsum() > (alpha))];