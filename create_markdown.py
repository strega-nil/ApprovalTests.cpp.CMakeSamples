#!/usr/bin/env python3

# traverse directory, and convert cmake files to include files for
# use in ApprovalTests.cpp documentation

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

    path = root.split(os.sep)

    print(f'{(len(path) + 1) * "#"} {rel_path}')
    print('\n')
    print(f"<!-- {abs_path} -->")
    print('\n')
    print('```cmake')
    with open(abs_path) as f:
        print(f'{"".join(f.readlines())}```')
    print('\n')


for root, dirs, files in os.walk(".", topdown=True):
    dirs[:] = remove_unwanted_dirs(dirs)
    for file in files:
        if not is_wanted_file(file):
            continue
        show_for_markdown(root, file)
