from distutils.dir_util import copy_tree
import sys
import os

source_dir = os.path.dirname(__file__)
destination_dir = ""
for arg in sys.argv:
    if "[--src=" and "]" in arg:
        source_dir = arg.replace("]", "").split("=")[1]
    elif "--dst=" in arg:
        destination_dir = arg.split("=")[1]

print(source_dir)
print(destination_dir)
copy_tree(source_dir, destination_dir)
