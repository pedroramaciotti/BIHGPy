def alpha(mean,var):
	return mean*mean*((1-mean)/var-1/mean);

def beta(mean,var):
	return alpha(mean,var)*(1/mean-1);