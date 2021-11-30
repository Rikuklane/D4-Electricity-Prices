import os


class DataDeleter:

    @staticmethod
    def clean_directory(path: str):
        """
        Method that cleans up the directory specified in the path
        :param path: the path of the directory
        """
        for root, dirs, files in os.walk(path):
            for file in files:
                if str(file) != ".gitkeep":
                    os.remove(os.path.join(root, file))

    def clean_data(self):
        """
        Method that cleans all files in the given directories
        """
        data_dirs = [os.path.join("data", "raw"), os.path.join("data", "processed")]
        for directory in data_dirs:
            self.clean_directory(directory)


if __name__ == '__main__':
    os.chdir("..")
    DataDeleter().clean_data()
