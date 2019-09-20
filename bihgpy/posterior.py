import numpy as np
from scipy.special import comb
from scipy.special import beta
from scipy.special import gamma
import tqdm

from .check import initial_checks

binom_coef_exact = True

def K_posterior_value(N,n,K,k,a=1,b=1):
    return comb(a+K,a+k,exact=binom_coef_exact)*comb(b+N-K,b+n-k,exact=binom_coef_exact)/comb(a+b+N+1,a+b+n+1,exact=binom_coef_exact);
    
def K_posterior_distribution(N,n,k,a=1,b=1,omit_tail=True):
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
    omit_tail : bool
        If true, check regularly if PMF sums to 1 with tolerance and stops 
        prematurely.
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
    K_img = np.zeros(K_dom.size)
    for i,K in enumerate(K_dom):
        K_img[i] = K_posterior_value(N,n,K,k,a,b)
        # for very large K we want to check if we can stop
        if omit_tail:
            if i%10000:
                if np.abs(K_img.sum()-1)<1e-6:
                    break
    # K_img = np.array([posterior_point(N,n,K,k,a,b) for K in K_dom])
    return K_dom,K_img;

def K_posterior_mean(N,n,k,a=1,b=1,omit_tail=True):
    
    # performing initial checks
    N,n,K,k = initial_checks(N,n,N,k)

    # Computing the domain of the probability density function
    K_dom,K_img = K_posterior_distribution(N,n,k,a,b,omit_tail)

    return np.multiply(K_dom,K_img).sum();
