import os

def get_files_info(working_dir, dir="."):
    """
    Get information about files in the specified directory.

    Args:
        working_dir (str): The base working directory.
        dir (str): The directory to list files from, relative to the working directory.

    Returns:
        list: A list of file information dictionaries.
    """
    working_dir_abs = os.path.abspath(working_dir)
    dir_path = os.path.join(working_dir_abs, dir)
    target_dir = os.path.normpath(dir_path)

    
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    if not valid_target_dir:
        raise ValueError(f"Invalid directory: {dir}. Directory must be within the working directory.")
    
    contents = os.listdir(target_dir)
    print(contents)
    item_info = ""
    for item in contents:
        item_path = os.path.join(target_dir, item)
        isdir = os.path.isdir(item_path)
        size = os.path.getsize(item_path)
        item_info += f"- {item}: file_size={size} bytes, is_directory={isdir}\n"

    return item_info