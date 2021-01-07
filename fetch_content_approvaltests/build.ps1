mkdir  -force build
Push-Location build

cmake -DCMAKE_BUILD_TYPE=Debug ..
cmake --build .
ctest --output-on-failure . -C Debug

Pop-Location
