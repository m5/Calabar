from math import log, ceil
import random
from copy import copy

def gen_enum_mutator(S,pf=None,save=True):
    """Generates a function which takes a vector in
    an enumerated space S, and returns a random,
    neighboring vector.

    Parameters
    ----------
    S: A description of the enumerated space.
      ex: S = [[1,2,3],[2,4,5,None],["Anya","Xander,"Giles","Willow"]]

    pf: A function whose return value determines how many dimensions
        to mutate.

        defaults to a geometric distribution:
           pf = lambda: ceil(log(1/random.random(),2))

    save: Boolean argument, decides whether to make a copy of the position
        vector before mutation.

    Returns
    -------
    mutator(p): Takes one position vector in S, returns a neighbor by
        setting pf() dimensions to a random member of S[dimension] """

    ndims = len(S)
    if pf==None:
        pf = lambda: ceil(log(1/random.random(),2))
        
    def mutator(p):
        if save:
          p = copy(p)
          
        for i in range( pf() ):
            dim = random.choice(ndims)
            p[dim] = random.choice(S[dim])
            
        return p

    return mutator
            
            
            
