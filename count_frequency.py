# -*- coding: utf-8 -*-

import re

TEXTFILE = "happiness_seg.txt"


def get_all_words2(filename):
    """Read the text file, filter the content, and return a word list.

    Args:
        filaneme (string): string of filename in the present directory.

    Return:
        word_list (list): a list with words have been filtered.
    """
    with open(filename, encoding='utf-8') as f:
        buf = f.read()
        word_list = []
        filted_buf = re.sub("[\s，。：、《》；―一“”（）！？　?]+", " ", buf)
        words = filted_buf.strip().split(" ")
        for word in words:
            if word:
                word_list.append(word)
        return word_list


def main():
    """Read txt file, then count the frequency of each two adjacent words.

    Args:
        None

    Returns:
        None
    """
    init_list = get_all_words2(TEXTFILE)
    dict_two_words = {}
    word_ranking = []
    for i in range(len(init_list) - 1):
        word1 = init_list[i]
        word2 = init_list[i + 1]
        two_words = word1 + ", " + word2
        if two_words not in dict_two_words:
            dict_two_words[two_words] = 1
        else:
            dict_two_words[two_words] += 1
    for key in dict_two_words:
        _tuple = (key, dict_two_words[key])
        word_ranking.append(_tuple)
    word_ranking.sort(key=lambda x: x[1], reverse=True)
    for i in range(10):
        print("Rank %s: %s" % (i + 1, word_ranking[i]))


if __name__ == '__main__':
    main()
