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

    def add_item(self, item_name):
        valid_items = {"acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu","cacao tree"}

        if item_name in valid_items:
            self.furniture.append(item_name)
    
    def print_inventory(self):
        # Implement the method here
        item_quantity = {}

        for item in self.furniture:
            if not item in item_quantity:
                item_quantity[item] = 1
            else:
                item_quantity[item] += 1
        
        if not item_quantity:
            print("Inventory empty")
        else:
            for i, item in item_quantity.items():
                print(i, item)

alice = Villager("Alice", "Koala", "guvnor")

alice.print_inventory()

alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
alice.print_inventory()