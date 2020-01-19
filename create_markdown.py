#!/usr/bin/env python3

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
    # print(file)
    if os.path.splitext(file)[1] == '.cmake':
        return True
    if file == 'CMakeLists.txt':
        return True
    return False


def show_for_markdown(root, file):
    rel_path = os.path.join(root, file)
    abs_path = os.path.abspath(rel_path)

    path = root.split(os.sep)
    # print((len(path) - 1) * '---', os.path.basename(root))

    print(f'{(len(path) + 2) * "#"} {rel_path}')
    print('\n')
    print(f"<!-- {abs_path} -->")
    print('\n')
    print('```cmake')
    with open(abs_path) as f:
        print(f'{"".join(f.readlines())}```')
    print('\n')


# traverse root directory, and list directories as dirs and files as files
print('# CMake files')
print('\n')
for root, dirs, files in os.walk(".", topdown=True):
    dirs[:] = remove_unwanted_dirs(dirs)
    #path = root.split(os.sep)
    # print((len(path) - 1) * '---', os.path.basename(root))
    for file in files:
        if not is_wanted_file(file):
            continue
        # print(len(path) * '---', file)
        # print(is_wanted_file(file))
        show_for_markdown(root, file)
