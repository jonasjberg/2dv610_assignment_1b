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

import argparse
import sys

from application import real_main
import constants as C


def main(args):
    parser = argparse.ArgumentParser(
        prog=C.STR_PROGRAM_NAME,
        description='{} {} -- Metadata Difference Utility'.format(
            C.STR_PROGRAM_NAME, C.STR_PROGRAM_VERSION
        ),
        epilog='{}  {}'.format(
            C.STR_COPYRIGHT, C.STR_URL_PROJECT
        )
    )
    parser.add_argument(
        '-v', '--verbose',
        dest='verbose',
        action='store_true',
        default=False,
        help='Enables verbose mode, prints additional information.'
    )

    opts = parser.parse_args(args)
    real_main(opts)
    print('Hellow World')


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        print('\nReceived keyboard interrupt. Exiting ..')
        sys.exit(0)
