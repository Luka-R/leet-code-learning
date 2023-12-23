#This is for solutions to certain LeetCode problems along with comments/tips/lessons throughout

import math
from collections import *

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
#Initial attempt at this problem, the general idea is to keep track of the character frequency in each word,
#then if they match, they must be anagrams.
def validAnagramV1(word1, word2):
    #Creating dictionaries to track the frequencies
    d1 = {}
    d2 = {}

    #Populating each dictionary 
    for i in word1:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1
    
    for i in word2:
        if i in d2:
            d2[i] += 1
        else:
            d2[i] = 1
    
    #Are the two dictionaries the same?
    return d1 == d2

#Second attempt, it is virtually the same, just abstracting the dict populating as one function
def validAnagramV2(word1, word2):
    return charFreq(word1) == charFreq(word2)

#This is the function that creates the character frequency dict
def charFreq(word):
    #Here, I am using defaultdict which creates a dictionary that assigns some default value to
    #keys that are not found in it. Thus, it behaves like a dictionary but doesn't raise any KeyErrors.
    #https://www.geeksforgeeks.org/defaultdict-in-python/ for more info on defaultdict
    d = defaultdict(lambda: 0)
    
    for i in word:
        #Due to the default value being 0, there is no need for a conditional, just add one each time
        d[i] += 1
    
    return d

#Final revision, utilizing the Counter from collections that automatically creates a mapping of the characters
#in the string to their frequency. That is what it does in this case, in general, it creates a Hast Table for
#an iterable. https://www.geeksforgeeks.org/python-counter-objects-elements/ for more info on Counter
#https://stackoverflow.com/questions/9884132/what-are-iterator-iterable-and-iteration for info on iterable
def validAnagramV3(word1, word2):
    return Counter(word1) == Counter(word2)

print(validAnagramV3("racecar", "carrace"))
print(validAnagramV3("racecar", "crrace"))
