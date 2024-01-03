import json
import os
import shutil
__all__ = [
    "does_file_exist",
    "does_dir_exist",
    "create_dir",
    "create_dirs_for",
    "load_text_file",
    "load_json_file",
    "save_text_file",
    "save_json_file",
    "list_files_in_dir",
    "get_extension",
    "is_file_image",
    "is_file_format",
    "remove_extension",
    "get_directory",
    "get_basename",
    "join_paths",
    "change_extension",
    "generate_next_file_name_path",
    "parse_json",
    "remove_file",
    "remove_dir",
    "rename_file",
    "copy_file",
]

def does_file_exist(file_path : str) -> bool:
    """
    Check if a file exists at the given file path.

    Parameters:
        file_path (str): The path of the file to be checked.

    Returns:
        bool: True if the file exists and is a regular file, False otherwise.
    """
    if os.path.exists(file_path):
        return os.path.isfile(file_path)
    return False

def does_dir_exist(dir_path : str) -> bool:
    """
    Check if a directory exists.

    Parameters:
        dir_path (str): The path of the directory to check.

    Returns:
        bool: True if the directory exists, False otherwise.
    """
    if os.path.exists(dir_path):
        return os.path.isdir(dir_path)
    return False

def create_dir(dir_path : str) -> str:
    """
    Creates a directory at the specified path if it does not already exist.

    Parameters:
        dir_path (str): The path of the directory to be created.

    Returns:
        str: The path of the created directory.
    """
    if not does_dir_exist(dir_path):
        os.makedirs(dir_path)
    else:
        pass
        #print(f"Directory already exists : {dir_path}")
    return dir_path

def create_dirs_for(path:str):
    create_dir(get_directory(path))

def load_text_file(file_path: str) -> str:
    """
    Load the contents of a text file.

    Args:
        file_path (str): The path to the text file.

    Returns:
        str: The contents of the text file.
    """
    with open(file_path, encoding='utf-8') as file:
        return file.read()

def load_json_file(file_path : str) -> str:
    """
    Load and parse a JSON file.

    Parameters:
        file_path (str): The path to the JSON file.

    Returns:
        str: The parsed JSON data.

    """
    if get_extension(file_path) != ".json":
        raise TypeError("File extension must be .json!")
    return json.load(open(file_path))

