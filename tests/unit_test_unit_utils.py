# -*- coding: utf-8 -*-

#   Copyright(c) 2016-2017 Jonas Sjöberg
#   Personal site:   http://www.jonasjberg.com
#   GitHub:          https://github.com/jonasjberg
#   University mail: js224eh[a]student.lnu.se
#
#   This file is part of metadatadiff.
#
#   metadatadiff is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation.
#
#   metadatadiff is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with metadatadiff.  If not, see <http://www.gnu.org/licenses/>.

import os
from unittest import TestCase

import unit_utils as uu


class TestAbsPathTestFile(TestCase):
    def test_abspath_testfile_is_defined(self):
        self.assertIsNotNone(uu.abspath_testfile)

    def test_raises_assertion_error_given_none_argument(self):
        with self.assertRaises(AssertionError):
            _ = uu.abspath_testfile(None)

    def test_raises_assertion_error_given_non_string_argument(self):
        def __assert_raises(given):
            with self.assertRaises(AssertionError):
                _ = uu.abspath_testfile(given)

        __assert_raises(1337)
        __assert_raises(b'foo')
        __assert_raises(['foo', 'bar'])

    def test_raises_file_not_found_error_for_basename_of_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            _ = uu.abspath_testfile('_.this_is_not_a_file_surely._')

    def test_returns_absolute_paths_given_basenames_of_existing_files(self):
        def __assert_ok(basename):
            actual = uu.abspath_testfile(basename)
            self.assertIsNotNone(actual)
            self.assertTrue(os.path.exists(actual))

        __assert_ok('.keep')
