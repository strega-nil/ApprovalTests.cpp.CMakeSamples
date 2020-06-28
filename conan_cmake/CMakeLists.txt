cmake_minimum_required(VERSION 3.14 FATAL_ERROR)

project(conan_cmake)

# Conan's cmake generator creates a conanbuildinfo.cmake file, which we
# need to include, and then use:
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

enable_testing()

add_subdirectory(tests)
