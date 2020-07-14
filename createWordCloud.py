import itertools
import os
from wordcloud import WordCloud
import json
import nltk


to_exclude = {"gasp", "chuckle", "music", "playing", "grunting", "screaming", "gasping",
              "all", "rights", "transcripts", "indistinct", "chatter", "tv",
              "kitteh", "thing", "exhale", "sigh", "groaning", "footstep", "grunt",
              "breathing", "heavily", "hmm", "indistinct", "conversation", "laughing",
              "shouting", "ungh", "laugh", "sobbing", "groan", "tv", "show"}


def create_all_word_cloud():
    wordcloud = WordCloud(background_color="black", width=900, height=400, max_words=400, contour_width=6,
                          stopwords=to_exclude)
    curr_dir = os.getcwd()
    file_name = curr_dir + "/Jsons/data.json"
    output_path = curr_dir + "/word_clouds/word_cloudAll.png"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(file_name, 'r') as f:
        char_dict = json.load(f)
        lines = list(
            itertools.chain.from_iterable([itertools.chain.from_iterable(dic["lines"].values()) for dic in char_dict]))
    processed_lines = [[word.lower() for (word, pos) in nltk.pos_tag(nltk.word_tokenize(line["text"])) if pos[0] == 'N']
                       for
                       line in lines]
    wordcloud.generate(','.join(list(itertools.chain.from_iterable(processed_lines))))
    wordcloud.to_image().save(output_path)


def remove_keys_from_lines_dict(char_dict, season):
    for d in char_dict:
        keys_to_delete = []
        for key, value in d.get('lines').items():
            if key != str(season):
                temp = {key: [{'season': season,
                               'ep': 1,
                               'text': "",
                               'words': 0}]}
                d.get('lines').update(temp)
                keys_to_delete.append(key)


def create_season_word_cloud(season):
    wordcloud = WordCloud(background_color="black", width=900, height=400, max_words=400, contour_width=6,
                          stopwords=to_exclude)
    curr_dir = os.getcwd()
    file_name = curr_dir + "/Jsons/data.json"
    output_path = curr_dir + f"/word_clouds/word_cloud_season{season}.png"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(file_name, 'r') as f:
        char_dict = json.load(f)
        remove_keys_from_lines_dict(char_dict, season)
        lines = list(
            itertools.chain.from_iterable([itertools.chain.from_iterable(dic["lines"].values()) for dic in char_dict]))
    processed_lines = [[word.lower() for (word, pos) in nltk.pos_tag(nltk.word_tokenize(line["text"])) if pos[0] == 'N']
                       for
                       line in lines]
    wordcloud.generate(','.join(list(itertools.chain.from_iterable(processed_lines))))
    wordcloud.to_image().save(output_path)


def create_seasons_word_cloud():
    season = 1
    while season < 6:
        create_season_word_cloud(season)
        season += 1


def remove_gender_lines_dict(char_dict, gender):
    for d in char_dict:
        if d.get('gender') != gender:
            keys_to_delete = []
            for key, value in d.get('lines').items():
                temp = {key: [{'season': 1,
                               'ep': 1,
                               'text': "",
                               'words': 0}]}
                d.get('lines').update(temp)
                keys_to_delete.append(key)


def create_gender_word_cloud(gender):
    wordcloud = WordCloud(background_color="black", width=900, height=400, max_words=400, contour_width=6,
                          stopwords=to_exclude)
    curr_dir = os.getcwd()
    file_name = curr_dir + "/Jsons/data.json"
    output_path = curr_dir + f"/word_clouds/word_cloud_{gender}.png"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(file_name, 'r') as f:
        char_dict = json.load(f)
        remove_gender_lines_dict(char_dict, gender)
        lines = list(
            itertools.chain.from_iterable([itertools.chain.from_iterable(dic["lines"].values()) for dic in char_dict]))
    processed_lines = [[word.lower() for (word, pos) in nltk.pos_tag(nltk.word_tokenize(line["text"])) if pos[0] == 'N']
                       for
                       line in lines]
    wordcloud.generate(','.join(list(itertools.chain.from_iterable(processed_lines))))
    wordcloud.to_image().save(output_path)


def remove_religion_lines_dict(char_dict, religion):
    for d in char_dict:
        if d.get('religion') != religion:
            keys_to_delete = []
            for key, value in d.get('lines').items():
                temp = {key: [{'season': 1,
                               'ep': 1,
                               'text': "",
                               'words': 0}]}
                d.get('lines').update(temp)
                keys_to_delete.append(key)


def create_religion_word_cloud(religion):
    wordcloud = WordCloud(background_color="black", width=900, height=400, max_words=400, contour_width=6,
                          stopwords=to_exclude)
    curr_dir = os.getcwd()
    file_name = curr_dir + "/Jsons/data.json"
    output_path = curr_dir + f"/word_clouds/word_cloud_{religion}.png"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(file_name, 'r') as f:
        char_dict = json.load(f)
        remove_religion_lines_dict(char_dict, religion)
        lines = list(
            itertools.chain.from_iterable([itertools.chain.from_iterable(dic["lines"].values()) for dic in char_dict]))
    processed_lines = [[word.lower() for (word, pos) in nltk.pos_tag(nltk.word_tokenize(line["text"])) if pos[0] == 'N']
                       for
                       line in lines]
    wordcloud.generate(','.join(list(itertools.chain.from_iterable(processed_lines))))
    wordcloud.to_image().save(output_path)


def create_word_clouds():
    create_all_word_cloud()
    create_seasons_word_cloud()
    create_gender_word_cloud("male")
    create_gender_word_cloud("female")
    create_religion_word_cloud("Viking")
    create_religion_word_cloud("Christian")
