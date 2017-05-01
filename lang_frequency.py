import argparse
import sys
import os
from string import punctuation
from collections import Counter


COUNT_SHOWING_WORDS = 10


def load_data(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as file_handler:
        return file_handler.read()


def get_most_frequent_words(text: str, count_showing_words=COUNT_SHOWING_WORDS):
    translator = str.maketrans('', '', punctuation)
    translated_text = text.translate(translator).lower()
    words = translated_text.split()
    counted_words = Counter(words)
    return counted_words.most_common(count_showing_words)


def print_most_frequent_words_in_file(dict_items, path_to_file):
    print('The most frequent words in {file_path} is:'.format(file_path=path_to_file))
    for dict_item in dict_items:
        print('word "{}" was founded {} times'.format(*dict_item))


def parse_command_line_and_get_it_args():
    parser = argparse.ArgumentParser(description='Find the most frequent words in file')
    parser.add_argument('path', type=str, help='path to file')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_command_line_and_get_it_args()
    text = load_data(args.path)
    if text is None:
        print('file {file_path} does not exists'.format(file_path=args.path))
        sys.exit(1)
    print_most_frequent_words_in_file(get_most_frequent_words(text), args.path)
