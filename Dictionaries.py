def get_dictionaries():
    player_choice = input("Enter Your Choice (Anime, Manga, Manhwa: ")
    computer_choice = "Manga"
    
    choices = {"player": player_choice, "computer": computer_choice}
    
    return choices
choices = get_dictionaries()
print(choices)

