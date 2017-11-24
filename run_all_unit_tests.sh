#!/usr/bin/env bash

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

set -o noclobber -o nounset -o pipefail

SELF="$(basename "$0")"
SELF_DIR="$(realpath -e "$(dirname "$0")")"
TESTRESULTS_DIR="${SELF_DIR}/testreports"

# Default options.
option_write_report='false'
option_quiet='false'
option_enable_coverage='false'


print_usage_info()
{
    cat <<EOF

"${SELF}"  --  metadatadiff unit tests runner

  USAGE:  ${SELF} ([OPTIONS])

  OPTIONS:  -h   Display usage information and exit.

            -c   Enable checking unit test coverage.
                 NOTE: Requires "pytest" and "pytest-html".

            -w   Write HTML test reports to disk.
                 Also writes a report of the test coverage if
                 combined with the '-c' option.

                 NOTE: Requires "pytest" and "pytest-html".
                       Coverage reports require "pytest-cov".

                 Reports are written to the following path:
                 "${TESTRESULTS_DIR}"

            -q   Suppress output from test suites.

  All options are optional. Default behaviour is to not write any
  reports and print the test results to stdout/stderr in real-time.

  Tests are executed with "pytest" if available, else "unittest".

EOF
}



# Set options to 'true' here and invert logic as necessary when testing (use
# "if not true"). Motivated by hopefully reducing bugs and weird behaviour
# caused by users setting the default option variables to unexpected values.
if [ "$#" -eq "0" ]
then
    printf "(USING DEFAULTS -- "${SELF} -h" for usage information)\n\n"
else
    while getopts chwq opt
    do
        case "$opt" in
            c) option_enable_coverage='true' ;;
            h) print_usage_info ; exit 0 ;;
            w) option_write_report='true' ;;
            q) option_quiet='true' ;;
        esac
    done

    shift $(( $OPTIND - 1 ))
fi


HAS_PYTEST='false'
if command -v "pytest" >/dev/null 2>&1
then
    HAS_PYTEST='true'

    # Workaround for pytest crashing when writing something other than stdout ..
    captured_pytest_help="$(pytest --help 2>&1)"
fi

if [ "$option_write_report" == 'true' ]
then
    # Make sure required executables are available.
    if [ "$HAS_PYTEST" != 'true' ]
    then
        echo "This script requires \"pytest\" to generate HTML reports." 1>&2
        echo "Install using pip by executing:  pip3 install pytest"
        exit 1
    fi

    if ! grep -q -- '--html' <<< "$captured_pytest_help"
    then
        echo "This script requires \"pytest-html\" to generate HTML reports." 1>&2
        echo "Install using pip by executing:  pip3 install pytest-html"
        exit 1
    fi
fi

if [ "$option_enable_coverage" == 'true' ]
then
    # Make sure required executables are available.
    if [ "$HAS_PYTEST" != 'true' ]
    then
        echo "This script requires \"pytest\" to check test coverage." 1>&2
        echo "Install using pip by executing:  pip3 install pytest"
        exit 1
    fi

    if ! grep -q -- '--cov' <<< "$captured_pytest_help"
    then
        echo "This script requires \"pytest-cov\" to check test coverage." 1>&2
        echo "Install using pip by executing:  pip3 install pytest-cov"
        exit 1
    fi
fi




_timestamp="$(date "+%Y-%m-%dT%H%M%S")"
_unittest_log="${TESTRESULTS_DIR}/unittest_log_${_timestamp}.html"
if [ -e "$_unittest_log" ]
then
    echo "File exists: \"${_unittest_log}\" .. Aborting" >&2
    exit 1
fi

_coverage_log="${TESTRESULTS_DIR}/coverage_log_${_timestamp}.html"
if [ -e "$_coverage_log" ]
then
    echo "File exists: \"${_coverage_log}\" .. Aborting" >&2
    exit 1
fi


run_unittest()
{
    python3 -m unittest discover --catch --buffer --start-directory tests \
            --pattern "unit_test_*.py" --top-level-directory .
}

run_pytest()
{
    _pytest_report_opts=''
    _pytest_coverage_opts=''
    if [ "$option_write_report" == 'true' ]
    then
        _pytest_report_opts="--self-contained-html --html="${_unittest_log}""
        if [ "$option_enable_coverage" == 'true' ]
        then
            _pytest_coverage_opts="--cov=metadatadiff --cov-report=html:"${_coverage_log}""
        fi
    else
        if [ "$option_enable_coverage" == 'true' ]
        then
            _pytest_coverage_opts="--cov=metadatadiff --cov-report=term"
        fi
    fi

    pytest ${_pytest_report_opts} ${_pytest_coverage_opts} tests/unit_test_*.py
}


(
    cd "$SELF_DIR" || return 1
    PYTHONPATH=metadatadiff:tests

    if [ "$HAS_PYTEST" != 'true' ]
    then
        run_unittest
    else
        run_pytest
    fi
)

