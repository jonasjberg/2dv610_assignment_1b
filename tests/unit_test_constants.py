# -*- coding: utf-8 -*-

#   Copyright(c) 2016-2017 Jonas Sjöberg
#   Personal site:   http://www.jonasjberg.com
#   GitHub:          https://github.com/jonasjberg
#   University mail: js224eh[a]student.lnu.se
#
#   This file is part of autonameow.
#
#   autonameow is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation.
#
#   autonameow is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with autonameow.  If not, see <http://www.gnu.org/licenses/>.

from unittest import TestCase

from metadatadiff.constants import (
    STR_COPYRIGHT,
    STR_PROGRAM_NAME,
    STR_PROGRAM_VERSION,
    STR_URL_AUTHOR,
    STR_URL_PROJECT,
)


class TestConstants(TestCase):
    def test_str_copyright(self):
        self.assertIsNotNone(STR_COPYRIGHT)
        self.assertTrue(isinstance(STR_COPYRIGHT, str))

    def test_str_program_name(self):
        self.assertIsNotNone(STR_PROGRAM_NAME)
        self.assertTrue(isinstance(STR_PROGRAM_NAME, str))

    def test_str_program_version(self):
        self.assertIsNotNone(STR_PROGRAM_VERSION)
        self.assertTrue(isinstance(STR_PROGRAM_VERSION, str))

    def test_str_url_author(self):
        self.assertIsNotNone(STR_URL_AUTHOR)
        self.assertTrue(isinstance(STR_URL_AUTHOR, str))

    def test_str_url_project(self):
        self.assertIsNotNone(STR_URL_PROJECT)
        self.assertTrue(isinstance(STR_URL_PROJECT, str))
