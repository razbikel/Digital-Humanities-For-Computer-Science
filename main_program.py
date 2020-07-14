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
    # read the series scripts from the web to text files
    read()
    # create data structure that contains all the characters details
    characters = create_characters_arr()
    # fits for each characters his own lines
    read_lines_to_characters(characters)
    # create csv and json files with all the arranged data for text analysis
    export_csv(characters)
    export_json(characters)
    # create world clouds
    create_word_clouds()
    # create map
    create_map()
    # sentiment analysis
    get_ploarity()
    # topic modeling
    topic_modeling()


if __name__ == "__main__":
    main()
