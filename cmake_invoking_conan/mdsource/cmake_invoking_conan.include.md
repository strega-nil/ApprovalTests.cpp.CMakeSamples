
| Topic        | Detail                                                       |
| ------------ | ------------------------------------------------------------ |
| Directory    | [cmake_invoking_conan](/cmake_invoking_conan/)                                 |
| Purpose      | Demo how to build your tests by getting CMake to invoke Conan, to download single headers for specific releases of ApprovalTests.cpp and Catch2.<br />The released headers of those dependencies will be downloaded inside your CMake build space, and will not be shown inside your IDE. |
| Dependencies | ApprovalTests.cpp - downloaded automatically by CMake invoking Conan<br/>Catch2 - downloaded automatically by CMake invoking Conan |
| Mechanism    | Uses the [cmake-conan](https://github.com/conan-io/cmake-conan) CMake module to invoke Conan automatically from within CMake.                              |
| More Detail  |                                                              |

