import os

data_dirs = ["processed", "raw"]


def clean_directory(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if str(file) != ".gitkeep":
                os.remove(os.path.join(root, file))


if __name__ == '__main__':
    for directory in data_dirs:
        clean_directory(directory)
