import os


class DataDeleter:

    @staticmethod
    def clean_directory(path):
        """
        Method that cleans up the directory specified in the path
        :param path: the path of the directory
        """
        for root, dirs, files in os.walk(path):
            for file in files:
                if str(file) != ".gitkeep":
                    os.remove(os.path.join(root, file))

    @staticmethod
    def clean_data():
        """
        Method that cleans all files in the directories "processed" and "raw"
        """
        # TODO might have to use os.path.join for different operating systems
        data_dirs = ["data/processed", "data/raw"]
        for directory in data_dirs:
            DataDeleter.clean_directory(directory)


if __name__ == '__main__':
    os.chdir("..")
    DataDeleter.clean_data()
