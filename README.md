# Count Lines Python Script

A simple script that counts the lines of code within specified directory paths, including all subdirectories. It allows for excluding specific file formats from the count.

## Requirements
- Python 3.6 or higher

## Installation
No installation is necessary. Simply clone or download this repository to your local machine.

```bash
git clone git@github.com:RaphaelMaschinsen/count-lines.git
cd count_lines
```

## Usage
The script can be run from the command line, providing the paths to the directories you want to analyze. Optionally, you can exclude specific file formats.

```
python count_lines.py <directory1> [<directory2> ...] [--exclude <.ext1> [<.ext2> ...]]
```

### Example Usage
Count lines in a single directory:

```
python count_lines.py /path/to/directory
```

Count lines in multiple directories:
```
python count_lines.py /path/to/directory1 /path/to/directory2
```

Count lines excluding specific file formats:
```
python count_lines.py /path/to/directory --exclude .pyc .txt
```

### Example Output
```
Lines of code by folder:
/path/to/directory1: 300 lines
/path/to/directory2: 150 lines

Lines of code by file:
/path/to/directory1/file1.py: 100 lines
/path/to/directory1/subdir/file2.js: 200 lines
/path/to/directory2/config.xml: 150 lines

Total lines of code: 450
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.
