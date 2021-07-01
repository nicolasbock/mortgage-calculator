import unittest
try:
    # python 3.4+ should use builtin unittest.mock not mock package
    from unittest.mock import patch
except ImportError:
    from mock import patch

import sys
from mortgage_calculator import parse_commandline


class TestParser(unittest.TestCase):

    def test_principal(self):
        with patch.object(sys, 'argv', ['program', '--principal', '100000']):
            result = parse_commandline.parse_commandline()
        self.assertEqual(100000, result.principal)

    def test_term_1(self):
        with patch.object(sys, 'argv', ['program', '--term', '15y']):
            result = parse_commandline.parse_commandline()
        self.assertEqual(15 * 12, result.term)

    def test_term_2(self):
        with patch.object(sys, 'argv', ['program', '--term', '15years']):
            result = parse_commandline.parse_commandline()
        self.assertEqual(15 * 12, result.term)

    def test_term_3(self):
        with patch.object(sys, 'argv', ['program', '--term', '15m']):
            result = parse_commandline.parse_commandline()
        self.assertEqual(15, result.term)

    def test_term_4(self):
        with patch.object(sys, 'argv', ['program', '--term', '15months']):
            result = parse_commandline.parse_commandline()
        self.assertEqual(15, result.term)

    def test_term_5(self):
        with patch.object(sys, 'argv', ['program', '--term', '15']):
            result = parse_commandline.parse_commandline()
        self.assertEqual(15, result.term)

    def test_term_6(self):
        with patch.object(sys, 'argv', ['program', '--term', 'illegal']):
            with self.assertRaises(Exception):
                result = parse_commandline.parse_commandline()

    def test_rate(self):
        with patch.object(sys, 'argv', ['program', '--rate', '4.25']):
            result = parse_commandline.parse_commandline()
        self.assertEqual(4.25, result.rate)
