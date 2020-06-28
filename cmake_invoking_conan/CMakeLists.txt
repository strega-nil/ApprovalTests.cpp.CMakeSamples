cmake_minimum_required(VERSION 3.14 FATAL_ERROR)

project(conan_cmake)

# Provide path for scripts
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/CMake")
include(Conan)
run_conan()

enable_testing()

add_subdirectory(tests)
