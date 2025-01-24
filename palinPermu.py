from itertools import permutations

def is_palindrome(s):
    # Check if a string is a palindrome
    return s == s[::-1]

def string_permutations(s):
    # Generate all permutations using itertools.permutations
    perms = set(permutations(s))  # Using set to avoid duplicates
    return [''.join(p) for p in perms]  

def find_palindromes(s):
    perms = string_permutations(s)
    palindromes = [word for word in perms if is_palindrome(word)]
    return palindromes

    
    
