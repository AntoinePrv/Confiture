# coding: utf-8

"""Test module for configurator module."""

import unittest
from unittest import mock
from .configurator import Configure


class TestConfigure(unittest.TestCase):

    def test_init(self):
        c = Configure({"a": 0}, "override")
        self.assertDictEqual(c._Configure__config, {"a": 0})
        self.assertEqual(c._Configure__mode, "override")
        self.assertRaises(ValueError, Configure, {}, "a")

    def test_mode(self):
        c = Configure({"a": 0})
        d = c.mode("override")
        self.assertIsNot(c, d)
        self.assertDictEqual(c._Configure__config, d._Configure__config)
        self.assertEqual(d._Configure__mode, "override")
