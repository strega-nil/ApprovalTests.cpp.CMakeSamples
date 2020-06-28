

```cmake
#!/bin/sh

sourcedir=`pwd`
mkdir -p build
cd       build
conan install ..
cmake  ..
cmake --build .
ctest .
```
<sup><a href='https://github.com/claremacrae/ApprovalTests.cpp.CMakeSamples/blob/main/./conan_cmake_find_package/build.sh' title='File snippet was copied from'>snippet source</a></sup>

