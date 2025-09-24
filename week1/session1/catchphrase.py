def print_catchphrase(character):
	# dictionary
    dict = {"Pooh": "Oh bother!", "Tigger": "TTFN: Ta-ta for now!",
    "Eeyore" : "Thanks for noticing me.", "Christopher Robin" :"Silly old bear." }

    result = ""
    if character in dict :
        result = dict.get(character)
    else:
        result = "Sorry! I don't know " + character + "'s catchphrase!"
    
    print(result)
print_catchphrase ("Pooh")
print_catchphrase ("hi")