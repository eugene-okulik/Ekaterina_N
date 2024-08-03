import argparse
import os


def check_path(path):
    """Check if the path goes to file or to directory"""
    if os.path.isdir(path):
        path = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        return path
    elif os.path.isfile(path):
        return [path]
    else:
        print("Please check the provided path")


parser = argparse.ArgumentParser()
parser.add_argument("file", help="absolute path to the log files")
parser.add_argument("-k", "--keywords", help="keywords for search")
parser.add_argument("--all", help="show all results", action="store_true")
args = parser.parse_args()

file_path = check_path(args.file)

for doc in file_path:
    with open(doc, encoding="utf-8") as file:
        line_num = 0
        founded = False
        for line in file:
            line_num += 1
            if args.keywords in line:
                founded = True
                words = line.split()
                key_index = words.index(args.keywords)
                before = max(key_index - 5, 0)
                after = min(key_index + 6, len(words))
                result_list = words[before:key_index] + [args.keywords] + words[key_index + 1:after]
                result = " ".join(result_list)
                print(f" Line # {line_num}: {result}")
        if not founded:
            print("No matches have been found")
