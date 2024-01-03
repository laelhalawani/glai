Module glai.helpers.file_handler
================================

Functions
---------

    
`change_extension(file_path: str, new_extension: str) ‑> str`
:   Changes the extension of a file path.
    
    Args:
        file_path (str): The file path.
        new_extension (str): The new extension.
    
    Returns:
        str: The file path with the new extension.

    
`copy_file(file_path, new_path)`
:   

    
`create_dir(dir_path: str) ‑> str`
:   Creates a directory at the specified path if it does not already exist.
    
    Parameters:
        dir_path (str): The path of the directory to be created.
    
    Returns:
        str: The path of the created directory.

    
`create_dirs_for(path: str)`
:   

    
`does_dir_exist(dir_path: str) ‑> bool`
:   Check if a directory exists.
    
    Parameters:
        dir_path (str): The path of the directory to check.
    
    Returns:
        bool: True if the directory exists, False otherwise.

    
`does_file_exist(file_path: str) ‑> bool`
:   Check if a file exists at the given file path.
    
    Parameters:
        file_path (str): The path of the file to be checked.
    
    Returns:
        bool: True if the file exists and is a regular file, False otherwise.

    
`generate_next_file_name_path(save_dir: str)`
:   Generates the next available file name path in the specified directory.
    Use this to avoid overwriting files and to generate unique file names on the fly for variable number of files.
    
    Args:
        save_dir (str): The directory where the file will be saved.
        _postfix (str, optional): The postfix to be added to the file name. Defaults to "".
        _prefix (str, optional): The prefix to be added to the file name. Defaults to "".
        Example: generate_next_file_name_path("C:/Users/Me/Desktop", _prefix="file_", _postfix="", _extension=".txt") -> C:/Users/Me/Desktop/file_0.txt 
    
    Returns:
        str: The next available file name path.

    
`get_basename(file_path)`
:   

    
`get_directory(dir_path: str) ‑> str`
:   Get the directory path.
    
    Args:
        dir_path (str): The path of the directory.
    
    Returns:
        str: The directory path if it exists, otherwise the parent directory path.

    
`get_extension(file_path: str) ‑> str`
:   Get the extension of a file.
    
    Args:
        file_path (str): The path of the file.
    
    Returns:
        str: The extension of the file. If the file path does not have an extension, None is returned.

    
`is_file_format(file_path: str, supported_extensions: list = None)`
:   

    
`is_file_image(file_path: str, supported_extensions: list = None)`
:   

    
`join_paths(*path_parts: str) ‑> str`
:   

    
`list_files_in_dir(dir_path: str, show_directories: bool = True, show_files: bool = True, only_with_extensions=None, absolute: bool = False) ‑> list`
:   Lists files in a directory.
    
    Parameters:
    - dir_path (str): The path to the directory.
    - show_directories (bool): Whether to include directories in the list. Default is True.
    - show_files (bool): Whether to include files in the list. Default is True.
    - specific_extensions (list): A list of specific file extensions to filter the files. Default is None.
    
    Returns:
    - list: A list of files in the directory that meet the specified criteria.

    
`load_json_file(file_path: str) ‑> str`
:   Load and parse a JSON file.
    
    Parameters:
        file_path (str): The path to the JSON file.
    
    Returns:
        str: The parsed JSON data.

    
`load_text_file(file_path: str) ‑> str`
:   Load the contents of a text file.
    
    Args:
        file_path (str): The path to the text file.
    
    Returns:
        str: The contents of the text file.

    
`parse_json(json_string)`
:   

    
`remove_dir(dir_path, with_contents=True, recursive=True)`
:   

    
`remove_extension(file_path: str) ‑> str`
:   Removes the file extension from the given file path.
    
    Args:
        file_path (str): The path of the file.
    
    Returns:
        str: The file path without the extension.

    
`remove_file(file_path)`
:   

    
`rename_file(file_path, new_name)`
:   

    
`save_json_file(file_path: str, data) ‑> str`
:   Saves data as a JSON file.
    Creates the directory if it doesn't exist.
    
    Args:
        file_path (str): The path to the file where the JSON data will be saved.
        data: The data to be saved as a JSON file.
    
    Returns:
        str: The path of the saved JSON file.

    
`save_text_file(file_path: str, text: str) ‑> str`
:   Saves the given text to a file at the specified file path.
    
    Parameters:
        file_path (str): The path to the file where the text will be saved.
        text (str): The text to be saved to the file.
    
    Returns:
        str: The file path where the text was saved.