from line import Line


class Character(object):
    def __init__(self, name, aliases, gender):
        self.name = name
        self.lines_dict = {str(i): [] for i in range(1, 6)}
        self.gender = gender
        self.words_per_season = {str(i): 0 for i in range(1, 6)}
        self.aliases = aliases
        self.religion = None
        self.words = 0

    def __str__(self):
        return f'name: {self.name}, aliases: {self.aliases} , religion: {self.religion}, gender: {self.gender}, words:{self.words}'

    def getlines_dict(self):
        return self.lines_dict

    def add_line_to_character(self, season, ep, text):
        line = Line(season, ep, text)
        str_se = str(season)
        self.lines_dict[str_se].append(line)

    def getName(self):
        return self.name

    def getAliases(self):
        return self.aliases

    def deleteAliasDuplicates(self):
        temp = self.aliases
        new = list(dict.fromkeys(temp))
        self.aliases = new

    def deleteAliasJunk(self):
        i = 0
        for a in self.aliases:
            if a.lower() == "for" or a.lower() == "the" or a.lower() == "of" or a.lower() == self.name.lower():
                self.aliases.pop(i)
            i += 1

    def getTotalWords(self):
        return self.words

    def add_words(self, num_of_words):
        self.words += num_of_words

    def add_words_for_season(self, season, num_of_words):
        self.words_per_season[str(season)] += num_of_words

    def getwords_dict(self):
        return self.words_per_season

    def getReligion(self):
        return self.religion

    def setReligion(self, rel):
        self.religion = rel

    def getGender(self):
        return self.gender
