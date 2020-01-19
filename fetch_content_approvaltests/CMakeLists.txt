cmake_minimum_required(VERSION 3.14 FATAL_ERROR)
# This version is needed for FetchContent_Declare & FetchContent_MakeAvailable

project(fetch_content_approvaltests)

include(FetchContent)
if (NOT TARGET ApprovalTests)
    FetchContent_Declare(ApprovalTests
            GIT_REPOSITORY https://github.com/approvals/ApprovalTests.cpp.git
            GIT_TAG cmake_docs) # TODO Merge cmake_docs to default - then change this to master

    # Tell the ApprovalTests CMake files that we want to use its copy of Catch2:
    set(APPROVAL_TESTS_BUILD_THIRD_PARTY_CATCH2 ON CACHE BOOL "")

    # See also
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    set(APPROVAL_TESTS_BUILD_THIRD_PARTY_GOOGLE_TEST ON CACHE BOOL "") # TODO This is giving an error
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    set(APPROVAL_TESTS_BUILD_THIRD_PARTY_DOCTEST ON CACHE BOOL "")
    set(APPROVAL_TESTS_BUILD_THIRD_PARTY_UT ON CACHE BOOL "")

    FetchContent_MakeAvailable(ApprovalTests)
endif ()

enable_testing()

add_subdirectory(tests)
