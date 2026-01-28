#!/usr/bin/env python3

import subprocess

def free_space():
    cmd = "df -h | grep '/$' | awk '{print $4}'"
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8').strip()

if __name__ == "__main__":
    print(free_space(), end="")

