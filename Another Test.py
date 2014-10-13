#!/usr/bin/env python

import unittest
import sum


class TestAnotherSum(unittest.TestCase):
    def test_starting_out(self):
        self.assertEqual(sum.sum_func(5), 5)

    def test_starting_next(self):
        self.assertEqual(sum.sum_func(15), 6)

def main():
    unittest.main()

if __name__ == "__main__":
    main()