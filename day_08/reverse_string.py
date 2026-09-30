"""
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

 
"""
# using string slicing
# def reverse(string):

#     string = string[::-1]

#     return string

# print(reverse(["h","e","l","l","o"]))

#using 2 pointer swap

def reverse(string):

    l=0
    r=len(string)-1
    
    while(r>=l):

        string[l],string[r]=string[r],string[l]
        l+=1
        r-=1

    return string

print(reverse(["H","a","n","n","a","h"]))