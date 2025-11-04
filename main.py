student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

### --- READ CSV FILE --- ###
data = pandas.read_csv("nato_phonetic_alphabet.csv")

### --- DICTIONARY COMPREHENSION --- ###
phonetic_codes = {row.letter: row.code for (i, row) in data.iterrows()}
print(phonetic_codes)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
### --- GENERATE PHONETIC FUNCTION --- ###
def gen_phonetics():
    word = input("Enter a word: ").upper()
    try:
        output_code = [phonetic_codes[letter] for letter in word]
    except KeyError:
        print("Do you even know what a letter is?!")
        gen_phonetics()
    else:
        print(output_code)

gen_phonetics()