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
    def test_is_defined(self):
        self.assertIsNotNone(Author)
