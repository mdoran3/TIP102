class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
	
    def set_catchphrase(self, new_catchphrase):
        is_updated = True
        if len(new_catchphrase) >= 20:
            is_updated = False
              
        for char in new_catchphrase:
            if not char.isalpha() and not char.isspace():
                is_updated = False 
                break

        if is_updated == True:
            self.catchphrase = new_catchphrase
            print("Catchphrase Updated")
        else:
            print("Invalid Catchphrase")
         
alice = Villager("Alice", "Koala", "guvnor")

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)
alice.set_catchphrase("@@@ !!!")
print(alice.catchphrase)