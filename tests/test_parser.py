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
