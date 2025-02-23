import os
import json
import glob
import logging

logging.basicConfig(
    filename = "app.log",
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    datefmt = "%Y-%m-%d %H:%M:%S"
)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
logging.getLogger().addHandler(console_handler)

class FileManager:
    """
    A class to manage file operations such as generating filenames and saving JSON data.
    This class helps in organizing and managing files within a specified directory.
    """

    def __init__(self, 
                directory = f"{os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data")}", 
                filename_prefix = "recently_played", file_extension = "json"):
        """
        Initializes the FileManager with directory, filename prefix, and file extension.

        :param directory: The directory where files will be saved. Default is "data/".
        :param filename_prefix: The prefix used for naming files. Default is "recently_played".
        :param file_extension: The file extension (type). Default is "json".
        """
        self.dir = directory
        self.file_prefix = filename_prefix
        self.file_type = file_extension

        os.makedirs(self.dir, exist_ok = True) 
        
        logging.info(f"FileManager Initialised with directory {self.dir}")

    def get_file_name(self):
        """
        Generates a unique filename based on the existing files in the directory.

        :return: A new filename with an incremented count to avoid overwriting existing files.
        """
        json_files = glob.glob(f"{os.path.join(self.dir, self.file_prefix)}*.{self.file_type}")
        count = len(json_files) + 1
        filename = f"{os.path.join(self.dir, self.file_prefix)}{count}.{self.file_type}"
        
        logging.info(f"Generated filename {filename}")

        return filename
        
    def save_file(self, recently_played):
        """
        Saves the given data (recently played tracks) into a JSON file.

        :param recently_played: The data to be saved, typically a dictionary or list.
        """
        try:
            filepath = self.get_file_name()
            with open(filepath, "w") as file:
                json.dump(recently_played, file, indent = 4)

            logging.info(f"File {filepath} saved successfully!")
        except Exception as e:
            logging.error(f"Error saving file: {e}")


# data = {
#     "greeting": "Hello World"
# }

# newFile = FileManager()
# print(newFile.get_file_name())
# newFile.save_file(data)