import json
from difflib import get_close_matches  # Step 4

with open('data.json') as data_file:
    data = json.load(data_file)  # Step 1 - Check rando word


def definition(name):  # Step 1

    name = name.lower()  # Step 3 - convert all input into lower case

    if name in data:  # Step 2 - Error handling for non english words
        return data[name]  # Step 2

    elif len(get_close_matches(name, data.keys())) > 0:  # Step 4
        # Step 4
        check = input(f"Did you mean {get_close_matches(name, data.keys())[0]} instead? Enter Y if yes, otherwise N to exit: ")
        if check == "Y":
            return data[get_close_matches(name, data.keys())[0]]
        elif check == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."

    else:
        return "Sorry, this word is not an English word. Please double check your spelling."  # Step 2
    # return data[name]  # Step 1


word = input('Enter a name: ')  # Step 1

# print(definition(word))  # Step 1
output = definition(word)  # Step 5
if type(output) == list:  # Step 5
    for item in output:
        print(item)
else:
    print(output)
