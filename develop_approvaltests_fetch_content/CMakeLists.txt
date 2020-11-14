cmake_minimum_required(VERSION 3.8 FATAL_ERROR)

project(develop_approvaltests_fetch_content)

enable_testing()
#include(CMakePrintHelpers)

set(CMAKE_VERBOSE_MAKEFILE off)
set_property(GLOBAL PROPERTY CTEST_TARGETS_ADDED 1) # hack to prevent CTest added targets

add_subdirectory(dependencies)

# -------------------------------------------------------------------
# ApprovalTests.cpp

set(APPROVAL_TESTS_BUILD_TESTING ON CACHE BOOL "")
set(APPROVAL_TESTS_BUILD_EXAMPLES ON CACHE BOOL "")

add_subdirectory(
        ../ApprovalTests.cpp
        ${CMAKE_CURRENT_BINARY_DIR}/approvaltests.cpp_build
)
