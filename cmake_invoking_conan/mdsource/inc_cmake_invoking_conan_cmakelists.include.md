

```cmake
cmake_minimum_required(VERSION 3.14 FATAL_ERROR)

project(conan_cmake)

# Provide path for scripts
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/CMake")
include(Conan)
run_conan()

enable_testing()

add_subdirectory(tests)
```
<sup><a href='https://github.com/claremacrae/ApprovalTests.cpp.CMakeSamples/blob/main/./cmake_invoking_conan/CMakeLists.txt' title='File snippet was copied from'>snippet source</a></sup>

