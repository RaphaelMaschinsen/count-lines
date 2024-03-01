import os
import sys


def count_lines_of_code_in_directories(directories, excluded_formats=None):
    """
    Counts the lines of code in each file within the specified directories,
    excluding files with specified formats, and including all subdirectories.
    """
    if excluded_formats is None:
        excluded_formats = []
    line_counts = {}
    folder_counts = {}

    for directory in directories:
        if not os.path.isdir(directory):
            print(f"Skipping non-directory: {directory}")
            continue
        for root, dirs, files in os.walk(directory):
            folder_line_count = 0
            for file in files:
                if any(file.endswith(ext) for ext in excluded_formats):
                    continue

                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        count = len(lines)
                        line_counts[file_path] = count
                        folder_line_count += count
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
            if folder_line_count > 0:
                folder_counts[root] = folder_counts.get(root, 0) + folder_line_count

    return line_counts, folder_counts


def print_line_counts(line_counts, folder_counts):
    """
    Prints the lines of code count for each file, each folder, and the total lines.
    """
    total_lines = 0
    print("\nLines of code by folder:")
    for folder, count in folder_counts.items():
        print(f"{folder}: {count} lines")

    print("\nLines of code by file:")
    for file, count in line_counts.items():
        print(f"{file}: {count} lines")
        total_lines += count

    print(f"\nTotal lines of code: {total_lines}")


if __name__ == "__main__":
    excluded_file_endings = []
    directories_to_analyze = sys.argv[1:]  # Assumes all arguments are directories unless '--exclude' is found

    if "--exclude" in sys.argv:
        exclude_index = sys.argv.index("--exclude")
        directories_to_analyze = sys.argv[1:exclude_index]
        excluded_file_endings = sys.argv[exclude_index + 1:]
    elif len(sys.argv) < 2:
        print("Usage: python count_lines_of_code.py <directory1> [<directory2> ...] [--exclude <.ext1> [<.ext2> ...]]")
        sys.exit(1)

    line_count, folder_count = count_lines_of_code_in_directories(directories_to_analyze, excluded_file_endings)
    print_line_counts(line_count, folder_count)
