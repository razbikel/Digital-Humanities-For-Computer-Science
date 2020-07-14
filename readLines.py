import os

from characters import create_characters_arr
from characters import find_character_by_name
from readScripts import get_str_ep_num
from characters import print_characters_array
from line import Line
from character import Character
import re


def num_of_episodes(season):
    switcher = {
        1: 9,
        2: 10,
        3: 10,
        4: 20,
        5: 20,
        6: 10
    }
    return switcher.get(season, "Invalid season")


# check if line begin with a regular expression of name:
def is_new_speaker(s1):
    if re.search("^.*:$", s1) is not None:
        return True
    else:
        return False


def print_num_of_words_per_season(char):
    words_dict = char.getwords_dict()
    for key, value in words_dict.items():
        print("character: " + char.getName() + " season: " + str(key), "num of words " + str(value))


def print_character_lines(character):
    print(character.getName())
    lines = character.getlines_dict()
    print_lines_dict(lines)


# get a list of Line objects and print its value(season,episode,text)
def print_lines_list(lines_list):
    for line in lines_list:
        print(line)


# get the lines field of a Character , a dictionary which his key is season number and his value is a list of lines
def print_lines_dict(lines_dic):
    for key, value in lines_dic.items():
        print(key)
        print_lines_list(value)


def read_seasons(characters):
    season = 1
    while season < 6:
        read_season(season, characters)
        season += 1


def read_season(season, characters):
    ep_in_se = num_of_episodes(season)
    ep = 1
    curr_dir = os.getcwd()
    while ep <= ep_in_se:
        str_ep = get_str_ep_num(ep)
        if season == 5 and (ep == 1 or ep == 2):
            file_name = curr_dir + f"/transcripts/season{season}/s0{season}ep01&02.txt"
        else:
            file_name = curr_dir + f"/transcripts/season{season}/s0{season}ep{str_ep}.txt"
        read_episode(characters, file_name)
        ep += 1


def read_episode(characters, file_name):
    with open(file_name, 'r') as episode:
        text = (episode.read())
        season = int(text[8])
        episode = int(text[19] + text[20])
        lines = text.splitlines()
        last_index = -1
        for line in lines:
            split_line = line.split(":")
            if len(split_line) >= 2 and len(split_line[0]) < 20:
                rest = split_line[1].strip()
                name = split_line[0]
                index = find_character_by_name(name, characters)
                if index != -1:
                    character = characters[index]
                    last_index = index
                else:
                    character = characters[27]
                character.add_line_to_character(season, episode, rest)
            else:
                if last_index != -1:
                    character = characters[last_index]
                    character.add_line_to_character(season, episode, split_line[0].strip())


def count_words_for_character(char):
    lines_dict = char.getlines_dict()
    for key, value in lines_dict.items():
        lines = value
        for line in lines:
            num_of_words = line.getNumOfWords()
            char.add_words(num_of_words)


def count_total_words(characters):
    for char in characters:
        count_words_for_character(char)


def count_words_for_character_per_season(char):
    lines_dict = char.getlines_dict()
    for key, value in lines_dict.items():
        lines = value
        for line in lines:
            num_of_words = line.getNumOfWords()
            season = line.getSeason()
            char.add_words_for_season(season, num_of_words)


def count_words_per_season(characters):
    for char in characters:
        count_words_for_character_per_season(char)


def read_lines_to_characters(characters):
    read_seasons(characters)
    count_total_words(characters)
    count_words_per_season(characters)
