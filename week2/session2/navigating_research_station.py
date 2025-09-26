def navigate_research_station(station_layout, observations):
  # enumerate station layout into dictionary
  for index, char in enumerate(station_layout):
    # print(index, char)
    station_dict = {index : char, }
    pass
  


# # Example 1: Iterating over indices and characters in a string
# my_string = 'code'
# for index, char in enumerate(my_string):
#   print(index, char)

# # Prints:
# # 0 c
# # 1 o
# # 2 d
# # 3 e

# # Example 2: Enumerate with start value specified
# cereals = ['cheerios', 'fruity pebbles', 'cocoa puffs']
# for count, cereal in enumerate(cereals, start=1):
#   print(count, cereal)

station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))

