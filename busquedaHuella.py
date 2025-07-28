import os
import argparse
import json

def search_for_string_in_files(directory, search_string, script_name):
    """
    Searches for a string in all files within a directory and its subdirectories.
    Returns a list of dictionaries with results.
    """
    print(f"Searching for '{search_string}' in '{directory}'...")
    results = []
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
                            results.append({
                                "file": file_path,
                                "line": line_num,
                                "content": line.strip()
                            })
            except Exception as e:
                pass

    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search for a string in files.")
    parser.add_argument("directory", nargs='?', default='.', help="The directory to search in. Defaults to the current directory.")
    parser.add_argument("-s", "--string", default="he.exe", help="The string to search for. Defaults to 'he.exe'.")
    parser.add_argument("-o", "--output", default="resultados.json", help="Output JSON file name.")
    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, args.output)

    script_name = os.path.basename(__file__)

    results = search_for_string_in_files(args.directory, args.string, script_name)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(json.dumps(results, ensure_ascii=False, indent=2))