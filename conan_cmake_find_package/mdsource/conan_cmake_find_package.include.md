
| Topic        | Detail                                                       |
| ------------ | ------------------------------------------------------------ |
| Directory    | [conan_cmake_find_package](/conan_cmake_find_package/)                        |
| Purpose      | Demo how to build your tests using Conan's `cmake_find_package` and optionally `cmake_paths` generators to download single headers for specific releases of ApprovalTests.cpp and Catch2.<br />The released headers of those dependencies will be downloaded inside your CMake build space, and will not be shown inside your IDE. |
| Dependencies | ApprovalTests.cpp - downloaded automatically by Conan<br/>Catch2 - downloaded automatically by Conan |
| Mechanism    | Uses Conan's [`cmake_find_package`](https://docs.conan.io/en/latest/integrations/build_system/cmake/cmake_find_package_generator.html) and (optionally) [`cmake_paths`](https://docs.conan.io/en/latest/integrations/build_system/cmake/cmake_paths_generator.html) generators.                              |
| More Detail  |                                                              |

