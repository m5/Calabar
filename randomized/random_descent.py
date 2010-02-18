import random
from copy import copy
from math import log, ceil, e

def random_descent(p_0, f, m, max_idle=50):
    """"Descend randomly, moving to any lower state
    
    Parameters
    ----------
    p_0: A vector in S, the search starts here.
    
    f: A fitness function on S.
        Should accept a vector in S, and return a value to be minimized.
        
    m: A mutator function on S.
        Should accept a vector in S, and return a random neighboring vector
        
    max_idle: Number of iterations to persist without further descent.

    Returns
    -------
    h_min: height of local minumum
    p_final: position of local minimum"""

    since_fell = 0
    p_curr = p_0
    h_min = f(p_curr)
        
    while since_fell < max_idle:
        p_prev = copy(p_curr)
        p_curr = m(p_curr)
        
        # check to see if that made things better
        h_curr = f(p_curr)

        if h_curr < h_min:      # if it is, keep it
            h_min = h_curr
            since_fell = 0
        elif h_curr == h_min:   # if it didn't matter, leave it
            since_fell += 1
        else:                   # if it's worse, throw it out
            p_curr = p_prev
            
    p_final = p_curr
    
    return h_min, p_final


def anneal(p_0, f, m, k=.001, max_idle=50):
    """"Run Simulated annealing over the fitness space S

    Parameters
    ----------
    p_0: A vector in S.
        This will be the starting point for the descent.
        
    f: A fitness function on S.
        Should accept a vector in S, and return a value to be minimized.
        
    m: A mutator function on S.
        Should accept a vector in S, and return a random neighboring vector

    k: Temperature decay constant
        Temp = e**(-k*t)
        Should be close to zero
        
    max_idle: Number of iterations to persist without further descent.

    Returns
    -------
    h_min: height of local minumum
    p_final: position of local minimum"""

    since_fell = 0
    ndims = len(s)
    p_curr = p_curr
    h_curr = f(p_curr)
    Temp = lambda t: e**(-k*t)
    P = lambda p,n,t: e**((p-n)/(h_curr*t))
    time = 0

    while since_fell < max_idle:
        p_new = m(copy(p_curr))
        h_new = f(p_new)

        if h_new < h_curr:
            since_fell = 0
            
        if P(h_curr, h_new, Temp(time)) > random.random():
            p_curr = p_new
            h_curr = h_new

        since_fell += 1
        time += 1
            

    
