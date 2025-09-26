# One param of list of species
# return name of species with lowest population
    # if more than one lowest, return lowest index

# 1. Iterate through the dictionary 
# 2. Get the population 
# 3. Compare each population with a min var
# 4. Have a variable for the current min
# 5. Set the lowest number to min var
# 6. Add the new set with the lowest population into a list
# 7. Return the name of the species with the lowest population
def most_endangered(species_list):
    
    min_pop = species_list[0]["population"]
    name = ""
    for animal in species_list:
        if animal.get("population") < min_pop:
            min_pop = animal.get("population")
            name = animal.get("name")
    return name

species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    },
     {"name": "Bear",
     "habitat": "Mountains",
     "population": 10
    }
]

print(most_endangered(species_list))