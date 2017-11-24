@echo off
REM METADATADIFF launcher script for Windows
REM ========================================
REM Copyright(c) 2017 Jonas Sjöberg
REM https://github.com/jonasjberg
REM http://www.jonasjberg.com
REM University mail: js224eh[a]student.lnu.se


SET self_path=%~dp0
pushd %self_path%
PYTHONPATH=. python metadatadiff
popd

