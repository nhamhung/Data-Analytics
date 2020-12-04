#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.docx") as letter:
    letter_content = letter.read()

with open("./Input/Names/invited_names.txt") as name_file:
    names = [name.strip() for name in name_file.readlines()]

# print(letter_content)
# print(names)

for name in names:
    new_letter = letter_content.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.docx", mode="w") as output_file:
        output_file.write(new_letter)
    with open(f"./Output/ReadyToSend/letter_for_{name}.docx", mode="r") as output_file:
        print(output_file.read())
