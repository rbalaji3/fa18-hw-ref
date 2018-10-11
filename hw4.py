"""
CS 196 FA18 HW4
Prepared by Andrew, Emilio, and Prithvi

You might find certain default Python packages immensely helpful.
"""

# Good luck!

"""
most_common_char

Given an input string s, return the most common character in s.
"""
def most_common_char(s):
	if s == None:
		return None
	maximum = 0
    desiredChar = ''
	for c in s:
		if s.count(c) > maximum:
			maximum = s.count(c)
            desiredChar = c
	return desiredChar


"""
alphabet_finder

Given an input string s, return the shortest prefix of s (i.e. some s' = s[0:i] for some 0 < i <= n)
that contains all the letters of the alphabet.
If there is no such prefix, return None.
Your function should recognize letters in both cases, i.e. "qwertyuiopASDFGHJKLzxcvbnm" is a valid alphabet.

Example 1:
	Argument:
		"qwertyuiopASDFGHJKLzxcvbnm insensitive paella"
	Return:
		"qwertyuiopASDFGHJKLzxcvbnm"

Example 2:
	Argument:
		"aardvarks are cool!"
	Return:
		None
"""

def alphabet_finder(s):
	if len(s) == 0 or len(s) < 26 or s == None:
		return None
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	loweredS = s.lower()
	last = 0
	for i in alphabet:
		try:
			if loweredS.index(i) > last:
				last = loweredS.index(i)
		except:
			return None
	return s[0:last + 1]


"""
longest_unique_subarray

Given an input list of integers arr,
return a list with two values [a,b] such that arr[a:a+b] is the longest unique subarray.
That is to say, all the elements of arr[a:a+b] must be unique,
and b must be the largest value possible for the array.
If multiple such subarrays exist (i.e. same b, different a), use the lowest value of a.

Example:
	Argument:
		[1, 2, 3, 1, 4, 5, 6]
	Return:
		[1, 6]
"""
def longest_unique_subarray(arr):
	pass


"""
string_my_one_true_love

A former(?) CA for this course really like[d] strings that have the same occurrences of letters.
This means the staff member likes "aabbcc", "ccddee", "abcabcabc", etcetera.

But the person who wrote all of your homework sets wants to trick the staff with really long strings,
that either could be the type of string that the staff member likes,
or a string that the CA would like if you remove exactly one character from the string.

Return True if it's a string that the homework creator made, and False otherwise.
Don't treat any characters specially, i.e. 'a' and 'A' are different characters.

Ungraded food for thought:
Ideally, your method should also work on integer arrays without any modification.

Example 1:
	Argument:
		"abcbabcdcdda"
		There are 3 a's, 3 b's, 3 c's, and 3 d's. That means it is a very likable string!
	Return:
		True

Example 2:
	Argument:
		"aaabbbcccddde"
		There are 3 a's, 3 b's, 3 c's, and 3 d's. We have 1 e, which we can remove.
	Return:
		True

Example 3:
	Argument:
		"aaabbbcccdddeeffgg"
		This string is similar to the other ones, except with 2 e's, f's and g's at the end.
		To make this string likable, we need to remove the 2 e's, f's, and g's or we can remove
		one a, b, c, and d. However all of these require more than one removal, so it becomes invalid.
	Return:
		False
"""
def string_my_one_true_love(s):
	pass


"""
alive_people

You are given a 2-dimensional list data. Each element in data is a list [birth_year, age_of_death].
Assume that the person was alive in the year (birth_year + age_of_death).
Given that data, return the year where the most people represented in the list were alive.
If there are multiple such years, return the earliest year.

Example:
	Argument:
		[[1920, 80], [1940, 22], [1961, 10]]
	Return:
		1961
"""
def alive_people(data):
    import numpy as np
    data = np.array(data)
    startYears = data[:,0]
    ages = data[:,1]
    endYears = []
    for i in range(len(startYears)):
        endYears.append(startYears[i] + ages[i])
    earliest = min(startYears)
    latest = max(endYears)
    possibleYears = {}
    for i in range(latest - earliest + 1):
        #print(i + earliest)
        x = {i + earliest: 0}
        possibleYears.update(x)
    for i in range(len(startYears)):
        start = startYears[i]
        end = endYears[i]
        for j in range(start, end):
            possibleYears[j] += 1
    maximumKey = earliest
    for key in possibleYears:
        if possibleYears[key] > possibleYears[maximumKey]:
            maximumKey = key
    return maximumKey
	
	

#loop through each element of the array
# when at each element, stop and parse through the rest of the array
# when parsing through the rest, stop at each element and parse through the rest of the elements 
# 3 * nested loop 
# for each one, if the 3 elemens work, put them into an array and save it 
 
"""
three_sum

Given an input list of integers arr, and a constant target t,
is there a triplet of distinct elements [a,b,c] so that a + b + c = t?

Return a 2-dimensional list of all the unique triplets as defined above.
Each inner list should be a triplet as we defined above.
We don't care about the order of triplets, nor the order of elements in each triplet.

Example:
	Arguments:
		[-1, 0, 1, 2, -1, -4], 0
	Return:
		[
			[-1, 0, 1],
			[-1, -1, 2]
		]
"""

def three_sum(arr, t):
    arrF = []
    if arr == None:
        return None
    for x in range(len(arr)):
        first = arr[x]
        for y in range(x + 1, len(arr)):
            second = arr[y]
            for z in range(y + 1, len(arr)):
                third = arr[z]
                if first + second + third == t:
                    arrF.append([first, second, third])
    for key in arrF:
        if(set(key) == set(arrF[0])):
            arrF.pop(arrF.index(key))
    return arrF


"""
happy_numbers

Given an input integer n > 0, return the number of happy integers between 1 and n, bounds inclusive.
https://en.wikipedia.org/wiki/Happy_number

Example 1:
	Argument:
		8
		The happy numbers between 1 and 8 are 1 and 7 (7 -> 49 -> 97 -> 130 -> 10 -> 1)
	Return:
		2468 // 1234 (i.e., 2)
Example 2:
	Argument:
		15
	Return:
		4294967296 ** (1 / 16) (i.e., 4)
"""
def happy_numbers(n):
	pass


"""
zero_sum_subarray

Given an input list of integers arr,
return a list with two values [a,b] such that sum(arr[a:a+b]) == 0.
In plain English, give us the location of a subarray of arr that starts at index a
and continues for b elements, so that the sum of the subarray you indicated is zero.
If multiple such subarrays exist, use the lowest valid a, and then lowest valid b,
in that order of priority.
If no such subarray exists, return None.

Ungraded food for thought:
Think about how to generalize your solution to any arbitrary target sum.

Example 1:
	Argument:
		[0, 1, 2, 3, 4, 5]
		Clearly, the first element by itself forms a subarray with sum == 0.
	Return:
		[0, 1]

Example 2:
	Argument:
		[10, 20, -20, 3, 21, 2, -6]
		In this case, arr[1:3] = [20, -20], so there is a zero sum subarray.
	Return:
		[1, 2]
"""
# iterate through all the elements in the array
# at each one stop, and selectivly parse the rest independently based on index 
def zero_sum_subarray(arr):
    arrFinal = []
    for i in range(len(arr)):
        outerIndex = arr[i]
        counter = i + 1
        for j in range(i + 1, len(arr)):
            innerIndex = arr[j]
            if sum(arr[i:j]) == 0:
                arrFinal.append([i,j - i])
    return arrFinal
