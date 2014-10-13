#!/usr/bin/env python

import unittest
import sum


class TestAnotherSum(unittest.TestCase):
    def test_starting_out(self):
        self.assertEqual(5, 5)

    def test_starting_next(self):
        self.assertEqual(15, 15)

def main():
    unittest.main()

if __name__ == "__main__":
    main()