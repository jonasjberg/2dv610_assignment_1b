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


def load_file(file_path):
    def _raise_invalid_path():
        raise FileNotFoundError('Invalid file path: "{!s}"'.format(file_path))

    if not file_path or not isinstance(file_path, str):
        _raise_invalid_path()
    if not file_path.strip():
        _raise_invalid_path()

    if not os.path.isfile(file_path):
        _raise_invalid_path()


def load_json(file_path):
    pass


class FileLoader(object):
    LOADERS = {}

    def __init__(self):
        pass

    def __call__(self, file_path):
        loader = self._loader_for_filetype(file_path)
        assert callable(loader)
        return loader(file_path)

    @staticmethod
    def _validate_path(file_path):
        try:
            is_valid_path = os.path.isfile(file_path)
        except (OSError, TypeError):
            return False
        else:
            return is_valid_path

    @classmethod
    def _file_extension(cls, file_path):
        try:
            _, extension = os.path.splitext(file_path)
        except OSError:
            return None
        else:
            assert isinstance(extension, str)
            extension = extension.lstrip('.').strip()
            return extension

    @classmethod
    def _loader_for_filetype(cls, file_path):
        # NOTE: It is always more robust to get the MIME-type from the "magic"
        #       header bytes, but this will have to be good enough for now.

        extension = cls._file_extension(file_path)
        return cls.LOADERS.get(extension)
