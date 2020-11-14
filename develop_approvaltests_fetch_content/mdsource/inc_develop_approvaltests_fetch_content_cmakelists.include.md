

```cmake
cmake_minimum_required(VERSION 3.14 FATAL_ERROR)

project(develop_approvaltests_fetch_content)

enable_testing()

set(CMAKE_VERBOSE_MAKEFILE off)

# Prevent ctest creating cluttering up CLion with nearly 30 CTest targets
# (Continuous, ContinuousBuild etc) when it does:
#   include(CTest)
# This hack taken from https://stackoverflow.com/a/57240389/104370
set_property(GLOBAL PROPERTY CTEST_TARGETS_ADDED 1) # hack to prevent CTest added targets

# Needs CMake 3.14 or above
include(FetchContent)

# -------------------------------------------------------------------
# boost
message(NOTICE "Fetching Boost...")
FetchContent_Declare(
        Boost
        URL https://dl.bintray.com/boostorg/release/1.74.0/source/boost_1_74_0.tar.gz
)
FetchContent_MakeAvailable(Boost)
# This is needed because there is not a CMakeLists.txt in the Boost download,
# so we have to teach find_package() to find Boost
set(BOOST_ROOT ${boost_SOURCE_DIR})

# -------------------------------------------------------------------
# Catch2
message(NOTICE "Fetching Catch2...")
set(CATCH_BUILD_TESTING OFF CACHE BOOL "")
FetchContent_Declare(Catch2
        GIT_REPOSITORY https://github.com/catchorg/Catch2.git
        GIT_TAG v2.11.1)
FetchContent_MakeAvailable(Catch2)

# -------------------------------------------------------------------
# CppUTest
message(NOTICE "Fetching cpputest...")
FetchContent_Declare(cpputest
        GIT_REPOSITORY https://github.com/cpputest/cpputest.git
        GIT_TAG v4.0)
FetchContent_MakeAvailable(cpputest)

# -------------------------------------------------------------------
# doctest
message(NOTICE "Fetching doctest...")
FetchContent_Declare(
        doctest
        GIT_REPOSITORY  https://github.com/onqtam/doctest
        GIT_TAG         2.4.0
)
FetchContent_MakeAvailable(doctest)
set_target_properties(doctest_with_main PROPERTIES FOLDER "external")

# -------------------------------------------------------------------
# fmt
message(NOTICE "Fetching fmt...")
set(CATCH_BUILD_TESTING OFF CACHE BOOL "")
FetchContent_Declare(fmt
        GIT_REPOSITORY https://github.com/fmtlib/fmt.git
        GIT_TAG 6.2.0)
FetchContent_MakeAvailable(fmt)

# -------------------------------------------------------------------
message(NOTICE "Fetching googletest...")
# GoogleTest
# Prevent GoogleTest from overriding our compiler/linker options
# when building with Visual Studio
set(gtest_force_shared_crt ON CACHE BOOL "" )
FetchContent_Declare(googletest
        GIT_REPOSITORY https://github.com/abseil/googletest.git
        GIT_TAG release-1.8.1)
FetchContent_MakeAvailable(googletest)

# -------------------------------------------------------------------
# Boost.ut
message(NOTICE "Fetching boost.ut...")
set(BUILD_BENCHMARKS OFF CACHE BOOL "")
set(BUILD_EXAMPLES OFF CACHE BOOL "")
set(BUILD_TESTS OFF CACHE BOOL "")
FetchContent_Declare(boost.ut
        GIT_REPOSITORY https://github.com/boost-ext/ut.git
        GIT_TAG v1.1.7)
FetchContent_MakeAvailable(boost.ut)

if ("${CMAKE_CXX_COMPILER_ID}" MATCHES "Clang")
    # Turn off some checks off for boost.ut
    target_compile_options(boost.ut INTERFACE
            -Wno-c99-extensions # Needed for Boost.ut, at least in v1.1.6
            -Wno-documentation-unknown-command # unknown command tag name \userguide
            -Wno-weak-vtables
            -Wno-comma # See https://github.com/boost-ext/ut/issues/398
            )
endif()

# -------------------------------------------------------------------
# ApprovalTests.cpp

set(APPROVAL_TESTS_BUILD_TESTING ON CACHE BOOL "")
set(APPROVAL_TESTS_BUILD_EXAMPLES ON CACHE BOOL "")

add_subdirectory(
        ../ApprovalTests.cpp
        ${CMAKE_CURRENT_BINARY_DIR}/approvaltests.cpp_build
)
```
<sup><a href='https://github.com/claremacrae/ApprovalTests.cpp.CMakeSamples/blob/main/./develop_approvaltests_fetch_content/CMakeLists.txt' title='File snippet was copied from'>snippet source</a></sup>

