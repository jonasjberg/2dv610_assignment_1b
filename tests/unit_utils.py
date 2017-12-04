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

import unit_constants as uuconst


def abspath_testfile(basename):
    """
    Utility function used by tests to construct a full path to individual test
    files in the 'test_files' directory.

    Args:
        basename: The basename of a file in the 'test_files' directory
                  as a Unicode string (internal string format)

    Returns:
        The full absolute path to the given file.
    """
    assert basename, 'Got empty argument "basename"'
    assert isinstance(basename, str), (
        'Expect "basename" to of type "str", not "{!s}"'.format(type(basename))
    )

    path = os.path.abspath(os.path.join(uuconst.TEST_FILES_DIR, basename))
    try:
        if os.path.exists(path):
            return path
    except (OSError, TypeError):
        pass

    raise FileNotFoundError
