

```bash
#!/bin/sh

sourcedir=`pwd`
mkdir -p build
cd       build
cmake  ..
cmake --build .
ctest .
```
<sup><a href='https://github.com/claremacrae/ApprovalTests.cpp.CMakeSamples/blob/main/./add_subdirectory_approvaltests_catch2/build.sh' title='File snippet was copied from'>snippet source</a></sup>

