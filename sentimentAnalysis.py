import os
from textblob import TextBlob
import json
from exportData import characters_polarity_csv, religion_polarity_csv


def get_character_polarity(char, characters_polarity_dic):
    name = char['name']
    religion = char['religion']
    lines = char['lines']
    gender = char['gender']
    text = ""
    for key, value in lines.items():
        for dic in value:
            line = dic['text']
            text = text + line + '\n'
    pol = TextBlob(text).sentiment.polarity
    temp = {name: [pol, religion, gender]}
    characters_polarity_dic.update(temp)


def get_polarity_by_religion(data, religion_polarity_dic):
    vikings_text = ""
    christian_text = ""
    for char in data:
        name = char['name']
        lines = char['lines']
        religion = char['religion']
        for key, value in lines.items():
            for dic in value:
                line = dic['text']
                if religion == 'Viking':
                    vikings_text = vikings_text + line + '\n'
                if religion == 'Christian':
                    christian_text = christian_text + line + '\n'

    pol_vikings = TextBlob(vikings_text).sentiment.polarity
    vikings_key = {'vikings': pol_vikings}
    pol_christian = TextBlob(christian_text).sentiment.polarity
    christian_key = {'christians': pol_christian}
    religion_polarity_dic.update(vikings_key)
    religion_polarity_dic.update(christian_key)


def get_ploarity():
    characters_polarity_dic = {}
    religion_polarity_dic = {}
    curr_dir = os.getcwd()
    file_name = curr_dir + "/Jsons/data.json"
    with open(file_name) as f:
        data = json.load(f)
    get_polarity_by_religion(data, religion_polarity_dic)
    for char in data:
        get_character_polarity(char, characters_polarity_dic)
    characters_polarity_csv(characters_polarity_dic)
    religion_polarity_csv(religion_polarity_dic)

