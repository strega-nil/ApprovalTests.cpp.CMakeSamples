# Needs CMake 3.14 or above
include(FetchContent)

# -------------------------------------------------------------------
message(NOTICE "Fetching Boost...")
FetchContent_Declare(
        Boost
        URL https://dl.bintray.com/boostorg/release/1.74.0/source/boost_1_74_0.tar.gz
)
FetchContent_MakeAvailable(Boost)
# This is needed because there is not a CMakeLists.txt in the Boost download,
# so we have to teach find_package() to find Boost
set(BOOST_ROOT ${boost_SOURCE_DIR} PARENT_SCOPE)

# -------------------------------------------------------------------
message(NOTICE "Fetching Catch2...")
FetchContent_Declare(Catch2
        GIT_REPOSITORY https://github.com/catchorg/Catch2.git
        GIT_TAG v2.11.1)
FetchContent_MakeAvailable(Catch2)

# -------------------------------------------------------------------
message(NOTICE "Fetching cpputest...")
FetchContent_Declare(cpputest
        GIT_REPOSITORY https://github.com/cpputest/cpputest.git
        GIT_TAG v4.0)
FetchContent_MakeAvailable(cpputest)

# -------------------------------------------------------------------
message(NOTICE "Fetching doctest...")
FetchContent_Declare(
        doctest
        GIT_REPOSITORY  https://github.com/onqtam/doctest
        GIT_TAG         2.4.0
)
FetchContent_MakeAvailable(doctest)
set_target_properties(doctest_with_main PROPERTIES FOLDER "external")

# -------------------------------------------------------------------
message(NOTICE "Fetching fmt...")
FetchContent_Declare(fmt
        GIT_REPOSITORY https://github.com/fmtlib/fmt.git
        GIT_TAG 6.2.0)
FetchContent_MakeAvailable(fmt)

# -------------------------------------------------------------------
message(NOTICE "Fetching googletest...")
FetchContent_Declare(googletest
        GIT_REPOSITORY https://github.com/abseil/googletest.git
        GIT_TAG release-1.8.1)
FetchContent_MakeAvailable(googletest)

# -------------------------------------------------------------------
