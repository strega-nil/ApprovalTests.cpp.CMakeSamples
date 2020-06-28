cmake_minimum_required(VERSION 3.14 FATAL_ERROR)

project(conan_cmake)

include(CMake/Conan.cmake)
run_conan()

enable_testing()

add_subdirectory(tests)
