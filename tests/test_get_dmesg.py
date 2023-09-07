#!/usr/bin/env python

import unittest
from mock import patch


import check_dmesg


class GetDmesgTestCase(unittest.TestCase):
    def setUp(self):
        pass

    @patch("check_dmesg.subprocess.run")
    def test_get_dmesg(self, mock_subprocess_run):
        mock_subprocess_run.return_value.stdout = "error"

        output = check_dmesg.get_dmesg(log_level="err")
        self.assertEqual(output, "error")
