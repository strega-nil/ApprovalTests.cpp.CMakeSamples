#!/bin/sh

sourcedir=`pwd`
mkdir -p build
cd       build
cmake -Wdev ..
cmake --build .
ctest .
