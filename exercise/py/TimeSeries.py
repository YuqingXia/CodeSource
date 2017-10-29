import numpy as np
#prepare data
def ARModel(phi,r_init,N,sigma):
    """
    Generate time series with AR(p) model: r_t=phi_0+\sum_{i=1}^{p} phi_i*r_{t-i}+a_t
    phi is the weight
    r_init: initial value for r.
    N: number of time series data to be generated init value of r are included. 
    """
    if len(phi)-1!=len(r_init):
        raise exception("Size of coefficient phi must be one less than the size of initial value r_init")
    data=[0]*N
    data[0:len(r_init)]=r_init
    phi=np.asarray(phi)
    r_init=np.asarray(r_init)
    for n in xrange(len(r_init),N):
        data[n]=phi[:0:-1].dot(data[n-len(r_init):n:1])+phi[0]+np.random.normal(loc=0.0,scale=sigma)
    return data

def MAModel(c0,theta,N,sigma):
    """
    Generate time series with MA(q) model: r_t=c_0+a_t-\sum_{i=1}^q \theta_i*a_{t-i}
    c0: is the mean value of r_t
    a_i: are white noise
    theta_i: are coefficient
    N: number of time series data to be generated
    q: order of MA model
    """
    q=len(theta)
    a=np.random.normal(loc=0.0,scale=sigma,size=q+N)
    r=[0]*N
    theta=np.asarray(theta)
    for n in xrange(0,N):
        r[n]=c0+a[n+q]-theta[::-1].dot(a[n:n+q])
    return r
    