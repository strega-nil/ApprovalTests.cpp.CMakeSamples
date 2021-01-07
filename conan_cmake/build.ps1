mkdir  -force build
Push-Location build

conan install ..
cmake -DCMAKE_BUILD_TYPE=Debug ..
cmake --build .
ctest --output-on-failure . -C Debug

Pop-Location
