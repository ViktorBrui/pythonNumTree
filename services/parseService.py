
class Parsing:


    def parsing_txt(self):
        file = open("numbers.txt", "r")
        if file:
            lines = file.readlines()
            file.close()
        return lines
