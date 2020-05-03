import random

DICT_FILE = "/usr/share/dict/words" # on OSX

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

def get_random_words(num_words, min_len=0, num_lines=0):
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
                random.seed()
                rnd = random.randint(0, num_lines)
                potential_word = get_line(DICT_FILE, rnd)
                if len(potential_word) >= min_len:
                    output.append(potential_word)
                    break
    return tuple(output)


