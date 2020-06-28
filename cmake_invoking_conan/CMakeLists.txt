cmake_minimum_required(VERSION 3.14 FATAL_ERROR)

project(conan_cmake)

# Load CMake/Conan.cmake, which sets up a 'run_conan()' macro to download dependencies.
include(CMake/Conan.cmake)
run_conan()

enable_testing()

add_subdirectory(tests)
