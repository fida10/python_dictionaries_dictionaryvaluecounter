""" 
Practice Question 3: Dictionary Value Counter

Task:

Write a function count_values that takes a dictionary 
and returns a new dictionary where each key is a value 
from the input dictionary and the corresponding value 
is the number of times that key value appeared in the original dictionary.
"""

def count_values(input_dict):
    ans = {}
    
    for value in input_dict.values():
        if value in ans.keys():
            ans[value] = ans[value] + 1
        else:
            ans[value] = 1
    
    return ans
