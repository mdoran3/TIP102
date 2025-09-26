def count_endangered_species(endangered_species, observed_species):
    # make enddangered_species a set
    count = 0
    s1 = set(endangered_species)
    # result_dict = {}
    # iterate through observed_species and use .Count method
    for specie in s1:
        # result_dict[specie] = observed_species.count(specie)
        count += observed_species.count(specie)
    return count

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))  