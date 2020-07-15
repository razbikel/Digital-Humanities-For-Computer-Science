# Digital-Humanities-For-Computer-Science
Text Analysis of the TV series 'Vikings' for the final project in the Digital Humanities For Computer science course BGU

As part of the course Digital Humanities For CS from Ben Gurion University,  I chose text analysis as the topic for the final project. I chose the tv series 'Vikings' , A series of events and real historical figures for my project in text analysis.

More information about the project, the work and research process and the presentation and analysis of the results are displayed on the website:
https://razbikel6.wixsite.com/vikingstextanalysis

Brief explanation of the files:
  * main_program.py - The program ran on this file  , From there, the calls are made to functions that perform the data collection, data arrangement, export and analysis of the       text itself that are implemented in the other files.
  * readLines.py - read the series scripts from the web to text files.
  * characters.py - create data structure that contains all the characters details.
  * readLines.py - fits for each characters his own lines.
  * exportData.py - create csv and json files with all the arranged data for text analysis.
  * createWordCloud.py - create world clouds by gender, religion and for each season.
  * getPlaces.py - Identify place names, convert to latitude and longitude coordinates to produce a map.
  * sentimentAnalysis.py - The analysis of the text by a positive or negative partner is performed by characters and by religion.
  * topicModeling.py - run topic modeling algorithm In order to identify the dominant issues in each season, and in general.
  
  * Json directory - The data structure of the list of characters, after all the data is arranged as follows - each member of the list contains a dictionary-type object, which         contains for each character the name, religion, nicknames, gender, the number of words spoken by him.
    In addition to each character there is an additional field of dictionary type object, which keeps the lines said by each character when the key is the season number, and the       value is the list of lines.
    This list is exported to a JSON file, which I used to create CSV files for text analysis.
    
  * CSVs directory - The CSV files I used to analyze the text:
    CSV file for each character with the word distribution in each season
    CSV file containing the list of characters, gender, and the total number of words spoken by each character
    CSV file with the names of the places mentioned in the series, their frequency of occurrence and longitude and latitude corresponding to each location in order to produce a     map
    A CSV file used for semantic analysis that contains for each character its religion and the corresponding polarity value for it
    A CSV file containing the results of the experiment for performing topic modeling for each season, with the 3 main topics and the 5 most valuable words.
    
  * transcripts directory - Episodes of the series downloaded from the web, using the Python library 'BeautifulSoup', with each episode saved in a text file.
