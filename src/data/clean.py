import os
data_dirs = ["processed", "raw"]

def clean_directory(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if str(file) != ".gitkeep":
                os.remove(os.path.join(root, file))

for directory in data_dirs:
    clean_directory(directory)