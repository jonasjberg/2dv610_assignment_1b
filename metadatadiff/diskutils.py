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


def load_file(file_path):
    def _raise_invalid_path():
        raise ValueError('Invalid file path: "{!s}"'.format(file_path))

    if not file_path or not isinstance(file_path, str):
        _raise_invalid_path()
    if not file_path.strip():
        _raise_invalid_path()


class FileLoader(object):
    def __init__(self):
        pass

    def __call__(self, file_path):
        pass

    def _validate_path(self, file_path):
        pass

