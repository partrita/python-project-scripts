import os.path
import sys


def find_longest_words(file_content):
    last_length = 0
    words = []
    # the first loop is on each line
    for line in file_content:
        # gradually searching longest words dividing each line in a list of words and looping on the list
        for el in line.split():
            if len(el) > last_length:
                words = [el]
                last_length = len(el)
            elif len(el) == last_length and el not in words:
                words.append(el)
    return words, last_length


if __name__ == '__main__':
    input_file = input('please enter file name: ')
    file_to_open = os.path.join("files", input_file)
    try:
        with open(file_to_open, 'r') as fin:
            words, max_length = find_longest_words(fin)
        print(f'length of longest word(s): {max_length}')
        print('words: {}'.format(', '.join(words)))
    except FileNotFoundError:
        print("file not found.")
        sys.exit()
