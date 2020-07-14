class Line(object):
    def __init__(self, season, ep, text):
        self.season = season
        self.ep = ep
        self.text = text
        self.words = len(text.split(" "))

    def __str__(self):
        return f'Season: {self.season}, Episode: {self.ep}, Text: {self.text}, NumOfWords: {self.words}'

    def getNumOfWords(self):
        return self.words

    def getSeason(self):
        return self.season

    def getEpisode(self):
        return self.ep

    def getText(self):
        return self.text