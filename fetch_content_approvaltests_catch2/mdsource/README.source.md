# fetch_content_approvaltests_catch2

include: fetch_content_approvaltests_catch2

The top-level CMakeLists.txt file is:

include: inc_fetch_content_approvaltests_catch2_cmakelists

The CMakeLists.txt to pull in dependencies is as follows: note that you can quote tags, branch names or commit IDs to control the exact version to be used:

include: inc_fetch_content_approvaltests_catch2_dependencies_cmakelists

And the CMakeLists.txt that builds the tests is:

include: inc_fetch_content_approvaltests_catch2_tests_cmakelists
