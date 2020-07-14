import os
from geopy.geocoders import Nominatim
from geotext import GeoText
from readLines import num_of_episodes
from readLines import get_str_ep_num
from exportData import create_places_csv
from exportData import create_places_csv_for_map

to_delete = ["Man", "Young", "Of", "Bell", "Swords", "Most", "Mary", "Split", "Ho", "Retreat", "Best",
             "Roman", "Eagle", "Offa", "Barking", "Sparks", "Reading", "Born", "Paradise", "Bar", "Bear",
             "Hercules", "Marks"
                         "Arles", "Much", "Rouen", "Maeks", "Bay", "Corpus Christi", "Same", "Alliance", "Anna",
             "Golden"]


def old_places(place):
    switcher = {
        'Frankia': 'France',
        'Wessex': 'London',
        'Kattegat': 'Oslo',
        'England': 'United Kingdom',
        'Northumbria': 'Liverpool',
        'Mercia': 'Leicester'
    }
    return switcher.get(place, "None")


def get_coordinates(place):
    res = old_places(place)
    if res != "None":
        to_coor = res
    else:
        to_coor = place
    locator = Nominatim(user_agent="myGeocoder")
    location = locator.geocode(to_coor)
    return {'latitude': location.latitude,
            'longitude': location.longitude}


def check_and_replace(text, old, new):
    return text.replace(old, new)


def replace_in_list(places, old, new):
    i = 0
    while i < len(places):
        if places[i] == old:
            places[i] = new
        i += 1


def get_places_from_episode(places, file_name):
    with open(file_name, 'r') as f:
        text = f.read()
        text1 = check_and_replace(text, "Frankia", "France")
        text2 = check_and_replace(text1, "Wessex", "London")
        text3 = check_and_replace(text2, "Kattegat", "Oslo")
        text4 = check_and_replace(text3, "England", "United Kingdom")
        text5 = check_and_replace(text4, "Northumbria", "Liverpool")
        text6 = check_and_replace(text5, "Mercia", "Leicester")
        locations = GeoText(text6)
        for item in locations.cities:
            if not (item in to_delete):
                places.append(item)
        for item in locations.countries:
            if not (item in to_delete):
                places.append(item)
        replace_in_list(places, 'France', 'Frankia')
        replace_in_list(places, 'London', 'Wessex')
        replace_in_list(places, 'United Kingdom', 'England')
        replace_in_list(places, 'Oslo', 'Kattegat')
        replace_in_list(places, 'Liverpool', 'Northumbria')
        replace_in_list(places, 'Leicester', 'Mercia')


def get_places_from_season(places):
    season = 1
    while season < 7:
        ep_in_se = num_of_episodes(season)
        ep = 1
        curr_dir = os.getcwd()
        while ep <= ep_in_se:
            str_ep = get_str_ep_num(ep)
            if season == 5 and (ep == 1 or ep == 2):
                file_name = curr_dir + f"/transcripts/season{season}/s0{season}ep01&02.txt"
            else:
                file_name = curr_dir + f"/transcripts/season{season}/s0{season}ep{str_ep}.txt"
            get_places_from_episode(places, file_name)
            ep += 1
        season += 1


def create_dic_of_places(places):
    dic = {}
    no_dup_places = list(dict.fromkeys(places))
    for word in places:
        occ = 0
        for w in places:
            if word == w:
                occ += 1
        temp = {word: [occ]}
        dic.update(temp)
    for place in no_dup_places:
        coor = get_coordinates(place)
        latitude = coor['latitude']
        longitude = coor['longitude']
        dic[place].append(latitude)
        dic[place].append(longitude)
    return dic


def create_map():
    places = []
    get_places_from_season(places)
    dic = create_dic_of_places(places)
    create_places_csv(dic)
    create_places_csv_for_map(dic)


