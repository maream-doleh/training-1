#!/usr/bin/python
import sys
import itertools
import os
import argparse

default_input_file = 'file1.txt'


def open_file_to_read_or_write(file_rw, opr, text=None):
    if opr == 'r':
        if os.path.isfile(file_rw):
            try:
                with open(file_rw, opr) as f:
                    input_text = getattr(f, 'read')()
                    return input_text
            except IOError:
                print "Connot open input file!"
        else:
            print "File {0} does not exist, {1} used instead"\
                    .format(file_rw, default_input_file)
            input_text = open_file_to_read_or_write(default_input_file, opr)
            return input_text

    elif opr == 'w+':
        try:
            with open(file_rw, opr) as f:
                getattr(f, 'write')(text)
        except IOError:
            print "Connot open output file!"
    else:
        print "You use wrong operation!!"
    return None


def main():
    parser = argparse.ArgumentParser(description='Replace words')
    parser.add_argument("--input_file", dest='input_file',
                        help='file contain text you want to modify',
                        default='file1.txt')
    parser.add_argument("--output_file", dest='output_file',
                        help='file where you want to write updated text',
                        default='file2.txt')
    parser.add_argument("--from", dest='fromm',
                        help='list of words you want to replace',
                        default='no,sad,yesterday')
    parser.add_argument("--to", dest='to',
                        help='list of words you want to replace with',
                        default='yes,happy,today')
    arguments = parser.parse_args()

    input_file = arguments.input_file
    output_file = arguments.output_file
    from_list_arr = arguments.fromm.split(',')
    to_list_arr = arguments.to.split(',')
    input_text = open_file_to_read_or_write(input_file, opr='r')
    print input_text
    for old, new in zip(from_list_arr, to_list_arr):
        input_text = input_text.replace(old, new)
    print input_text
    open_file_to_read_or_write(output_file, opr='w+', text=input_text)

if __name__ == "__main__":
    main()

