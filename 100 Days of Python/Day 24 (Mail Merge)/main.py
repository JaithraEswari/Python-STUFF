#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt", "r") as name_data:
    name_list = name_data.readlines()

for name in name_list:
    with open("./Input/Letters/starting_letter.txt", "r") as letter_data:
        stripped_name = name.strip('\n')
        letter = letter_data.read()
        new_letter = letter.replace("[name]" , stripped_name)
        
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as final_letter:
        final_letter.write(f'{new_letter}')


