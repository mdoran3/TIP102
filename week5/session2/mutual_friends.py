class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []

    def get_mutuals(self, new_contact):
        mutual_friends = []
        for friend in self.friends:
            if friend in new_contact.friends:
                mutual_friends.append(friend.name)
        return mutual_friends

bob = Villager("Bob", "Cat", "pthhhpth")
marshal = Villager("Marshal", "Squirrel", "sulky")
ankha = Villager("Ankha", "Cat", "me meow")
fauna = Villager("Fauna", "Deer", "dearie")
raymond = Villager("Raymond", "Cat", "crisp")
stitches = Villager("Stitches", "Cub", "stuffin")

bob.friends = [stitches, raymond, fauna]
marshal.friends = [raymond, ankha, fauna]
print(bob.get_mutuals(marshal))

ankha.friends = [marshal]
print(bob.get_mutuals(ankha))

# Understand
    #write new mehtod with new_contact as param, which  is instance of Villager and returns all friends in common with current Villager

# Plan
    # 1) create a set or list to store friends in common
    # 2) Iterate through current Villagers list of friends and compare to new_contact's list
    # 3) If there is match, put name into new set
    # 4) return list / set of mutual friends