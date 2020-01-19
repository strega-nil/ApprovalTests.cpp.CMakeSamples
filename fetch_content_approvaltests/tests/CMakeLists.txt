add_executable(tests
        main.cpp
        tests.cpp
)
target_link_libraries(tests ApprovalTests::ApprovalTests Catch2::Catch2)

set_target_properties(tests PROPERTIES
        CXX_STANDARD 11
        CXX_STANDARD_REQUIRED YES
        CXX_EXTENSIONS NO
)

add_test(
        NAME tests
        COMMAND tests)
