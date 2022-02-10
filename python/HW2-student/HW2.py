# HW2
# Name:Jiaxin Luo
# Collaborators:
# Date:1/19/2022

import random

def count_characters(s):
    """Count the number of occurrences of each character in a string. 
    Args:
        s: str, the string in which to count. 
    Returns:
        a dict keyed by characters whose values are the number of occurrences in s
    """
    D = {}
    for i in range(len(s)):
        D[s[i]] = 0

    for i in range(len(s)):
        D[s[i]] += 1
    return D

def count_ngrams(s, n=1):
    """Count the number of occurrences of n-grams in a string. 
    Args:
        s: str.
        n: positive int. should have default value 1.
    Returns:
        a dict keyed by n-grams whose values are the number of occurrences in s
    """
    D = {}
    
    for i in range(len(s)-n+1):
        D[s[i:i+n]] = 0

    for i in range(len(s)-n+1):
        D[s[i:i+n]] += 1

    return D

def markov_text(s, n, length = 100, seed = "Emma Woodhouse"):
    """Generate fake text according to an n-th order Markov model, with data from a user-supplied corpus. 
    Args:
        s: str. the text from which to learn grams.
        n: positive int. the order of the Markov model. 
        length: positive int. the number of synthetic characters to generate. should have a default value. 
        seed: str. should have a default value.
    Returns:
        The output string fake_text. fake_text starts with the seed. 
        length of fake_text = length of seed + argument 'length'
    """
    seed_length = len(seed)
    # All n+1-grams in the text
    D = count_ngrams(s, n+1)
    while length + seed_length - len(seed)>0:
        # The n most recent character in generated text
        recent_char = seed[-n::1]       
        # A list of n+1-grams whose first n characters match
        matched_str = [key for key in D.keys() if recent_char == key[:n]]
        # Weighted the grams according to its number of occurrences
        weights = []
        for w in matched_str:
            weights.append(D.get(w))
        # Pick a random one of these n+1-grams
        choice = random.choices(matched_str, weights)
        choice_char = choice[0]
        # The final character of this n+1-gram is the next letter added to the seed
        seed = seed + choice_char[-1:]
    
    fake_text = seed
    
    return fake_text
    
    