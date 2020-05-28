cmake_minimum_required(VERSION 3.14 FATAL_ERROR)

project(conan_cmake_find_package)

include(${CMAKE_BINARY_DIR}/conan_paths.cmake)
find_package(Catch2)
find_package(ApprovalTests)

enable_testing()

add_subdirectory(tests)
