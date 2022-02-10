import random

# Problem 1

def print_s(s):
    ''' Prints a given string.
    Args:
        s: A string.
    Returns:
        None
    '''
    print(s)

def print_s_lines(s):
    for line in s.split(": "):
        print(line)

def print_s_parts(s):
    for chunk in s.split():
        if chunk[-4:] == "ired":
            print(chunk)

def print_s_some(s):
    for line in s.split("\n"):
        if len(line) < 70:
            print(line)

def print_s_change(s):
    t = s.replace("math", "data science")
    t = t.replace("long division", "machine learning")
    print(t)


# Problem 2 

def make_count_dictionary(L):
    ''' Counts how many times each element in a list appears.
    Args:
        L: A list. Elements may be of different types.
    Returns:
        A dict of counts. A key is a unique element of L,
        and its corresponding value is how many times
        that element is in L.
    Example:
        L = ["a", "a", "b", "c"]
        returns {"a" : 2, "b" : 1, "c" : 1}
    '''
    D = {}

    for i in L:
        D[i] = 0

    for i in L:
        D[i] += 1
    
    return D


# Problem 3

def gimme_an_odd_number():
    ''' Waits for an odd number.
    Repeatedly prompts user with 'Please enter an integer.'  
    until given an odd number.
    Assume the user will only type in non-negative integers.

    Args:
        None
    Returns:
        At termination, prints and returns a list of 
        all numbers that the user has given so far.
    '''
    L = []
    while True:
        s = input("Please enter an integer.")
        i = int(s)
        L.append(i)
        if i % 2 == 1:
            break
    print(L)
    return L


# Problem 4

def get_triangular_numbers(k):
    ''' Finds the first k triangular numbers. 
    Args:
        k: A positive integer.  
    Returns:
        A list of the first k triangular numbers,
        in order. Each element is an integer.
    Example:
        k = 6
        returns [1, 3, 6, 10, 15, 21]
    '''
    L = [sum(range(i+1)) for i in range(1, k+1)]
    return L

def get_consonants(s):
    ''' Finds only the consonant letters in a string.
    Args:
        s: A string that contains only lowercase alphabet letters,
        vowels, spaces, commas, and periods.
    Returns:
        A list of strings. Each element
            - is one character long,
            - is not a vowel, space, comma, nor period,
            - is in s, and
            - may appear multiple times.
        The elements appear in the same order as the letters in s.
    Example:
        s = "make it so, number one."
        returns ["m", "k", "t", "s", "n", "m", "b", "r", "n"]    
    '''
    L = [l for l in s if l not in ["e", "i", "o", "u", "a", " ", ",", "."]] 
    return L

def get_list_of_powers(X, k):
    ''' Raise elements of a list to its powers.
    Args:
        X: A list of non-negative integers.
        k: A non-negative integer.
    Returns:
        A list of lists. The ith element is a list
        of the powers of X[i] from 0 to (and including) k, 
        in increasing order.
    Example:
        X = [5,6,7], k = 2
        returns [[1, 5, 25], [1, 6, 36], [1, 7, 49]]
    '''
    L = [[l**j for j in range(k+1)] for l in X]
    return L

def get_list_of_even_powers(X, k):
    ''' Raise elements of a list to its even powers.
    Args:
        X: A list of non-negative integers.
        k: A non-negative integer. May or may not be even.
    Returns:
        A list of lists. The ith element is a list
        of the EVEN powers of X[i] from 0 to (and including) k, 
        in increasing order.
    Example:
        X = [5,6,7], k = 2
        returns [[1, 25], [1, 36], [1, 49]]
    '''
    L = [[l**j for j in range(k+1) if j % 2 == 0] for l in X]
    return L


# Problem 5

def random_walk(upper_bound, lower_bound):
    ''' Simulates a simple, unbiased random walk.
    Terminates when the walk's position reaches
    the upper bound or lower bound. Initial position is 0.

    Args:
        ub: An integer. Upper bound of the walk.
        lb: An integer. Lower bound of the walk.
        You can assume ub >= lb.
    Returns:
        pos: An integer. The walk's final position.
        positions: A list of integers. A log of the walk's positions, 
        including initial but excluding final position.
        steps: A list of -1s and 1s. A log of the coin flips.
    '''
    steps = []      # history of all step directions
    positions = []  # history of all positions
    pos = 0           # current position
    positions.append(pos)
    # until we trigger a break statement
    while True:
        # flip a coin to take step
        x = random.choice([-1, 1])
        # add result to current position p
        pos += x
        # append to step history
        steps.append(x)

        # check whether we have reached one of the bounds
        # break if so
        if pos >= upper_bound:
            print("Upper bound reached.")
            break
        elif pos <= lower_bound:
            print("Lower bound reached.")
            break
        
        # append to position history
        positions.append(pos)
    
    return pos, positions, steps