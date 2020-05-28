cmake_minimum_required(VERSION 3.14 FATAL_ERROR)

project(conan_cmake)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

enable_testing()

add_subdirectory(tests)
