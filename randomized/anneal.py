import random
from copy import copy
from math import log, ceil, e

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
    p_curr = p_0
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
