# -*- coding: utf-8 -*-
"""Tests for the output writer."""

import os
import unittest

from dtformats import output_writer

from tests import test_lib


class StdoutWriterTest(test_lib.BaseTestCase):
  """Stdout output writer tests."""

  def testClose(self):
    """Tests the Close function."""
    test_writer = output_writer.StdoutWriter()

    test_writer.Close()

  def testOpen(self):
    """Tests the Open function."""
    test_writer = output_writer.StdoutWriter()

    test_writer.Open()

  def testWriteText(self):
    """Tests the WriteText function."""
    test_writer = output_writer.StdoutWriter()

    test_writer.WriteText(u'')


if __name__ == '__main__':
  unittest.main()
