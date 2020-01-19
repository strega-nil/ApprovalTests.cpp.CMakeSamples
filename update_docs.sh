#!/bin/sh

# Force execution to halt if there are any errors in this script:
set -e
set -o pipefail

./create_markdown.py > ../ApprovalTests.cpp/doc/mdsource/include_cmake_samples.include.md
pushd ../ApprovalTests.cpp
./run_markdown_templates.sh
popd
