# -*- coding: utf-8 -*-

from .context import pyworkload

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        assert True
        # self.assertIsNone(pywork.hmm())


if __name__ == '__main__':
    unittest.main()
