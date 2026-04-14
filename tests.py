from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def main():
    working_dir = "calculator"
    dir = "."

    print("Testing get_files_info with valid and invalid file paths\n")
    files_info = get_files_info(working_dir, dir)
    print(files_info)
    files_info = get_files_info(working_dir, "pkg")
    print(files_info)
    files_info = get_files_info(working_dir, "/bin")
    print(files_info)
    files_info = get_files_info(working_dir, "../")
    print(files_info)

    print("\nTesting get_file_content\n")
    working_dir = "calculator"
    print(get_file_content(working_dir, "lorem.txt"))
    print(get_file_content(working_dir, "main.py"))
    print(get_file_content(working_dir, "pkg/calculator.py"))
    print(get_file_content(working_dir, "pkg/tests.py"))
    print(get_file_content(working_dir, "../main.py"))
    print(get_file_content(working_dir, "/bin/bash"))

main()