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

    @property
    def __input_file(self):
        return self.__input_file

    @__input_file.setter
    def __input_file(self, input_file):
        self.__input_file = input_file

    @property
    def __output_file(self):
        return self.__output_file

    @__output_file.setter
    def __output_file(self, output_file):
        self.__output_file = output_file

    @property
    def __from_list_arr(self):
        return self.__from_list_arr

    @__from_list_arr.setter
    def __from_list_arr(self, from_list_arr):
        self.__from_list_arr = from_list_arr

    @property
    def __to_list_arr(self):
        return self.__to_list_arr

    @__to_list_arr.setter
    def __to_list_arr(self, to_list_arr):
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

    @property
    def input_file(self):
        return self.arguments.input_file

    @property
    def output_file(self):
        return self.arguments.output_file

    @property
    def fromm(self):
        return self.arguments.fromm

    @property
    def to(self):
        return self.arguments.to


def main():
    argP = ArgParser()

    MyWordsModifier = WordsModifier(argP.input_file, argP.output_file,
                                    argP.fromm.split(','), argP.to.split(','))

    replaced_text = MyWordsModifier.replace_words()
    MyWordsModifier.write_to_file(replaced_text)

if __name__ == "__main__":
    main()
