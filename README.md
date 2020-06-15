<!--
GENERATED FILE - DO NOT EDIT
This file was generated by [MarkdownSnippets](https://github.com/SimonCropp/MarkdownSnippets).
Source File: /mdsource/README.source.md
To change this file edit the source file and then execute ./run_markdown_templates.sh.
-->

# ApprovalTests.cpp.CMakeSamples

<!-- toc -->
## Contents

  * [add_subdirectory_approvaltests_catch2](#add_subdirectory_approvaltests_catch2)
  * [fetch_content_approvaltests](#fetch_content_approvaltests)
  * [fetch_content_approvaltests_catch2](#fetch_content_approvaltests_catch2)
  * [conan_cmake](#conan_cmake)
  * [conan_cmake_find_package](#conan_cmake_find_package)
  * [develop_approvaltests](#develop_approvaltests)<!-- endtoc -->

CMake code for various scenarios, for including in the ApprovalTests.cpp cmake docs, and for copying as templates for new projects.  

## add_subdirectory_approvaltests_catch2

 <!-- include: add_subdirectory_approvaltests_catch2. path: /add_subdirectory_approvaltests_catch2/mdsource/add_subdirectory_approvaltests_catch2.include.md -->
| Topic        | Detail                                                       |
| ------------ | ------------------------------------------------------------ |
| Directory    | [add_subdirectory_approvaltests_catch2](/add_subdirectory_approvaltests_catch2/)                        |
| Purpose      | Demo how to build your tests against clones or forks of ApprovalTests.cpp and Catch2.<br />Those source code of those dependencies will be included in your IDE, alongside your own source code.<br />This allows you to make edits to the dependent projects. |
| Dependencies | ApprovalTests.cpp - cloned on your machine<br />Catch2 - cloned on your machine |
| Mechanism    | Uses CMake's [`add_subdirectory()`](https://cmake.org/cmake/help/latest/command/add_subdirectory.html) |
 <!-- end include: add_subdirectory_approvaltests_catch2. path: /add_subdirectory_approvaltests_catch2/mdsource/add_subdirectory_approvaltests_catch2.include.md -->

## fetch_content_approvaltests

 <!-- include: fetch_content_approvaltests. path: /fetch_content_approvaltests/mdsource/fetch_content_approvaltests.include.md -->
| Topic        | Detail                                                       |
| ------------ | ------------------------------------------------------------ |
| Directory    | [fetch_content_approvaltests](/fetch_content_approvaltests/)                        |
| Purpose      | Demo how to build your tests using CMake's `FetchContent_Declare` and `FetchContent_MakeAvailable` to clone ApprovalTests.cpp, and use its copy of Catch2.<br />The source code of this dependency will be cloned inside your CMake build space, and will not be shown inside your IDE.<br />This requires at least CMake 3.14. |
| Dependencies | ApprovalTests.cpp - cloned automatically by CMake<br />Catch2 - the version in the pprovalTests.cpp repo will be used |
| Mechanism    | Uses CMake's [`FetchContent`](https://cmake.org/cmake/help/latest/module/FetchContent.html) module. |
 <!-- end include: fetch_content_approvaltests. path: /fetch_content_approvaltests/mdsource/fetch_content_approvaltests.include.md -->

## fetch_content_approvaltests_catch2

 <!-- include: fetch_content_approvaltests_catch2. path: /fetch_content_approvaltests_catch2/mdsource/fetch_content_approvaltests_catch2.include.md -->
| Topic        | Detail                                                       |
| ------------ | ------------------------------------------------------------ |
| Directory    | [fetch_content_approvaltests_catch2](/fetch_content_approvaltests_catch2/) |
| Purpose      | Demo how to build your tests using CMake's `FetchContent_Declare` and `FetchContent_MakeAvailable` to clone ApprovalTests.cpp and Catch2.<br />The source code of those dependencies will be cloned inside your CMake build space, and will not be shown inside your IDE.<br />This requires at least CMake 3.14. |
| Dependencies | ApprovalTests.cpp - cloned automatically by CMake<br />Catch2 - cloned automatically by CMake |
| Mechanism    | Uses CMake's [`FetchContent`](https://cmake.org/cmake/help/latest/module/FetchContent.html) module. |
 <!-- end include: fetch_content_approvaltests_catch2. path: /fetch_content_approvaltests_catch2/mdsource/fetch_content_approvaltests_catch2.include.md -->

## conan_cmake

 <!-- include: conan_cmake. path: /conan_cmake/mdsource/conan_cmake.include.md -->
**TODO** Update content of this table, for this director

| Topic        | Detail                                                       |
| ------------ | ------------------------------------------------------------ |
| Directory    | [conan_cmake](/conan_cmake/)                        |
| Purpose      | Demo how to build your tests against clones or forks of ApprovalTests.cpp and Catch2.<br />Those source code of those dependencies will be included in your IDE, alongside your own source code.<br />This allows you to make edits to the dependent projects. |
| Dependencies | ApprovalTests.cpp - cloned on your machine<br />Catch2 - cloned on your machine |
| Mechanism    | Uses CMake's [`add_subdirectory()`](https://cmake.org/cmake/help/latest/command/add_subdirectory.html) |
 <!-- end include: conan_cmake. path: /conan_cmake/mdsource/conan_cmake.include.md -->

## conan_cmake_find_package

 <!-- include: conan_cmake_find_package. path: /conan_cmake_find_package/mdsource/conan_cmake_find_package.include.md -->
**TODO** Update content of this table, for this director

| Topic        | Detail                                                       |
| ------------ | ------------------------------------------------------------ |
| Directory    | [conan_cmake_find_package](/conan_cmake_find_package/)                        |
| Purpose      | Demo how to build your tests against clones or forks of ApprovalTests.cpp and Catch2.<br />Those source code of those dependencies will be included in your IDE, alongside your own source code.<br />This allows you to make edits to the dependent projects. |
| Dependencies | ApprovalTests.cpp - cloned on your machine<br />Catch2 - cloned on your machine |
| Mechanism    | Uses CMake's [`add_subdirectory()`](https://cmake.org/cmake/help/latest/command/add_subdirectory.html) |
 <!-- end include: conan_cmake_find_package. path: /conan_cmake_find_package/mdsource/conan_cmake_find_package.include.md -->

## develop_approvaltests

 <!-- include: develop_approvaltests. path: /develop_approvaltests/mdsource/develop_approvaltests.include.md -->
**TODO** Update content of this table, for this director

| Topic        | Detail                                                       |
| ------------ | ------------------------------------------------------------ |
| Directory    | [develop_approvaltests](/develop_approvaltests/)                        |
| Purpose      | Demo how to build your tests against clones or forks of ApprovalTests.cpp and Catch2.<br />Those source code of those dependencies will be included in your IDE, alongside your own source code.<br />This allows you to make edits to the dependent projects. |
| Dependencies | ApprovalTests.cpp - cloned on your machine<br />Catch2 - cloned on your machine |
| Mechanism    | Uses CMake's [`add_subdirectory()`](https://cmake.org/cmake/help/latest/command/add_subdirectory.html) |
 <!-- end include: develop_approvaltests. path: /develop_approvaltests/mdsource/develop_approvaltests.include.md -->

