#This is for solutions to certain LeetCode problems along with comments/tips/lessons throughout

import math

#Two Sum
#First Attempt at twoSum, using nested for loops thus it is O(n^2)
def twoSumV1(nums, target):
    #The idea is to stop at each index and check if the rest of indexes add with it to the target.
    #If so, then we stop.
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            tempSum = nums[i] + nums[j]
            if tempSum == target:
                return [i, j]

print(twoSumV1([1, 2, 3, 4], 5))

#This is the second and better attempt at Twosum, here we only go through the list once, thus
#the solution is O(n). We are able to accomplish this using a Dictionary to keep track of the 
#numbers we have seen so far and what index they are found at.
def twoSumV2(nums, target):
    #This is how you create an empty dictionary
    d = {}
    #Here we have an interesting looking for loop, it utilizes enumerate instead of range. This 
    #is usable on lists and it shortens our code by assigning names to the index and value at the
    #index.
    for idx, val in enumerate(nums):
        #At the current value, calculate what's needed for the target and see if we have already
        #seen that number before. If so, then we just return the indexes, otherwise, add to the
        #dictionary and move on.
        needed = target - val
        if needed in d:
            return [d[needed], idx]
        d[val] = idx

print(twoSumV2([1, 2, 3, 4], 5))


#Valid Anagram
