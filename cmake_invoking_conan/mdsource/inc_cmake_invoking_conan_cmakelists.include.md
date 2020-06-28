

```cmake
cmake_minimum_required(VERSION 3.14 FATAL_ERROR)

project(conan_cmake)

# Load CMake/Conan.cmake, which sets up a 'run_conan()' macro to download dependencies.
include(CMake/Conan.cmake)
run_conan()

enable_testing()

add_subdirectory(tests)
```
<sup><a href='https://github.com/claremacrae/ApprovalTests.cpp.CMakeSamples/blob/main/./cmake_invoking_conan/CMakeLists.txt' title='File snippet was copied from'>snippet source</a></sup>

