#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 69. Sqrt(x)
# Implement int sqrt(int x).

# 总结：
#



import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print 'ok'

