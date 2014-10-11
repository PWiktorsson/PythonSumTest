#!/usr/bin/env python

import unittest
import sum


class TestSum(unittest.TestCase):
    def test_starting_out(self):
        self.assertEqual(1, 1)

    def test_starting_next(self):
        self.assertEqual(12, 12)

def main():
    unittest.main()

if __name__ == "__main__":
    main()