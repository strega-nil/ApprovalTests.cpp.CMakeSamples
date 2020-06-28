#!/bin/sh

sourcedir=`pwd`
mkdir -p cmake-build-spaces/cmake-build-command-line
cd       cmake-build-spaces/cmake-build-command-line
conan install $sourcedir
cmake -Wdev $sourcedir
cmake --build .
ctest .
