#!/usr/bin/python
import sys
import itertools
import os
import argparse


class WordsModifier:
    default_input_file = 'file1.txt'

    def __init__(self, input_file='file1.txt', output_file='file2.txt',
                 from_list_arr='no,bad', to_list_arr='yes,happy'):
        self.__input_file = input_file
        self.__output_file = output_file
        self.__from_list_arr = from_list_arr
        self.__to_list_arr = to_list_arr

    def get_input_file(self):
        return self.__input_file

    def set_input_file(self, input_file):
        self.__input_file = input_file

    def get_output_file(self):
        return self.__output_file

    def set_output_file(self, output_file):
        self.__output_file = output_file

    def get_from_list_arr(self):
        return self.__from_list_arr

    def set_from_list_arr(self, from_list_arr):
        self.__from_list_arr = from_list_arr

    def get_to_list_arr(self):
        return self.__to_list_arr

    def set_to_list_arr(self, to_list_arr):
        self.__to_list_arr = to_list_arr

    def __open_file_to_read_or_write(self, file_rw, opr, text=None):
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
                input_text = open_file_to_read_or_write(default_input_file,
                                                        opr)
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

    def replace_words(self):
        input_text = self.__open_file_to_read_or_write(self.__input_file,
                                                       opr='r')
        print input_text
        for old, new in zip(self.__from_list_arr, self.__to_list_arr):
            input_text = input_text.replace(old, new)
        print input_text
        return input_text

    def write_to_file(self, replaced_text):
        self.__open_file_to_read_or_write(self.__output_file,
                                          opr='w+', text=replaced_text)


class ArgParser:
    arguments = ""

    def __init__(self):

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

        self.arguments = parser.parse_args()

    def get_arguments(self):
        return self.arguments


def main():
    argParser = ArgParser()
    argu = argParser.get_arguments()

    MyWordsModifier = WordsModifier(argu.input_file, argu.output_file,
                                    argu.fromm.split(','), argu.to.split(','))

    replaced_text = MyWordsModifier.replace_words()
    MyWordsModifier.write_to_file(replaced_text)

if __name__ == "__main__":
    main()
