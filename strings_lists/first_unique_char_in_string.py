'''
Type: strings, hash table
Source: Leetcode (Easy)
Prompt: Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
You may assume the string contain only lowercase letters.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Paramters:
- s, string

Returns: int, index
'''


def first_unique_char(s):
	''' Uses hashmap. Can also use Python standard library collections.Counter to create hash table.
	t: O(n)
	s: O(n)
	'''
    counter = {}
    for c in s:
        counter[c] = counter.get(c, 0) + 1
    for k, v in counter.items():
        if v == 1:
            return s.index(k)
    return -1