from getPlaces import create_map
from readScripts import read
from characters import create_characters_arr
from readLines import read_lines_to_characters
from exportData import export_csv
from exportData import export_json
from createWordCloud import create_word_clouds
from sentimentAnalysis import get_ploarity
from topicModeling import topic_modeling


def main():
    read()
    characters = create_characters_arr()
    read_lines_to_characters(characters)
    export_csv(characters)
    export_json(characters)
    create_word_clouds()
    create_map()
    get_ploarity()
    topic_modeling()


if __name__ == "__main__":
    main()
