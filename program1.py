import sys

import os


file_path = sys.argv[1]


does_file_exist = os.path.exists(file_path)

print(does_file_exist)
