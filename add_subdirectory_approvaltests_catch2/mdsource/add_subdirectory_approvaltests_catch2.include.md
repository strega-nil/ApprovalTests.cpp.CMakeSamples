
| Topic        | Detail                                                       |
| ------------ | ------------------------------------------------------------ |
| Directory    | [add_subdirectory_approvaltests_catch2](/add_subdirectory_approvaltests_catch2/) |
| Purpose      | Demo how to build your tests against clones or forks of ApprovalTests.cpp and Catch2.<br />Those source code of those dependencies will be included in your IDE, alongside your own source code.<br />This allows you to make edits to the dependent projects. |
| Dependencies | ApprovalTests.cpp - cloned on your machine<br />Catch2 - cloned on your machine |
| Mechanism    | Uses CMake's [`add_subdirectory()`](https://cmake.org/cmake/help/latest/command/add_subdirectory.html) |
| More Detail  | See [Use own ApprovalTests.cpp and Catch2 clones](https://github.com/approvals/ApprovalTests.cpp/blob/master/doc/CMakeIntegration.md#use-own-approvaltestscpp-and-catch2-clones) |

