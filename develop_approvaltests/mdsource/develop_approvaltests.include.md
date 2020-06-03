
**TODO** Update content of this table, for this director

| Topic        | Detail                                                       |
| ------------ | ------------------------------------------------------------ |
| Directory    | [develop_approvaltests](/develop_approvaltests/)                        |
| Purpose      | Demo how to build your tests against clones or forks of ApprovalTests.cpp and Catch2.<br />Those source code of those dependencies will be included in your IDE, alongside your own source code.<br />This allows you to make edits to the dependent projects. |
| Dependencies | ApprovalTests.cpp - cloned on your machine<br />Catch2 - cloned on your machine |
| Mechanism    | Uses CMake's [`add_subdirectory()`](https://cmake.org/cmake/help/latest/command/add_subdirectory.html) |

