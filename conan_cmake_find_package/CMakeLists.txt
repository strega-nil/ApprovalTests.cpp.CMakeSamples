cmake_minimum_required(VERSION 3.14 FATAL_ERROR)

project(conan_cmake_find_package)

# EITHER Using the "cmake_find_package" generator
#set(CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR} ${CMAKE_MODULE_PATH})
#set(CMAKE_PREFIX_PATH ${CMAKE_BINARY_DIR} ${CMAKE_PREFIX_PATH})

# OR Using the "cmake_find_package" and "cmake_paths" generators
include(${CMAKE_BINARY_DIR}/conan_paths.cmake)

find_package(Catch2 REQUIRED)
find_package(ApprovalTests REQUIRED)

enable_testing()

add_subdirectory(tests)
