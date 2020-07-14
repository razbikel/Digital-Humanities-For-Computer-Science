import urllib.request
from bs4 import BeautifulSoup
from gender_detector.gender_detector import GenderDetector

from character import Character


def print_characters_array(char_arr):
    for char in char_arr:
        print(char)


# get a character's name and characters array and find his index in the characters array
def find_character_by_name(name, characters):
    index = 0
    is_found = False
    curr_name = name.lower()
    for char in characters:
        total_names = char.getAliases()
        total_names.append(char.getName())
        total_names_lower = []
        for n in total_names:
            total_names_lower.append(n.lower())
        char.deleteAliasDuplicates()
        char.deleteAliasJunk()
        if curr_name in total_names_lower:
            is_found = True
            break
        else:
            index += 1
    if is_found:
        return index
    else:
        return -1


def has_aliases(string):
    if len(string.split()) > 1:
        return True
    else:
        return False


def get_aliases(name):
    output = []
    sub_strs = name.split()
    sub1 = sub_strs[0]
    output.append(sub1)
    if sub_strs[1].lower() != "the":
        sub2 = sub_strs[0] + " " + sub_strs[1]
        output.append(sub2)
    sub3 = sub_strs[1]
    output.append(sub3)
    if len(sub_strs) > 2:
        if sub_strs[2].lower() != "of":
            sub4 = sub_strs[0] + " " + sub_strs[1] + " " + sub_strs[2]
            output.append(sub4)
        sub5 = sub_strs[2]
        output.append(sub5)
    if len(sub_strs) > 3:
        sub6 = sub_strs[0] + " " + sub_strs[1] + " " + sub_strs[2] + " " + sub_strs[3]
        output.append(sub6)
    return output


def create_religion_dict(characters_names):
    religions = ['Viking', 'Viking', 'Viking', 'Viking', 'Viking', 'Viking', 'Christian',
                 'Viking', 'Viking', 'Christian', 'Viking', 'Viking', 'Viking', 'Christian',
                 'Viking', 'Viking', 'Viking', 'Viking', 'Viking', 'Viking', 'Viking',
                 'Christian', 'Christian', 'Christian', 'Viking', 'Viking', 'Viking', 'None']
    religion_dict = {}
    i = 0
    for char_name in characters_names:
        value = religions[i]
        temp = {char_name: value}
        religion_dict.update(temp)
        i += 1
    return religion_dict


def find_gender(name, aliases):
    output = []
    char_gender = 'unknown'
    detector1 = GenderDetector('us')
    output.append(detector1.guess(name))
    for alias in aliases:
        output.append(detector1.guess(alias))
    for res in output:
        if res != 'unknown':
            char_gender = res
            break
    return char_gender


def read_characters():
    characters_names = []
    url = 'https://en.wikipedia.org/wiki/List_of_Vikings_characters'
    web_page = urllib.request.urlopen(url)
    html_page = BeautifulSoup(web_page, 'html.parser')
    names = html_page.findAll('span', attrs={'class': 'toctext'})
    for e in names:
        name = e.text.strip()
        characters_names.append(name)
    output = characters_names[1:29]
    return output


def is_male_index(index):
    unknown_male_indexes = [4, 6, 11, 12, 18, 20, 21]
    unknown_female_indexes = [1, 3, 8, 25, 26]
    if index in unknown_male_indexes:
        return True
    else:
        return False


def get_religion_by_name(name, religion_dict):
    return religion_dict.get(name, "Invalid name")


def get_characters_array(characters_names):
    characters_array = []
    religion_dict = create_religion_dict(characters_names)
    i = 0
    for name in characters_names:
        aliases = []
        if has_aliases(name):
            to_add = get_aliases(name)
            for alias in to_add:
                aliases.append(alias)
        char_gender = find_gender(name, aliases)
        if char_gender == "unknown":
            if is_male_index(i):
                char_gender = "male"
            else:
                char_gender = "female"
        religion = get_religion_by_name(name, religion_dict)
        char = Character(name, aliases, char_gender)
        char.setReligion(religion)
        characters_array.append(char)
        i += 1
    return characters_array


def create_characters_arr():
    characters_names = read_characters()
    return get_characters_array(characters_names)
