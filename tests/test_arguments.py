#!/usr/bin/env python

import unittest

import check_dmesg


class ArgumentsTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_parse_arguments(self):
        args = check_dmesg.parse_arguments(["--log-level", "err"])
        self.assertEqual(args.log_level, "err")
