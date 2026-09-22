"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

"""
# nums = [1,2,3,4,5,2]

# new = []
# for n in nums:

#     if n in new:

#         print( True)
#         break

#     new.append(n)

# else:
#     print(False)



## using set 


nums = [1,2,3,4,4,2,3,7]

num_set = set(nums)

if len(nums) != len(num_set):

    print(True)

else:

    print(False)