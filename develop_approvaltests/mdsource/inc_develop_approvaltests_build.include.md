

```bash
#!/bin/sh

mkdir -p build
cd       build
cmake -DCMAKE_BUILD_TYPE=Debug ..
cmake --build .
ctest ctest --output-on-failure . -C Debug
```
<sup><a href='https://github.com/claremacrae/ApprovalTests.cpp.CMakeSamples/blob/main/./develop_approvaltests/build.sh' title='File snippet was copied from'>snippet source</a></sup>

