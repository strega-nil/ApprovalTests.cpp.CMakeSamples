
| Topic        | Detail                                                       |
| ------------ | ------------------------------------------------------------ |
| Directory    | [fetch_content_approvaltests](/fetch_content_approvaltests/)                        |
| Purpose      | Demo how to build your tests using CMake's `FetchContent_Declare` and `FetchContent_MakeAvailable` to clone ApprovalTests.cpp, and use its copy of Catch2.<br />The source code of this dependency will be cloned inside your CMake build space, and will not be shown inside your IDE.<br />This requires at least CMake 3.14. |
| Dependencies | ApprovalTests.cpp - cloned automatically by CMake<br />Catch2 - the version in the pprovalTests.cpp repo will be used |
| Mechanism    | Uses CMake's [`FetchContent`](https://cmake.org/cmake/help/latest/module/FetchContent.html) module. |

