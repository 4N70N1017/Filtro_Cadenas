import os
import argparse

def search_for_string_in_files(directory, search_string, script_name):
    """
    Searches for a string in all files within a directory and its subdirectories.

    Args:
        directory (str): The path to the directory to search.
        search_string (str): The string to search for.
        script_name (str): The name of the script to exclude from the search.
    """
    print(f"Searching for '{search_string}' in '{directory}'...")
    found_occurrences = False
    for root, _, files in os.walk(directory):
        for file in files:
            if file == script_name:
                continue
            if file.lower().endswith('.bal'):
                continue
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    for line_num, line in enumerate(f, 1):
                        if search_string in line:
                            if not found_occurrences:
                                found_occurrences = True
                            print(f"\nFound in: {file_path} (Line: {line_num})")
                            print(f"  -> {line.strip()}")
            except Exception as e:
                pass

    if not found_occurrences:
        print(f"\nNo occurrences of '{search_string}' found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search for a string in files.")
    parser.add_argument("directory", nargs='?', default='.', help="The directory to search in. Defaults to the current directory.")
    parser.add_argument("-s", "--string", default="he.exe", help="The string to search for. Defaults to 'he.exe'.")
    args = parser.parse_args()

    script_name = os.path.basename(__file__)

    search_for_string_in_files(args.directory, args.string, script_name)
