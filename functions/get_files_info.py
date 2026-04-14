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
    dir_path = os.path.join(working_dir, dir)
    target_dir = os.path.normpath(dir_path)
    file_info_list = []

    for root, dirs, files in os.walk(dir_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_info = {
                "name": filename,
                "path": file_path,
                "size": os.path.getsize(file_path),
                "modified": os.path.getmtime(file_path),
            }
            file_info_list.append(file_info)

    return file_info_list