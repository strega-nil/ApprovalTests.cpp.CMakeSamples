#!/bin/sh

sourcedir=`pwd`
mkdir -p build
cd       build
conan install ..
cmake  ..
cmake --build .
ctest .
