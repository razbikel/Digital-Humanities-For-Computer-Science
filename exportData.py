import csv
import json
import os


def create_all_topic_modeling_csv(dic):
    curr_dir = os.getcwd()
    file_name = curr_dir + f"/CSVs/topicModeling/all.csv"
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name, 'w') as new_csv:
        writer = csv.writer(new_csv, lineterminator='\n')
        writer.writerow(
            ['Topic Index', 'Word1', 'Word2', 'Word3', 'Word4', 'Word5'])
        for key, value in dic.items():
            writer.writerow(
                [key, value[0], value[1], value[2], value[3], value[4]])


def create_season_topic_modeling_csv(dic, season):
    str_season = str(season)
    curr_dir = os.getcwd()
    file_name = curr_dir + f"/CSVs/topicModeling/season_{str_season}.csv"
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name, 'w') as new_csv:
        writer = csv.writer(new_csv, lineterminator='\n')
        writer.writerow(
            ['Topic Index', 'Word1', 'Word2', 'Word3', 'Word4', 'Word5'])
        for key, value in dic.items():
            writer.writerow(
                [key, value[0], value[1], value[2], value[3], value[4]])


def create_main_csv(characters):
    curr_dir = os.getcwd()
    file_name = curr_dir + "/CSVs/main.csv"
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name, 'w') as new_csv:
        writer = csv.writer(new_csv, lineterminator='\n')
        writer.writerow(
            ['Name', 'Religion', 'Gender', 'Season1', 'Season2', 'Season3', 'Season4', 'Season5', 'Words'])
        for character in characters:
            if character.getName() != "Othere":
                writer.writerow(
                    [character.name, character.religion, character.gender, *character.words_per_season.values(),
                     character.words])


def create_character_csv(character):
    name = character.getName()
    curr_dir = os.getcwd()
    file_name = curr_dir + f"/CSVs/Characters/{name}.csv"
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name, 'w') as new_csv:
        writer = csv.writer(new_csv, lineterminator='\n')
        writer.writerow(['Season', 'Words'])
        season = 1
        while season < 6:
            writer.writerow([season, character.words_per_season[str(season)]])
            season += 1


def create_places_csv(places_dic):
    curr_dir = os.getcwd()
    file_name = curr_dir + f"/CSVs/places.csv"
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name, 'w') as new_csv:
        writer = csv.writer(new_csv, lineterminator='\n')
        writer.writerow(['Name', 'Occurences', 'Latitude', 'Longitude'])
        for key, value in places_dic.items():
            writer.writerow([key, value[0], value[1], value[2]])


def divide_places(places_dic, big_places, med_places, small_places):
    for key, value in places_dic.items():
        num_occ = value[0]
        temp = {key: value}
        if num_occ < 48:
            small_places.update(temp)
        if 48 <= num_occ < 120:
            med_places.update(temp)
        if num_occ >= 120:
            big_places.update(temp)


def crate_csv_map(places_dic, file_name):
    curr_dir = os.getcwd()
    file_name = curr_dir + f"/CSVs/places_for_map/{file_name}.csv"
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name, 'w') as new_csv:
        writer = csv.writer(new_csv, lineterminator='\n')
        writer.writerow(['lat', 'lng', 'name'])
        for key, value in places_dic.items():
            writer.writerow([value[1], value[2], key])


def create_places_csv_for_map(places_dic):
    big_places = {}
    med_places = {}
    small_places = {}
    divide_places(places_dic, big_places, med_places, small_places)
    crate_csv_map(small_places, "small_places")
    crate_csv_map(med_places, "med_places")
    crate_csv_map(big_places, "big_places")


def create_characters_csv(characters):
    for character in characters:
        if character.getName() != "Othere":
            create_character_csv(character)


def create_season_csv(characters):
    season = 1
    curr_dir = os.getcwd()
    while season < 6:
        file_name = curr_dir + f"/CSVs/Seasons/{season}.csv"
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        with open(file_name, 'w') as new_csv:
            writer = csv.writer(new_csv, lineterminator='\n')
            writer.writerow(['Name', 'Religion', 'Gender', 'Words'])
            for char in characters:
                if char.getName() != "Othere":
                    writer.writerow([char.name, char.religion, char.gender, char.words_per_season[str(season)]])
        season += 1


def characters_polarity_csv(characters_polarity_dic):
    curr_dir = os.getcwd()
    file_name = curr_dir + f"/CSVs/SentimentAnalysis/character_polarity.csv"
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name, 'w') as new_csv:
        writer = csv.writer(new_csv, lineterminator='\n')
        writer.writerow(['Name', 'Polarity', 'Religion', 'Gender'])
        for key, value in characters_polarity_dic.items():
            writer.writerow([key, value[0], value[1], value[2]])


def religion_polarity_csv(religion_polarity_dic):
    curr_dir = os.getcwd()
    file_name = curr_dir + f"/CSVs/SentimentAnalysis/religion_polarity.csv"
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name, 'w') as new_csv:
        writer = csv.writer(new_csv, lineterminator='\n')
        writer.writerow(['Religion', 'Polarity'])
        for key, value in religion_polarity_dic.items():
            writer.writerow([key, value])


def convert_line_object_to_dict(line):
    return {'season': line.getSeason(),
            'episode': line.getEpisode(),
            'text': line.getText(),
            'words': line.getNumOfWords()}


def create_character_dict(char):
    lines = char.getlines_dict()
    dict_lines = {str(i): [] for i in range(1, 6)}
    for key, value in lines.items():
        for line in value:
            season = line.getSeason()
            line_dic = convert_line_object_to_dict(line)
            dict_lines[str(season)].append(line_dic)

    char1 = {'name': char.getName(),
             'religion': char.getReligion(),
             'aliases': char.getAliases(),
             'gender': char.getGender(),
             'words': char.getTotalWords(),
             'words_per_season': char.getwords_dict(),
             'lines': dict_lines
             }
    return char1


def create_json(characters):
    data = []
    for char in characters:
        if char.getName() != "Othere":
            char_dict = create_character_dict(char)
            data.append(char_dict)
    curr_dir = os.getcwd()
    file_name = curr_dir + "/Jsons/data.json"
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name, 'w') as outfile:
        json.dump(data, outfile, indent=4)


def export_csv(characters):
    create_main_csv(characters)
    create_characters_csv(characters)
    create_season_csv(characters)


def export_json(characters):
    create_json(characters)
