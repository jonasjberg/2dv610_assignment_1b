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


class BaseField(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return '{!s}("{!s}")'.format(self.__class__.__name__, self.value)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.value == other.value:
            return True
        return False


class Author(BaseField):
    def __init__(self, value):
        super().__init__(value)

        self._firstname, *_ = value.split(' ')

    @property
    def firstname(self):
        return self._firstname

    @property
    def lastname(self):
        return ''

    @property
    def middlename(self):
        return ''
