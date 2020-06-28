

```bash
#!/bin/sh

mkdir -p build
cd       build
# Note that we do not need to invoke conan.
# However, we do need to say what build configuration we want.
cmake  -DCMAKE_BUILD_TYPE=Debug ..
cmake --build .
ctest .
```
<sup><a href='https://github.com/claremacrae/ApprovalTests.cpp.CMakeSamples/blob/main/./cmake_invoking_conan/build.sh' title='File snippet was copied from'>snippet source</a></sup>

