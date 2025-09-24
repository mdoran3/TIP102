def get_artist_info(artist, festival_schedule):
    error = {'message': 'Artist not found'}
    if artist in festival_schedule:
        return festival_schedule[artist]
    return error

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))  


"""
1. check if artist is in the list
    1a. if no, return dictionary message: artist not found
    1b. else- return artist info
"""