import pathlib
# learn how to use relative paths
NAMES_PATH = "./Input/Names/invited_names.txt"
TEMPLATE_LETTER_PATH = "./Input/Letters/starting_letter.txt"
OUTPUT_LETTER_PATH = "./Output/ReadyToSend/"
# for each name in invited_names.txt
with open(NAMES_PATH) as name_list:
    names = name_list.readlines()

s_letter = pathlib.Path(TEMPLATE_LETTER_PATH).read_text()
# Replace the [name] placeholder with the actual name.
for name in names:
    new_name = name.replace("\n", "")
    new_letter = s_letter.replace("[name]", new_name)
    # Save the letters in the folder "ReadyToSend".
    output_letter = f"{OUTPUT_LETTER_PATH}/letter_for_{new_name}.txt"
    with open(output_letter, mode="w") as letter_to_send:
        letter_to_send.write(new_letter)
