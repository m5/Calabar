from collections import defaultdict

def gen_count_distance(goals,f_weight):
    """Generate a function to count appearances of
       an item in an enumerated position vector

       Parameters
       ----------
       goals: a dictionary containing the target
           number of appearances of each key
              
       f_weight: a function which takes the differnce
           between the actual and target counts, and
           returns a fitness score.

       Returns
       -------
       count_distance(p): a function which takes
           a position vector, and returns a fitness
           score."""
    
    def count_distance(p):
        count = defaultdict(lambda:0)
        score = 0
        for item in p:
            count[item] += 1
        for item, goal in goals.items():
            score += f_weight(count[item] - goal)
        return score
    return count_distance

def gen_dot_weight(goals):
    """Generates a function to count the appearances of
    an item in an enumerated position vector, weighted
    on the dimension in which it occurs.

    Parameters
    ---------
    goals: a dictionary containing a list of weights
        for each key. The list should have an entry for
        each dimension.

    Returns
    -------
    dot_weight(p): a function which takes a position
        vector, and returns a fitness score."""
    
    def dot_weight(p):
        for i, item in enumerate(p):
            score += goals[item][i]
    return dot_weight
            
            
