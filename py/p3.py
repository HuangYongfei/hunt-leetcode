#!/usr/bin/env python
# -*- coding: utf8 -*-

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub = ''
        max_len = 0
        max_sub = ''
        for c in s:
            if c in sub:
                index = sub.rfind(c)
                sub = sub[index+1:] + c
            else:
                sub += c
                (max_len, max_sub) = (max_len, max_sub) if max_len > len(sub) else (len(sub), sub)

        # print max_len, max_sub
        return max_len


if __name__ == '__main__':
    t1 = "abcabcbb"
    t2 = "bbbbb"
    t3 = "pwwkew"
    t4 = "bpfbhmipx"
    Solution().lengthOfLongestSubstring(t1)
    Solution().lengthOfLongestSubstring(t2)
    Solution().lengthOfLongestSubstring(t3)
    Solution().lengthOfLongestSubstring(t4)
    print 'ok'
