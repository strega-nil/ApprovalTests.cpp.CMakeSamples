#!/bin/sh

sourcedir=`pwd`
mkdir -p cmake-build-spaces/cmake-build-command-line
cd       cmake-build-spaces/cmake-build-command-line
cmake $sourcedir
cmake --build .
ctest .
