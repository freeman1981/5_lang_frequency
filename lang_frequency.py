import argparse
import sys
from string import punctuation
from collections import Counter


def load_data(file_path):
    with open(file_path, 'r') as file_handler:
        return file_handler.read()


def get_ten_most_frequent_words(text: str):
    translator = str.maketrans('', '', punctuation)
    translated_text = text.translate(translator).lower()
    words = translated_text.split()
    counted_words = Counter(words)
    return sorted(counted_words.items(), key=lambda item: item[1], reverse=True)[:10]


def print_most_frequent_words(dict_items):
    for dict_item in dict_items:
        print('word "{}" was founded {} times'.format(*dict_item))


def parse_command_line_and_get_it_args():
    parser = argparse.ArgumentParser(description='Find the most frequent words in file')
    parser.add_argument('path', type=str, help='path to file')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_command_line_and_get_it_args()
    try:
        text = load_data(args.path)
    except FileNotFoundError:
        print('file {file_path} does not exists'.format(file_path=args.path))
        sys.exit(1)
    print('Ten most frequent words in {file_path} is:'.format(file_path=args.path))
    print_most_frequent_words(get_ten_most_frequent_words(text))
