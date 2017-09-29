# -*- coding: utf-8 -*-

TEXTFILE = "happiness_seg.txt"
FILTER = ["，", "。", "：", "、", "《", "》", "；", "―", "一",
    "“", "”", "（", "）", "！", "？", "　", "?"]


def get_all_words(filename):
    """Function: Read text file, return a unfinished word list.

    Args:
        String: filename in the present directory.
    Return:
        List: A word in unfinished list maybe contains FILTER content.
    """
    with open(filename, encoding='utf-8') as f:
        buf = f.read()
        words = buf.strip().split(" ")
        unfinished_word_list = []
        for word in words:
            if word not in FILTER:
                unfinished_word_list.append(word)
        return unfinished_word_list


def split_words(unfinished_word_list):
    """Function: Continue to process the unfinished word list, returns a clear list.

    Args:
        List: unfinished word list that a word may contains FILTER content.
    Return:
        List: a clear list that a word DO NOT contains FILTER content.
    """
    word_list = []
    for word in unfinished_word_list:
        if "\n" not in word:
            word_list.append(word)
        else:
            more_words = word.split("\n")
            for one_word in more_words:
                if one_word and one_word not in FILTER:
                    word_list.append(one_word)
    return word_list


def main():
    init_list = split_words(get_all_words(TEXTFILE))
    dict_two_words = {}
    word_ranking = []
    for i in range(len(init_list) - 1):
        word1 = init_list[i]
        word2 = init_list[i + 1]
        two_words = word1 + "," + word2
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
