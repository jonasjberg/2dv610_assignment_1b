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

from unittest import TestCase, mock

import diskutils


class TestLoadFile(TestCase):
    def test_load_file_is_defined(self):
        self.assertIsNotNone(diskutils.load_file)

    def test_raises_exception_when_given_invalid_path(self):
        def __assert_raises(test_input):
            with self.assertRaises(FileNotFoundError):
                _ = diskutils.load_file(test_input)

        __assert_raises(None)
        __assert_raises('')
        __assert_raises(' ')
        __assert_raises(b'')
        __assert_raises(b' ')
        __assert_raises(object())


class TestFileLoader(TestCase):
    def test__validate_path_raises_exception_given_invalid_path(self):
        def __assert_false(test_input):
            actual = diskutils.FileLoader._validate_path(test_input)
            self.assertFalse(actual)

        __assert_false(None)
        __assert_false('')
        __assert_false(' ')
        __assert_false(b'')
        __assert_false(b' ')
        __assert_false(object())
        __assert_false('/tmp/does/not/exist/surely/..right?')

    # Isolate ourselves from any real I/O.
    @mock.patch('os.path.splitext')
    def test__file_extension(self, mock_splitext):
        mock_splitext.return_value = ('foo', '.txt')
        expect = 'txt'
        actual = diskutils.FileLoader._file_extension('foo.txt')
        self.assertEqual(expect, actual)
