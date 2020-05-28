add_executable(tests
        main.cpp
        tests.cpp
)
target_link_libraries(
        tests
        CONAN_PKG::approvaltests.cpp
        CONAN_PKG::catch2)

target_compile_features(tests PUBLIC cxx_std_11)
set_target_properties(tests PROPERTIES CXX_EXTENSIONS OFF)

add_test(
        NAME tests
        COMMAND tests)
