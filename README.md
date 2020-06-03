# ApprovalTests.cpp.CMakeSamples

CMake code for various scenarios, for including in the ApprovalTests.cpp cmake docs, and for copying as templates for new projects.  

| Directory                                                    | Purpose                                                      | Dependencies | Mechanism                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------ | ------------------------------------------------------------ |
| [add_subdirectory_approvaltests_catch2](/add_subdirectory_approvaltests_catch2/) | Demo how to build your tests against clones or forks of ApprovalTests.cpp and Catch2.<br />Those source code of those dependencies will be included in your IDE, alongside your own source code. |              | Uses CMake's [`add_subdirectory()`](https://cmake.org/cmake/help/latest/command/add_subdirectory.html) |
| [fetch_content_approvaltests](/fetch_content_approvaltests/) |                                                              |              |                                                              |
| [fetch_content_approvaltests_catch2](/fetch_content_approvaltests_catch2/) |                                                              |              |                                                              |
| [conan_cmake](/conan_cmake/)                                 |                                                              |              |                                                              |
| [conan_cmake_find_package](/conan_cmake_find_package/)       |                                                              |              |                                                              |
| [develop_approvaltests](/develop_approvaltests/)             |                                                              |              |                                                              |

