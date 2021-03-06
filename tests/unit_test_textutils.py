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

from unittest import TestCase

from metadatadiff import textutils


class TestLevenshteinDistance(TestCase):
    def test_is_defined(self):
        self.assertIsNotNone(textutils.levenshtein)

    def test_returns_integers(self):
        actual = textutils.levenshtein('a', 'b')
        self.assertTrue(isinstance(actual, int))

    def test_returns_expected_string_difference(self):
        TESTDATA_GIVEN_A_B_EXPECT = [
            ('a', 'a', 0),
            ('a', 'b', 1),
            ('a', 'ab', 1),
            ('a', 'ab', 1),
            ('c', 'ab', 2),
            ('cd', 'ab', 2),
            ('abc', 'abc', 0),
            ('abc', 'cba', 2),
            ('meow', 'meow', 0),
            ('meeeow', 'meow', 2),
            ('MEOW', 'meow', 4),
            ('MEOW', 'meeeow', 6),
        ]

        for a, b, expect in TESTDATA_GIVEN_A_B_EXPECT:
            actual = textutils.levenshtein(a, b)
            self.assertEqual(actual, expect)
