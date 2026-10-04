"""
You are given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]

Output: [0,0,1,1,2,2]

Explanation:

The array has two 0s, two 1s, and two 2s. Sorting them in-place places all 0s first, then all 1s, then all 2s.

Example 2:

Input: nums = [2,0,1]

Output: [0,1,2]

Explanation:

The array has one each of 0, 1, and 2, arranged in-place in the order 0, 1, 2.

Constraints:

    n == nums.length
    1 <= n <= 300
    nums[i] is either 0, 1, or 2.

 
"""

nums = [2,0,2,1,1,0]

count_0 = nums.count(0)
count_1 = nums.count(1)
count_2 = nums.count(2)

index = 0

for i in range(count_0):
    nums[index] = 0
    index = index + 1

for i in range(count_1):
    nums[index] = 1
    index = index + 1

for i in range(count_2):
    nums[index] = 2
    index = index + 1

print(nums)

    
    
# for i in range(0,count_0):

#     nums.remove(0)

# for i in range(0,count_1):

#     nums.remove(1)

# for i in range(0,count_2):

#     nums.remove(2)


# while (count_0!=0):

#     nums.append(0)
#     count_0=count_0-1


# while (count_1!=0):

#     nums.append(1)
#     count_1=count_1-1

# while (count_2!=0):

#     nums.append(2)
#     count_2=count_2-1

# print(nums)


