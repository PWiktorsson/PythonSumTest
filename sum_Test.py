#!/usr/bin/env python

import unittest
import sum


class TestSum(unittest.TestCase):
    def test_starting_out(self):
        self.assertEqual(sum.sum_func(1), 1)

    def test_starting_next(self):
        self.assertEqual(sum.sum_func(12), 3)

    def test_starting_yet_next(self):
        self.assertEqual(sum.sum_func(98237924), 44)

def main():
    unittest.main()

if __name__ == "__main__":
    main()