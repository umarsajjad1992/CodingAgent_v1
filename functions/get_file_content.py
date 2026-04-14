import os

from config import MAX_CONTEXT_SIZE

def get_file_content(working_dir, file_path):
    abs_working_dir = os.path.abspath(working_dir)
    abs_file_path = os.path.abspath(os.path.join(working_dir, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f"Error: Invalid file path: {file_path}. File must be within the working directory."
    if not os.path.isfile(abs_file_path):
        return f"Error: {file_path} is not a valid file."
    try:
        with open(abs_file_path, 'r') as file:
            content = file.read(MAX_CONTEXT_SIZE)
            if len(content) >= MAX_CONTEXT_SIZE:
                content += f"\n\n[Content truncated to {MAX_CONTEXT_SIZE} characters due to size limit]"
            return content
    except Exception as e:
        return f"Error reading file: {e}"
