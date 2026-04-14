from functions.get_files_info import get_files_info

def main():
    working_dir = "calculator"
    dir = "pkg"
    files_info = get_files_info(working_dir, dir)
    print(files_info)

main()