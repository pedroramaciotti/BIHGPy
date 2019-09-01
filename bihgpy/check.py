def initial_checks(N,n,K,k):
	"""
	initial_checks(int,int,int,int)

	Check correctness of inputs for hypergeometric distributions

	Parameters
    ----------
    N : int
        Size of the population.
    n : int
        Size of the sample.
    K: int
    	Number of successes in the population.
    k : int
        Number of successes observed in the sample.
    Returns
    -------
    check : int,int,int,int
	"""

	try:
		N=int(N)
		n=int(n)
		K=int(K)
		k=int(k)
	except:
		raise ValueError('Some arguments could not be interpreted as integers.')
	if N<1:
		raise ValueError('Population size N must be a positive number.')
	if n<1:
		raise ValueError('Sample size n must be a positive number.')
	if K<0:
		raise ValueError('Number of successes K in population cannot bet negative.')
	if N<K:
		raise ValueError('Number of successes K in population cannot be greater than population size N.')
	if K<k:
		raise ValueError('Number of observed successes k cannot be greater than successes K in population.')
	if k<0:
		raise ValueError('Number of observed successes k cannot be a negative number.')
	if n>N:
		raise ValueError('Sample size n cannot exceed population size N.')
	if k>n:
		raise ValueError('Number of observed successes k cannot be a greater than the sample size n.')
	return N,n,K,k;