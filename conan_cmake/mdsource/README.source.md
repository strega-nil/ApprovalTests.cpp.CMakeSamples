# conan_cmake

include: conan_cmake

The top-level CMakeLists.txt file is:

include: inc_conan_cmake_cmakelists

<!--
The CMakeLists.txt to pull in dependencies is:

include: inc_conan_cmake_dependencies_cmakelists
-->

And the CMakeLists.txt that builds the tests is:

include: inc_conan_cmake_tests_cmakelists
