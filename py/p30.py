#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n = len(words)
        if n == 0:
            return []
        l1 = len(s)

        l2 = len(words[0])
        if l2 * n > l1:
            return []

        res = []
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        # print word_count
        for i in range(l1 - n*l2 + 1):
            check_count = {}
            # 记录匹配的单词数
            count = 0
            for j in range(n):
                word = s[i+j*l2:i+j*l2+l2]
                if word_count.get(word):
                    # 子串出现 word 的次数多于在words
                    if check_count.get(word, 0) == word_count[word]:
                        break
                    check_count[word] = check_count.get(word, 0) + 1
                    count += 1
                else:
                    break

            # 注意python中， range(j)结束后 j 不会等于n
            # print check_count, j
            # 匹配了n个
            if count == n:
                res.append(i)

        return res

import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().findSubstring("barfoothefoobarman", ["foo","bar"])
    print Solution().findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"])
    # print Solution().findSubstring("foo", ["bar","bar"])
    print Solution().findSubstring("foobarfoobar", ["foo","bar"])
    print Solution().findSubstring("ababaab", ["ab","ba","ba"])
    print Solution().findSubstring("barfoothefoobarman", ["ab","ba","ba"])
    # print Solution().findSubstring("f", ["fb","fb"])
    print 'ok'

