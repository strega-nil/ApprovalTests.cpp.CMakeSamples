#!/bin/sh

mkdir -p build
cd       build
cmake -DCMAKE_BUILD_TYPE=Debug ..
cmake --build .
ctest ctest --output-on-failure . -C Debug
