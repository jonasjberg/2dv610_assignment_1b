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

from collections import namedtuple
from unittest import TestCase

from metadatadiff.model.field import (
    Author,
    BaseField
)


class TestBaseField(TestCase):
    def test_is_defined(self):
        self.assertIsNotNone(BaseField)

    def test_init_accepts_one_parameter(self):
        f = BaseField('foo')
        self.assertIsNotNone(f)

    def test_instance_comparison(self):
        f1 = BaseField('foo')
        f2 = BaseField('foo')
        f3 = BaseField('bar')
        self.assertTrue(f1 == f1, 'Expected {!r} == {!r}'.format(f1, f1))
        self.assertTrue(f1 == f2, 'Expected {!r} == {!r}'.format(f1, f2))
        self.assertTrue(f1 != f3, 'Expected {!r} != {!r}'.format(f1, f3))
        self.assertTrue(f2 != f3, 'Expected {!r} != {!r}'.format(f2, f3))


class TestFieldAuthor(TestCase):
    def setUp(self):
        self.author = Author('Gibson Meow Sjöberg')

    def test_attribute_first_name_is_expected_type(self):
        actual = self.author.firstname
        self.assertTrue(isinstance(actual, str))

    def test_attribute_last_name_is_expected_type(self):
        actual = self.author.lastname
        self.assertTrue(isinstance(actual, str))

    def test_attribute_middle_name_is_expected_type(self):
        actual = self.author.middlename
        self.assertTrue(isinstance(actual, str))

    def __assert_that(self, instance, attribute, equals):
        expected = equals
        actual = getattr(instance, attribute)
        _msg = 'Expected {!s} of {!r} to be "{!s}". Got "{!s}"'.format(
            attribute, instance, expected, actual
        )
        self.assertEqual(actual, expected, _msg)

    def test_attribute_first_name_has_expected_value(self):
        self.__assert_that(self.author, 'firstname', equals='Gibson')

    def test_attribute_last_name_has_expected_value(self):
        self.__assert_that(self.author, 'lastname', equals='Sjöberg')

    def test_attribute_middle_name_has_expected_value(self):
        self.__assert_that(self.author, 'middlename', equals='Meow')


class TestFieldAuthorNameSegmentation(TestCase):
    # Using 'namedtuple' for readability.
    TD = namedtuple('TD', 'Full First Middle Last')

    # List of tuples, each containing input data and the expected output data.
    TESTDATA_FULLNAME_EXPECTED_SEGMENTS = [
        TD(Full='Gibson Meow Sjöberg',
           First='Gibson', Middle='Meow', Last='Sjöberg'),
        TD(Full='Gibson Sjöberg',
           First='Gibson', Middle='', Last='Sjöberg'),
        TD(Full='Gibson',
           First='Gibson', Middle='', Last=''),
        TD(Full='Jonas Sjöberg',
           First='Jonas', Middle='', Last='Sjöberg'),
        TD(Full='Jonas',
           First='Jonas', Middle='', Last=''),
    ]

    def test_testdata(self):
        """
        Sanity-checking.
        """
        def __assert_valid_type(value):
            self.assertTrue(isinstance(value, str))

        for testdata in self.TESTDATA_FULLNAME_EXPECTED_SEGMENTS:
            __assert_valid_type(testdata.Full)
            __assert_valid_type(testdata.First)
            __assert_valid_type(testdata.Middle)
            __assert_valid_type(testdata.Last)

    def test_first_name(self):
        for testdata in self.TESTDATA_FULLNAME_EXPECTED_SEGMENTS:
            actual = Author(testdata.Full).firstname
            self.assertEqual(actual, testdata.First)
