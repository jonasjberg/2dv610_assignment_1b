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

import unit_utils as uu


class TestAbsPathTestFile(TestCase):
    def test_abspath_testfile_is_defined(self):
        self.assertIsNotNone(uu.abspath_testfile)

    def test_raises_assertion_error_given_none_argument(self):
        with self.assertRaises(AssertionError):
            _ = uu.abspath_testfile(None)
