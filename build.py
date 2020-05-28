#!/usr/bin/env python3

import os
import subprocess

ignored_paths = ['.git', '.idea']

for dir in os.listdir(os.getcwd()):
    if not os.path.isdir(dir):
        continue
    if os.path.islink(dir):
        continue
    if dir in ignored_paths:
        continue
    print('==============================', dir)
    os.chdir(dir)

    success = True
    try:
        output = subprocess.check_output(['./build.sh'])
    except subprocess.CalledProcessError as e:
        output = e.output
        success = False

    print(output.decode())
    if not success:
        print(F"ERROR {dir} build failed")
        exit(1)

    os.chdir('..')

print(F"Success!")
