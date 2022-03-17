# 1.1
# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?
# Hints: #44, #117, #732

from operator import truediv


testcase1 = "abc"
testcase2 = "aabb"
testcase3 = "abcdefghijklmnopqrstuvwxyz"
# testcase4 = "abc123"

test = [testcase1, testcase2, testcase3]

# With additional data structure

# can use a hashmap to count the number of occurences of each character O(n)
# Lookup in the hashmap if the value associated with each character is > 1


class Solution:

    def __init__(self, s):
        self.s = s
        self.hashMap = {}

    def isUnique(self):
        
        for char in self.s:
            self.hashMap[char] = 1 + self.hashMap.get(char, 0)

        for v in self.hashMap.values():
            if v > 1:
                return False
        return True


for case in test:
    c = Solution(case)
    print(c.isUnique())

print("_______________________________________________________________________")
print(" ")
# Without addtional data structure
# WE have to use bit manipulation to achieve this

import math

class Solution1:

    def __init__(self, s):
        self.s = s
        self.checker = 0

    def isUnique(self):
        
        for char in range(len(self.s)):
            bitAtIdx = ord(self.s[char]) - ord('a')

            # If that bit is already set in the checker
            # Return False

            if bitAtIdx > 0:
                if (self.checker and (1 << bitAtIdx)) > 0:
                    return False

                # Else we can update the checker
                self.checker = self.checker | (1 << bitAtIdx)
        return True

for case in test:
    c = Solution1(case)
    print(c.isUnique())