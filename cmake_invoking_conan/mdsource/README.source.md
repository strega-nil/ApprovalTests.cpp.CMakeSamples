# cmake_invoking_conan

include: cmake_invoking_conan

The conanfile.txt file is:

include: inc_cmake_invoking_conan_conanfile

There is a CMake file called `CMake/Conan.cmake` which contains instructions for downloading a specific version of the cmake-conan CMake module:

include: inc_cmake_invoking_conan_CMake_conan
 
The top-level CMakeLists.txt file includes the above `CMake/Conan.cmake` file, and runs the macro that it contained:

include: inc_cmake_invoking_conan_cmakelists

And the CMakeLists.txt that builds the tests is:

include: inc_cmake_invoking_conan_tests_cmakelists

The build script is:

include: inc_cmake_invoking_conan_build
