
| Topic        | Detail                                                       |
| ------------ | ------------------------------------------------------------ |
| Directory    | [dev_approvals_fetch_content](/dev_approvals_fetch_content/)                        |
| Purpose      | Demo how to build the ApprovalTests.cpp project using CMake's `FetchContent_Declare` and `FetchContent_MakeAvailable` to clone its dependencies.<br />The source code of the dependencies will be cloned inside your CMake build space, and will not be shown inside your IDE.<br />This requires at least CMake 3.14. |
| Dependencies | ApprovalTests.cpp - cloned on your machine<br />All its dependencies also cloned on your machine, inside each build space |
| Mechanism    | Uses CMake's [`FetchContent`](https://cmake.org/cmake/help/latest/module/FetchContent.html) module. |
| More Detail  |  |

