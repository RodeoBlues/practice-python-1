"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

    Given "abcabcbb", the answer is "abc", which the length is 3.

    Given "bbbbb", the answer is "b", with the length of 1.

    Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        max_length = count = 0
        checker = dict()
        for i, c in enumerate(s):
            if c in checker:
                prev = checker[c]
                count = min(count + 1, i - prev)
                checker[c] = i
            else:
                count += 1
                checker[c] = i
            max_length = max(max_length, count)

        return max_length
