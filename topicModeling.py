import itertools
import json
import os
import re

import gensim
import nltk
from createWordCloud import remove_keys_from_lines_dict
from exportData import create_season_topic_modeling_csv, create_all_topic_modeling_csv


def all_topic_modeling():
    curr_dir = os.getcwd()
    file_name = curr_dir + "/Jsons/data.json"
    with open(file_name, 'r') as f:
        characters = json.load(f)
        lines = list(
            itertools.chain.from_iterable(
                [itertools.chain.from_iterable(c["lines"].values()) for c in characters]))
    processed_lines = [
        [word.lower() for (word, pos) in nltk.pos_tag(nltk.word_tokenize(line["text"])) if pos[0] == 'N']
        for line in lines]

    dictionary = gensim.corpora.Dictionary(processed_lines)
    bow_corpus = [dictionary.doc2bow(line) for line in processed_lines]
    lda_model = gensim.models.LdaMulticore(bow_corpus,
                                           num_topics=3,
                                           id2word=dictionary,
                                           passes=5,
                                           workers=3)
    # for idx, topic in lda_model.print_topics(-1):
    #     print("Topic: {} \nWords: {}".format(idx, topic))
    dic = {}
    for idx, topic in lda_model.print_topics(-1):
        lst = topic.split('+')
        words = lst[:5]
        temp = {idx: words}
        dic.update(temp)
    create_all_topic_modeling_csv(dic)


def create_season_topic_modeling(season):
    curr_dir = os.getcwd()
    file_name = curr_dir + "/Jsons/data.json"
    with open(file_name, 'r') as f:
        char_dict = json.load(f)
        remove_keys_from_lines_dict(char_dict, season)
        lines = list(
            itertools.chain.from_iterable(
                [itertools.chain.from_iterable(c["lines"].values()) for c in char_dict]))
    processed_lines = [
        [word.lower() for (word, pos) in nltk.pos_tag(nltk.word_tokenize(line["text"])) if pos[0] == 'N']
        for line in lines]

    dictionary = gensim.corpora.Dictionary(processed_lines)
    bow_corpus = [dictionary.doc2bow(line) for line in processed_lines]
    lda_model = gensim.models.LdaMulticore(bow_corpus,
                                           num_topics=3,
                                           id2word=dictionary,
                                           passes=5,
                                           workers=3)
    # for idx, topic in lda_model.print_topics(-1):
    # print("Topic: {} \nWords: {}".format(idx, topic))
    dic = {}
    for idx, topic in lda_model.print_topics(-1):
        lst = topic.split('+')
        words = lst[:5]
        temp = {idx: words}
        dic.update(temp)
    create_season_topic_modeling_csv(dic, season)


def season_topic_modeling():
    season = 1
    while season < 6:
        create_season_topic_modeling(season)
        season += 1


def topic_modeling():
    all_topic_modeling()
    season_topic_modeling()
