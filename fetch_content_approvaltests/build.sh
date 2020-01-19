#!/bin/sh

# Force execution to halt if there are any errors in this script:
set -e
set -o pipefail

sourcedir=`pwd`
mkdir -p cmake-build-spaces/cmake-build-command-line
cd       cmake-build-spaces/cmake-build-command-line
cmake -Wdev $sourcedir
cmake --build .
ctest .
