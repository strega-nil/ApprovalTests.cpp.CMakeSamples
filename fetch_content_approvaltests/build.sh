#!/bin/sh

sourcedir=`pwd`
mkdir -p build
cd       build
cmake  ..
cmake --build .
ctest .