def save_text_file(file_path : str, text : str) -> str:
    """
    Saves the given text to a file at the specified file path.

    Parameters:
        file_path (str): The path to the file where the text will be saved.
        text (str): The text to be saved to the file.

    Returns:
        str: The file path where the text was saved.
    """
    create_dir(get_directory(dir_path=file_path))
    file_path = _add_extension_if_not_exists(file_path, ".txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)
    return file_path

def save_json_file(file_path : str, data) -> str:
    """
    Saves data as a JSON file.
    Creates the directory if it doesn't exist.

    Args:
        file_path (str): The path to the file where the JSON data will be saved.
        data: The data to be saved as a JSON file.

    Returns:
        str: The path of the saved JSON file.
    """
    create_dir(get_directory(dir_path=file_path))
    file_path = _add_extension_if_not_exists(file_path, ".json")
    with open(file_path, "w") as f:
        json.dump(data, f)
    return file_path

def list_files_in_dir(dir_path : str, show_directories : bool = True, show_files : bool = True, only_with_extensions = None, absolute:bool=False) -> list:
    """
        Lists files in a directory.

        Parameters:
        - dir_path (str): The path to the directory.
        - show_directories (bool): Whether to include directories in the list. Default is True.
        - show_files (bool): Whether to include files in the list. Default is True.
        - specific_extensions (list): A list of specific file extensions to filter the files. Default is None.

        Returns:
        - list: A list of files in the directory that meet the specified criteria.
    """
    files = []
    if os.path.isdir(dir_path):
        if show_directories and show_files:
            files = os.listdir(dir_path)
        elif show_directories or show_files:
            for file in os.listdir(dir_path):
                if show_directories:
                    if os.path.isdir(os.path.join(dir_path, file)):
                        files.append(file)
                if show_files:
                    if os.path.isfile(os.path.join(dir_path, file)):
                        if only_with_extensions:
                            state = False 
                            for ext in only_with_extensions:
                                if file.endswith(ext):
                                    state = True
                            if not state:
                                continue
                        if absolute:
                            files.append(join_paths(dir_path, file))
                        else:
                            files.append(file)
        else:
            print("Didn't select to show directories or files!")
            raise ValueError("Didn't select to show directories or files, at least on of the paramaters must be true")         
    else:
        print(f"Directory doesn't exist : {dir_path}")
        raise ValueError(f"Directory doesn't exist : {dir_path}")
    return files

def get_extension(file_path : str) -> str:
    """
    Get the extension of a file.

    Args:
        file_path (str): The path of the file.

    Returns:
        str: The extension of the file. If the file path does not have an extension, None is returned.
    """
    ext = os.path.splitext(file_path)[1]
    if "." in ext:
        ext = ext
    else:
        ext = None
    return ext

def is_file_image(file_path:str, supported_extensions:list=None):
    if supported_extensions is None:
        supported_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.ico', '.svg', '.svgz', '.bmp', '.tiff', '.tif']
    else:
        for i in range(len(supported_extensions)):
            if "." in supported_extensions[i]:
                supported_extensions[i] = supported_extensions[i]
            else:
                supported_extensions[i] = f".{supported_extensions[i]}"
    ext = get_extension(file_path)
    return True if ext in supported_extensions else False

def is_file_format(file_path:str, supported_extensions:list=None):
    if isinstance(supported_extensions, str):
        supported_extensions = [supported_extensions]
    for ext in supported_extensions:
        if "." in ext:
            ext = ext
        else:
            ext = f".{ext}"
        if file_path.endswith(ext):
            return True
    return False

def remove_extension(file_path : str) -> str:
    """
    Removes the file extension from the given file path.

    Args:
        file_path (str): The path of the file.

    Returns:
        str: The file path without the extension.
    """
    if(get_extension(file_path) is not None):
        return os.path.splitext(file_path)[0]
    else:
        return file_path

def get_directory(dir_path : str) -> str:
    """
    Get the directory path.

    Args:
        dir_path (str): The path of the directory.

    Returns:
        str: The directory path if it exists, otherwise the parent directory path.
    """
    return os.path.dirname(dir_path)
    
def get_basename(file_path):
    return os.path.basename(file_path)


def _add_extension_if_not_exists(file_path : str, extension : str) -> str:
    """
    Adds an extension to a file path if it doesn't already have one.

    Args:
        file_path (str): The file path.
        extension (str): The extension to add.

    Returns:
        str: The file path with the added extension.
    """
    if "." in extension:
        extension = extension
    else:
        extension = f".{extension}"
    if get_extension(file_path) is None:
        return f"{file_path}{extension}"
    else:
        return file_path

def join_paths(*path_parts: str) -> str:
    return os.path.join(*path_parts)

def change_extension(file_path : str, new_extension : str) -> str:
    """
    Changes the extension of a file path.

    Args:
        file_path (str): The file path.
        new_extension (str): The new extension.

    Returns:
        str: The file path with the new extension.
    """
    if not "." in new_extension:
        new_extension = f".{new_extension}"
    return remove_extension(file_path) + new_extension

def generate_next_file_name_path(save_dir:str, _prefix:str="", _postfix:str="", _extension:str=""):
    """
    Generates the next available file name path in the specified directory.
    Use this to avoid overwriting files and to generate unique file names on the fly for variable number of files.

    Args:
        save_dir (str): The directory where the file will be saved.
        _postfix (str, optional): The postfix to be added to the file name. Defaults to "".
        _prefix (str, optional): The prefix to be added to the file name. Defaults to "".
        Example: generate_next_file_name_path("C:/Users/Me/Desktop", _prefix="file_", _postfix="", _extension=".txt") -> C:/Users/Me/Desktop/file_0.txt 

    Returns:
        str: The next available file name path.
    """
    create_dir(save_dir)
    file_num = 0
    while True:
        n = f"{_prefix}{file_num}{_postfix}{_extension}"
        n = join_paths(save_dir, n)
        if does_file_exist(n):
            file_num += 1
        else:
            break
    return n

def parse_json(json_string):
    return json.loads(json_string)

def remove_file(file_path):
    if does_file_exist(file_path):
        os.remove(file_path)

def remove_dir(dir_path, with_contents=True, recursive=True):
    if does_dir_exist(dir_path):
        if with_contents:
            if recursive:
                import shutil
                shutil.rmtree(dir_path)
            else:
                os.rmdir(dir_path)
        else:
            os.rmdir(dir_path)

def rename_file(file_path, new_name):
    if does_file_exist(file_path):
        os.rename(file_path, new_name)


def copy_file(file_path, new_path):
    if does_file_exist(file_path):
        shutil.copy(file_path, new_path)
        return new_path
    else:
        raise ValueError(f"File {file_path} doesn't exist!")



