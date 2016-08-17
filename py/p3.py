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

        print max_len, max_sub
        return max_len

    # 原理和前面lengthOfLongestSubstring（slide window）的一样，
    # 优化方法： 通过字典优化（原来使用string）
    def optSlideWindow(self, s):
        max_len = 0
        sub_map = {} # {char: position_in_str+1}
        i = 0
        # try to extend the range [i, j]
        for (j, ch) in enumerate(s):
            if sub_map.get(ch):
                i = max(sub_map.get(ch), i)
            max_len = max(max_len, j - i + 1)
            sub_map[ch] = j + 1

        print max_len
        return max_len

    def optWithSmallCharset(self, s):
        i, max_len = 0, 0
        index = [0 for x in range(128)]
        for (j, ch) in enumerate(s):
            i = max(index[ord(ch)], i)
            max_len = max(max_len, j - i + 1)
            index[ord(ch)] = j + 1

        print max_len
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

    Solution().optSlideWindow(t1)
    Solution().optSlideWindow(t2)
    Solution().optSlideWindow(t3)
    Solution().optSlideWindow(t4)

    Solution().optWithSmallCharset(t1)
    Solution().optWithSmallCharset(t2)
    Solution().optWithSmallCharset(t3)
    Solution().optWithSmallCharset(t4)
    print 'ok'
