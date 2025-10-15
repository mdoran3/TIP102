class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"


apollo = Villager("Apllo", "Eagle", "pah")

bones = Villager("Bones", "Dog", "ruff it up!")

print (bones.greet_player("Samia"))