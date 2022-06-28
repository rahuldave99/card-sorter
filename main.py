from Sorter import Sorter

num_of_decks = input("How many decks would you like in the sorter? ")

if (not num_of_decks.isnumeric() or 
    num_of_decks < 1):
    print("Please enter a valid integer and try again")
    exit()

sorter_obj = Sorter(int(num_of_decks))
sorter_obj.generate_decks()

while True:
    print("a. Request Card")
    print("b. Number of cards remaining")
    print("c. Reset Sorter")
    print("d. Reshuffle Cards")
    print("e. Exit")

    user_input = (input("")).lower()
    if user_input == "a": print(str(sorter_obj.request_card()))
    elif user_input == "b": print(str(sorter_obj.number_of_cards_left()))
    elif user_input == "c": sorter_obj.reset_sorter()
    elif user_input == "d": sorter_obj.shuffle_sorter()
    elif user_input == "e": break
    else: 
        print("Please enter a valid input")
    print("\n")