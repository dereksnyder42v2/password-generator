#!/usr/bin/env python3

import random
import os
import string

#DEBUG = True
DEBUG = False
#DICT_FILE = "/usr/share/dict/words" # on OSX
DICT_FILE = "%s/words" % os.getcwd()

def count_lines(flnm):
    count = 0
    with open(flnm, 'r') as f:
        for line in f:
            count += 1
    return count-1 # so that return value corresponds to an existant line

def get_line(flnm, which_line):
    ln_num = 0
    with open(flnm, 'r') as f:
        for line in f:
            if ln_num == which_line:
                return line.rstrip().lstrip()
            else:
                ln_num += 1

def get_random_words(
    num_words, 
    min_len=1, 
    max_len=5,
    num_lines=0,
    ):
    """
    args:
        num_words...number of words in password
        min_len...minimum number of characters required
        num_lines...(opt) if you're creating multiple passwords in a batch,
                          you can pass in the number of lines in the 'words'
                          file to speed things up
    """
    if not num_lines:
        num_lines = count_lines(DICT_FILE)
    output = []
    for i in range(0, num_words):
        random.seed()
        rnd = random.randint(0, num_lines)
        if not min_len:
            output.append(get_line(DICT_FILE, rnd))
        else:
            while True:
                if DEBUG:
                    print("get_random_words output:", output)
                random.seed()
                rnd = random.randint(0, num_lines)
                potential_word = get_line(DICT_FILE, rnd)
                if len(potential_word) >= min_len and len(potential_word) <= max_len:
                    output.append(potential_word.lower())
                    break

    return output


def get_password(
    min_chars,
    max_word_len=5,
    gte_one_upper=0,
    gte_one_lower=0,
    gte_one_num=0,
    gte_one_special=0
    ):
    """
    args:
        num_chars... required length of password
        gte_one_upper...(opt) number of required upper case characters
        gte_one_lower...(opt) number of required lower case characters
        gte_one_num...(opt) number of required numbers
        gte_one_special...(opt) number of required special characters. note:
                                this script uses the 'string.punctuation'
                                tuple for special chars. 
    """

    specials = ('!', '@', '#', '$', '%', '^', '&', '*')
    # one-liners
    len_of_parts = lambda l: sum([len(i) for i in l])
    get_random_numbers = lambda n: [random.randint(0,10) for i in range(0,n)]
    get_random_specials = lambda n: [specials[random.randint(0,len(specials)-1)] for i in range(0,n)]

    parts = []
    # words
    while True:
        parts = parts + get_random_words(1, max_len=max_word_len)
        if len_of_parts(parts) >= min_chars:
            break
    ### uppers
    if gte_one_upper:
        for i in range(0, gte_one_upper):
            parts[i] = parts[i].capitalize()
    if DEBUG:
        print("uppers:", parts)
    ### lowers
    pass # TODO
    ### numbers
    random.seed()
    if gte_one_num:
        parts = parts + get_random_numbers(gte_one_num) 
    if DEBUG:
        print("numbers:", parts)

    ### specials
    random.seed()
    if gte_one_special:
        parts = parts + get_random_specials(gte_one_special)
    if DEBUG:
        print("specials:", parts)
    ### shuffle
    random.seed()
    random.shuffle(parts)
    if DEBUG:
        print("shuffle:", parts)
    ### return
    passwd = []
    for part in parts:
        passwd.append(str(part))
    return tuple(passwd)

if __name__ == "__main__":
    len_of_parts = lambda l: sum([len(i) for i in l])
    p = get_password(
        14, 
        max_word_len=5, 
        gte_one_upper=1, 
        gte_one_lower=1, 
        gte_one_num=1, 
        gte_one_special=1
        )
    print("Password: %s" % ( ''.join((p)) ))
    print("Length: %d" % (len_of_parts(p)))
