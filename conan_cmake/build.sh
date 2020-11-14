#!/bin/sh

mkdir -p build
cd       build
conan install ..
cmake -DCMAKE_BUILD_TYPE=Debug ..
cmake --build .
ctest . -C Debug
