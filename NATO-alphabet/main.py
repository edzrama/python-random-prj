import pandas
# read phonetic alphabet csv
csv_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in csv_data.iterrows()}

is_on = True
while is_on:
    user_input = input("Enter a word: ").upper()
    if user_input.lower() == "exit":
        is_on = False
    else:
        # check each letter in the alphabet list
        word_list = list(user_input)
        try:
            coded_list = [nato_dict[letter] for letter in word_list]
        except KeyError:
            print("Sorry, only letters in the alphabet please.")
        else:
            print(coded_list)
