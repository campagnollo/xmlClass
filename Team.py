import xml.etree.ElementTree as et


def loader():
    group = []
    engtree = et.parse("MESS.xml")
    engroot = engtree.getroot()
    for child in engroot.findall("Eng"):
        group.append(Team(child[0].text, child[1].text, child[2].text))


    for i in group:
        if i.showloc() != 'MEX':
            print(i.showname())


class Team:

    def __init__(self, name, skills, loc):
        self.name = name
        self.skills = skills
        self.loc = loc

    def showname(self):
        return self.name

    def showloc(self):
        return self.loc

    def showskills(self):
        return self.skills


if __name__ == '__main__':
    loader()
