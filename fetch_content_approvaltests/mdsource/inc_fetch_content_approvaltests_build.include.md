

```cmake
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
```
<sup><a href='https://github.com/claremacrae/ApprovalTests.cpp.CMakeSamples/blob/main/./fetch_content_approvaltests/build.sh' title='File snippet was copied from'>snippet source</a></sup>

