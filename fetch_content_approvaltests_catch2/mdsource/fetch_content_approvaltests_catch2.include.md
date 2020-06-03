
| Topic        | Detail                                                       |
| ------------ | ------------------------------------------------------------ |
| Directory    | [fetch_content_approvaltests_catch2](/fetch_content_approvaltests_catch2/) |
| Purpose      | Demo how to build your tests using CMake's `FetchContent_Declare` and `FetchContent_MakeAvailable` to clone ApprovalTests.cpp and Catch2.<br />The source code of those dependencies will be cloned inside your CMake build space, and will not be shown inside your IDE.<br />This requires at least CMake 3.14. |
| Dependencies | ApprovalTests.cpp - cloned automatically by CMake<br />Catch2 - cloned automatically by CMake |
| Mechanism    | Uses CMake's [`FetchContent`](https://cmake.org/cmake/help/latest/module/FetchContent.html) module. |

