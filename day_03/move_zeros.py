"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]
"""
#better solution 

nums = [0, 1, 0, 3, 12]

j = 0

for i in range(len(nums)):
    if nums[i] != 0:
        nums[i], nums[j] = nums[j], nums[i]
        j += 1

print(nums)

#method 1
# nums = [0,1,0,3,12]

# zeros = []

# new =[]
# for i in nums:

#     if i == 0:

#         zeros.append(i)

#     else :

#         new.append(i)

# new.extend(zeros)
# print(new)

#method 2
# nums = [0,1,0,3,12]
# zeros =0
# for i in  nums:

#     if i == 0:

#         nums.remove(0)
#         zeros = zeros+1

# for z in range(0,zeros):

#     nums.append(0)

# print(nums)


