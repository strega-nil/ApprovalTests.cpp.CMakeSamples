#!/bin/sh

sourcedir=`pwd`
mkdir -p build
cd       build
conan install ..
cmake -Wdev ..
cmake --build .
ctest .
