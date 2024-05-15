import random
import string
import re
from faker import Faker
from nltk.corpus import words
import uuid
import pandas as pd

#Create a class for synthetic data helpers

class SyntheticHelper:

    def __init__(self):
        self.fake = Faker()


    #Function to generate addresses
    def generate_address(self, cities_dict):
        state = random.choice(list(cities_dict.keys()))
        city = random.choice(cities_dict[state])
        address_line1 = self.fake.street_address()
        return {
            'AddressLine1': address_line1,
            'AddressLine2': "",
            'AddressType': "",
            'GeoLocation': 
                {
                    "Latitude": "",
                    "Longitude": "",
                },
            'City': city,
            'StateProvince': state,
            'Country': random.choice(['USA', 'United States', '']),
            "Zip":{"Zip4":"","Zip5":""}
        }

    # Function to generate email address based on name
    def generate_email(self, first_name, last_name):
        email_address = ['gmail.com', 'yahoo.com', 'icloud.com']
        # Extract first name from full name
        firstname = first_name.lower()
        lastname = last_name.lower()
        # Generate email address based on first name
        return f"{firstname}.{lastname}@{random.choice(email_address)}"

    #Change numbers in address
    def change_numbers_in_address(self, address):
        # Define a regular expression pattern to match numbers in the address
        pattern = r'\b\d+\b'
        
        # Find all matches of numbers in the address
        numbers = re.findall(pattern, address)
        
        # Replace each number with a random value
        new_address = address
        for number in numbers:
            # Generate a random replacement value with the same number of digits
            new_number = ''.join(random.choices(string.digits, k=len(number)))
            # Replace the number in the address with the random value
            new_address = new_address.replace(number, new_number, 1)
        
        return new_address

    #Remove numbers from address
    def remove_numbers_from_address(self, address):
        # Define a regular expression pattern to match numbers in the address
        pattern = r'\d+'
        
        # Replace all numeric characters with an empty string
        new_address = re.sub(pattern, '', address)
        new_address = new_address.strip()
        
        return new_address

    def generate_random_word(self):
        # Get a list of words from NLTK corpus
        word_list = words.words()
        # Select a random word from the list
        new_word = random.choice(word_list)
        return new_word

    def randomly_replace_word(self, address, words_to_replace):
        # Split the address into individual words
        words = address.split()
        
        # Randomly select a word to replace
        word_indexes = []
        for i in range(words_to_replace):
            word_index = random.randint(0, len(words) - 1)
            word_indexes.append(word_index)
        
        # Generate a new random word
            
        for index in word_indexes:
            new_word = self.generate_random_word()
            
            # Replace the selected word with the new word
            words[index] = new_word
        
        # Join the words back into a single string
        new_address = ' '.join(words)
        
        return new_address

    def replace_numbers_in_phone(self, phone_number):
        # Split the phone number into individual digits
        digits = list(phone_number)
        
        # Choose four random indices to replace
        indices_to_replace = random.sample(range(len(digits)), 4)
        
        # Replace the digits at the chosen indices with new random digits
        for index in indices_to_replace:
            digits[index] = str(random.randint(0, 9))
        
        # Join the digits back into a single string
        new_phone_number = ''.join(digits)
        
        return new_phone_number

    def convert_keys_and_values(self, dictionary):
        new_dict = {}
        for key, value in dictionary.items():
            new_key = '"' + key + '"'   # Convert key to double quotes
            new_value = '"' + value + '"'   # Convert value to double quotes
            new_dict[new_key] = new_value
        return new_dict

    def generate_unique_id(self):
        return str(uuid.uuid4())
    
    def lists_to_dataframe(self, list1, list2):
        # Transpose the first list of lists
        df1 = pd.DataFrame(list(zip(*list1)))
        # Transpose the second list of lists
        df2 = pd.DataFrame(list(zip(*list2)))
        
        # Merge the two DataFrames on their index
        merged_df = pd.merge(df1, df2, left_index=True, right_index=True)
        merged_df.columns = ['master_name', 'master_address', 'master_number', 'master_email', 'candidate_name', 'candidate_address', 'candidate_email', 
                             'candidate_number']
        
        return merged_df
    
    def clean_commas(self, input_string):
        # Remove leading and trailing commas
        cleaned_string = input_string.strip(',')
        
        # Replace multiple consecutive commas with a single comma
        cleaned_string = re.sub(r',+', ',', cleaned_string)
        
        # Remove commas followed by a space
        cleaned_string = re.sub(r',\s', '', cleaned_string)
        
        return cleaned_string