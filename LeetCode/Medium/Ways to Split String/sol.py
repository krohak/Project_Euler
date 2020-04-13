# Question 2:
# Given a string S, we can split S into 2 strings: S1 and S2. Return the number of ways S can be split such that 
# the number of unique characters between S1 and S2 are the same.

# Example 1:

# Input: "aaaa"
# Output: 3
# Explanation: we can get a - aaa, aa - aa, aaa- a
# Example 2:

# Input: "bac"
# Output: 0
# Example 3:

# Input: "ababa"
# Output: 2
# Explanation: ab - aba, aba - ba


def split_string(string):

    dict_left = {}
    dict_right = {}

    uniq_left = 0
    uniq_right = 0

    counter = 0

    for i in range(len(string)):
        uniq_right = add_to_dict(string[i], dict_right, uniq_right)
    
    for i in range(len(string)):

        if uniq_left == uniq_right:
            counter+=1

        uniq_left = add_to_dict(string[i], dict_left, uniq_left)
        uniq_right = remove_from_dict(string[i], dict_right, uniq_right)

    return counter


def add_to_dict(char, _dict, uniq):
    
    if not char in _dict:
        _dict[char] = 1
        uniq+=1
    else:
        _dict[char]+=1
    return uniq

def remove_from_dict(char, _dict, uniq):
    if char in _dict:
        _dict[char]-=1

    if _dict[char] == 0:
        uniq-=1
    return uniq

# ways = split_string("aaaa")
ways = split_string("bac")
# ways = split_string("ababa")
print(ways)
