### 2DV610 --- Software Testing

Assignment 1, Part 2: XUnit Testing
===================================
*Copyright(c) 2017 Jonas Sjöberg*  
<https://github.com/jonasjberg>  
<http://www.jonasjberg.com>  
University mail: `js224eh[a]student.lnu.se`  

--------------------------------------------------------------------------------

This is the second part of the first assignment in the course "`2DV610` --
"Software Testing", given at [Linnaeus University](https://lnu.se/en/) as part
of the "[Software Development and Operations](https://udm-devops.se/)"
programme.

Written by Jonas Sjöberg (`js224eh`)



Program Description
===================
This program will compare *metadata* and display any differences along with a
similarity score between 0 and 1.

Example metadata:
```python
isbn_metadata_1 = {
    'Title'     : 'Mastering Windows Network Forensics And Investigation',
    'Authors'   : ['Steven Anson', 'Steve Bunting', 'Ryan Johnson', 'Scott Pearson'],
    'Publisher' : 'Sybex',
    'Year'      : 2012,
    'Language'  : 'eng',
    'ISBN-10'   : 1118236084,
    'ISBN-13'   : 9781118236086
}
```

If the above metadata was to be compared with this;
```python
isbn_metadata_2 = {
    'Title'     : 'Mastering Windows Network Forensics And Investigation',
    'Authors'   : ['Steve Anson ... [et al.]'],
    'Publisher' : 'Wiley',
    'Year'      : 2012,
    'Language'  : 'eng',
    'ISBN-10'   : 1118264118,
    'ISBN-13'   : 9781118264119
}
```

.. the program output should be something along the lines of:
```
Comparison results
==================

'Title'      Similarity: 1.0
'Authors'    Similarity: 0.2
                   Diff: ['Steven Anson', 'Steve Bunting', 'Ryan Johnson', 'Scott Pearson']
                         ['Steve Anson ... [et al.]']

'Publisher'  Similarity: 0.0
                   Diff: 'Sybex'
                         'Wiley'

'Year'       Similarity: 1.0
'Language'   Similarity: 1.0
'ISBN-10'    Similarity: 0.0
                   Diff: 1118236084
                         1118264118

'ISBN-13'    Similarity: 0.0
                   Diff: 9781118236086
                         9781118264119

 TOTAL SIMILARITY SCORE: 0.6
```



Running/Requirements
====================
This program requires Python 3 to run.
It has been developed on Linux and MacOS but should run fine on Windows.


A wrapper script is provided for running all unit tests and optionally
producing HTML reports of the test result and test coverage.

Runner script help text:
```
"run_all_unit_tests.sh"  --  metadatadiff unit tests runner

  USAGE:  run_all_unit_tests.sh ([OPTIONS])

  OPTIONS:  -h   Display usage information and exit.

            -c   Enable checking unit test coverage.
                 NOTE: Requires "pytest" and "pytest-html".

            -w   Write HTML test reports to disk.
                 Also writes a report of the test coverage if
                 combined with the '-c' option.

                 NOTE: Requires "pytest" and "pytest-html".
                       Coverage reports require "pytest-cov".

                 Reports are written to the following path:
                 "/Users/jonas/Dropbox/LNU/2DV610_Testing/src/2dv610_assignment-1b.git/testreports"

            -q   Suppress output from test suites.

  All options are optional. Default behaviour is to not write any
  reports and print the test results to stdout/stderr in real-time.

  Tests are executed with "pytest" if available, else "unittest".
```
