#!/usr/bin/env python3

# traverse directory, and convert cmake files to include files for
# use in ApprovalTests.cpp documentation
#
# The CMake files in this directory are intended for inclusion in 
# ApprovalTests.cpp documentation.
# 
# Currently there is no way to use mdsnippets to pull
# in files from other repos.
# 
# So for now, I'm copying these CMake files on to that
# repo, converted to Markdown format, for inclusion
# in the documentation there.

import os

def remove_unwanted_dirs(dirs):
    kept_dirs = []
    excluded = ['.git', '.idea']
    for dir in dirs:
        if dir.startswith('cmake-build'):
            continue
        if dir in excluded:
            continue
        kept_dirs.append(dir)
    return kept_dirs


def is_wanted_file(file):
    if os.path.splitext(file)[1] == '.cmake':
        return True
    if file == 'CMakeLists.txt':
        return True
    return False


def show_for_markdown(root, file):
    rel_path = os.path.join(root, file)
    abs_path = os.path.abspath(rel_path)

    dir_name = os.path.normpath(root).replace('/', '_')
    file_base_name = os.path.splitext(file)[0]
    output_file = f'../ApprovalTests.cpp/doc/mdsource/inc_{dir_name}_{file_base_name.lower()}.include.md'
    print(output_file)
    with open(output_file, 'w') as s:
        s.write('\n')
        s.write('\n')
        s.write('```cmake\n')
        with open(abs_path) as f:
            s.write(f'{"".join(f.readlines())}```')
        s.write('\n')


for root, dirs, files in os.walk(".", topdown=True):
    dirs[:] = remove_unwanted_dirs(dirs)
    for file in files:
        if not is_wanted_file(file):
            continue
        show_for_markdown(root, file)
