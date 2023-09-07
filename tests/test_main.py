#!/usr/bin/env python

import sys
import unittest
from mock import patch

import check_dmesg


class MainTestCase(unittest.TestCase):
    def setUp(self):
        pass

    @patch("check_dmesg.get_dmesg")
    def test_main(self, mock_get_dmesg):
        #
        # Test with no issues
        #
        with patch.object(sys, "argv", ["check_dmesg.py"]):
            mock_get_dmesg.return_value = ""

            self.assertEqual(check_dmesg.main(), 0)

        #
        # Test with min-days failure
        #
        with patch.object(sys, "argv", ["check_dmesg.py"]):
            mock_get_dmesg.return_value = "error"

            self.assertEqual(check_dmesg.main(), 1)
