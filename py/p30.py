#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        words_len = len(words)
        if words_len == 0:
            return []
        s_len = len(s)

        word_len = len(words[0])
        if word_len * words_len > s_len:
            return []

        res = []
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        # print word_count
        for i in range(s_len - words_len*word_len + 1):
            # 记录
            check_count = {}
            # 记录匹配word_count中的单词个数
            count = 0
            for j in range(words_len):
                # 从位置i开始，按找出每个word_len的子串
                # 如果该子串不在word_count，退出
                # 如果该子串中出现某个word的次数多于word_count中出现的次数，退出
                word = s[i+j*word_len:i+j*word_len+word_len]
                if word_count.get(word):
                    # 子串出现 word 的次数多于在words
                    if check_count.get(word, 0) == word_count[word]:
                        break
                    check_count[word] = check_count.get(word, 0) + 1
                    count += 1
                else:
                    break

            # 注意python中， range(j)结束后 j 不会等于words_len
            # print check_count, j
            # 匹配了words_len个
            if count == words_len:
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

