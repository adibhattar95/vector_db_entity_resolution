import pandas as pd
import random
import string
from synthetic import SyntheticHelper
from faker import Faker
from tqdm import tqdm

#Create a class for creating match types

helper = SyntheticHelper()

class MatchType:

    def __init__(self, master_profiles, female_name_list, male_name_list, prefix_female, prefix_male, male_suffixes, middle_name,
                 cities):
        self.master_profiles = master_profiles
        self.female_name_list = female_name_list
        self.male_name_list = male_name_list
        self.prefix_female = prefix_female
        self.prefix_male = prefix_male
        self.male_suffixes = male_suffixes
        self.middle_name = middle_name
        self.cities = cities
        self.fake = Faker()


    # Function to generate easy match pairs with slight variations
    def create_easy_match(self):
        candidate_name_profiles = []
        candidate_address_profiles = []
        candidate_email_profiles = []
        candidate_phone_profiles = []

        for name in tqdm(self.master_profiles[0]):
            candidate_name = {}
            candidate_name['FirstName'] = name['FirstName']
            candidate_name['LastName'] = name['LastName']
            candidate_name['Gender'] = name['Gender']
        # Introduce slight variations
            if name['FirstName'] in self.female_name_list:
                candidate_name['Prefix'] = random.choice(self.prefix_female)
            else:
                candidate_name['Prefix'] = random.choice(self.prefix_male)

            if name['FirstName'] in self.male_name_list:
                candidate_name['SuffixName'] = random.choice(self.male_suffixes)
            else:
                candidate_name['SuffixName'] = ''
            candidate_name['MiddleName'] = random.choice([name['MiddleName'] + ''.join([random.choice(list(string.ascii_lowercase)) for _ in range(3)]),
                                                            name['MiddleName']])
            candidate_name_profiles.append(candidate_name)
        print("Easy Name matches created")

        for address in tqdm(self.master_profiles[1]):
            candidate_address = {}
            candidate_address['StateProvince'] = address['StateProvince']
            candidate_address['Country'] = address['Country']
            candidate_address['AddressLine2'] = address['AddressLine2']
            candidate_address['AddressType'] = address['AddressType']
            candidate_address['GeoLocation'] = {"Latitude": "", "Longitude": ""}
            candidate_address['Zip'] = {"Zip4": "", "Zip5": ""}
            if random.choice([True, False]):
                # Replace 'St.' with 'Street'
                candidate_address['AddressLine1'] = address['AddressLine1'].replace('Avenue', 'Ave.').replace('Suite', 'Ste').replace('Apt.', 'Apartment')
            else:
                candidate_address['AddressLine1'] = address['AddressLine1']
            if random.choice([True, False]):
                # Remove City
                candidate_address['City'] = ''
            else:
                candidate_address['City'] = address['City']
            candidate_address_profiles.append(candidate_address)
        print("Easy address matches created")

        for number in tqdm(self.master_profiles[2]):
            candidate_number = {}
            if random.choice([True, False]):
                # Remove City
                candidate_number['Number'] = ''
            else:
                candidate_number['Number'] = number['Number']
            candidate_number['Type'] = number['Type']
            candidate_phone_profiles.append(candidate_number)
        print("Easy phone matches created")
        
        for email in tqdm(self.master_profiles[3]):
            candidate_email = {}
            if random.choice([True, False]):
                # Remove City
                candidate_email['Email'] = ''
            else:
                candidate_email['Email'] = email['Email']
            candidate_email['Type'] = email['Type']
            candidate_email_profiles.append(candidate_email)
        print("Easy email matches created")
            
        return [candidate_name_profiles, candidate_address_profiles, candidate_email_profiles, candidate_phone_profiles]

    def create_difficult_match(self):
        candidate_name_profiles = []
        candidate_address_profiles = []
        candidate_email_profiles = []
        candidate_phone_profiles = []

        first_name_list = [first_name['FirstName'] for first_name in self.master_profiles[0]]
        last_name_list = [first_name['LastName'] for first_name in self.master_profiles[0]]

        for name in tqdm(self.master_profiles[0]):
            candidate_name = {}
            candidate_name['FirstName'] = random.choice([name['FirstName'][0], name['FirstName'][:4], name['FirstName'] + name['FirstName'][-1], 
                                                        name['FirstName'][0] + name['FirstName'], name['FirstName']])
            candidate_name['LastName'] = random.choice([name['LastName'][0], name['LastName'] + name['LastName'][-1], 
                                                        name['LastName'][0] + name['LastName'], name['LastName']])
            candidate_name['Gender'] = name['Gender']
        # Introduce slight variations
            if name['FirstName'] in self.female_name_list:
                candidate_name['Prefix'] = random.choice(self.prefix_female)
            else:
                candidate_name['Prefix'] = random.choice(self.prefix_male)
            if name['FirstName'] in self.male_name_list:
                candidate_name['SuffixName'] = random.choice(self.male_suffixes)
            else:
                candidate_name['SuffixName'] = ''
            candidate_name['MiddleName'] = random.choice([name['MiddleName'] + ''.join([random.choice(list(string.ascii_lowercase)) for _ in range(3)]),
                                                            name['MiddleName']])
            candidate_name_profiles.append(candidate_name)
        print("Difficult name matches created")

        for address in tqdm(self.master_profiles[1]):
            candidate_address = {}
            candidate_address['StateProvince'] = random.choice([address['StateProvince'], ''])
            candidate_address['City'] = random.choice([address['City'], ''])
            candidate_address['Country'] = random.choice([address['Country'], 'US', 'USA', 'United States', 'United States of America', ''])
            candidate_address['AddressLine2'] = address['AddressLine2']
            candidate_address['AddressType'] = address['AddressType']
            candidate_address['GeoLocation'] = {"Latitude": "", "Longitude": ""}
            candidate_address['Zip'] = {"Zip4": "", "Zip5": ""}
            # Replace 'St.' with 'Street'
            candidate_address['AddressLine1'] = random.choice(
                [address['AddressLine1'].replace('Avenue', 'Ave.').replace('Suite', 'Ste').replace('Apt.', 'Unit'),
                helper.remove_numbers_from_address(address['AddressLine1'])]
            )
            candidate_address_profiles.append(candidate_address)
        print("Difficult address matches created")

        for number in tqdm(self.master_profiles[2]):
            candidate_number = {}
            candidate_number['Number'] = random.choice(['', number['Number'], number['Number'].replace('+', '').replace('-', '').replace('x', '')])
            candidate_number['Type'] = number['Type']
            candidate_phone_profiles.append(candidate_number)
        print("Difficult phone matches created")
        
        i = 0
        for email in tqdm(self.master_profiles[3]):
            candidate_email = {}
            candidate_email['Email'] = random.choice([email['Email'], '',
                                                    f"{first_name_list[i].lower()}.{last_name_list[i].lower()}@{self.fake.company_email().split('@')[-1]}",
                                                    f"{first_name_list[i][0].lower()}.{last_name_list[i].lower()}@{self.fake.company_email().split('@')[-1]}",
                                                    f"{first_name_list[i].lower()}.{last_name_list[i][0].lower()}@{self.fake.company_email().split('@')[-1]}"])
            candidate_email['Type'] = email['Type']
            candidate_email_profiles.append(candidate_email)
            i += 1
        print("Difficult email matches created")
            
        return [candidate_name_profiles, candidate_address_profiles, candidate_email_profiles, candidate_phone_profiles]

    def create_easy_non_match(self):
        candidate_name_profiles = []
        candidate_address_profiles = []
        candidate_email_profiles = []
        candidate_phone_profiles = []

        for name in tqdm(self.master_profiles[0]):
            candidate_name = {}
            candidate_name['FirstName'] = self.fake.first_name_female() if name['FirstName'] in self.female_name_list else self.fake.first_name_male()
            candidate_name['LastName'] = self.fake.last_name()
            candidate_name['Gender'] = name['Gender']
        # Introduce slight variations
            if name['FirstName'] in self.female_name_list:
                candidate_name['Prefix'] = random.choice(self.prefix_female)
            else:
                candidate_name['Prefix'] = random.choice(self.prefix_male)

            if name['FirstName'] in self.male_name_list:
                candidate_name['SuffixName'] = random.choice(self.male_suffixes)
            else:
                candidate_name['SuffixName'] = ''
            
            candidate_name['MiddleName'] = random.choice(self.middle_name)
            candidate_name_profiles.append(candidate_name)
        print("Easy name non-matches created")

        for _ in tqdm(range(len(self.master_profiles[1]))):
            candidate_address = helper.generate_address(self.cities)
            candidate_address_profiles.append(candidate_address)
        print("Easy address non-matches created")

        for _ in tqdm(range(len(self.master_profiles[2]))):
            candidate_number = {'Number': self.fake.phone_number()}
            candidate_number['Type'] = ""
            candidate_phone_profiles.append(candidate_number)
        print("Easy phone non-matches created")
        
        i = 0
        for _ in tqdm(range(len(self.master_profiles[3]))):
            candidate_email = {'Email': helper.generate_email(candidate_name_profiles[i]['FirstName'], candidate_name_profiles[i]['LastName'])}
            candidate_email['Type'] = ""
            candidate_email_profiles.append(candidate_email)
            i += 1
        print("Easy email non-matches created")
        return [candidate_name_profiles, candidate_address_profiles, candidate_email_profiles, candidate_phone_profiles]

    def create_difficult_non_match(self):
        candidate_name_profiles = []
        candidate_address_profiles = []
        candidate_email_profiles = []
        candidate_phone_profiles = []

        for name in tqdm(self.master_profiles[0]):
            candidate_name = {}
            if random.choice([True, False]):
                candidate_name['FirstName'] = self.fake.first_name_female() if name['FirstName'] in self.female_name_list else self.fake.first_name_male()
                candidate_name['LastName'] = name['LastName']
            else:
                candidate_name['FirstName'] = name['FirstName']
                candidate_name['LastName'] = self.fake.last_name()
            candidate_name['Gender'] = random.choice([name['Gender'], ''])
        # Introduce slight variations
            candidate_name['Prefix'] = name['Prefix']
            candidate_name['SuffixName'] = name['SuffixName']
            candidate_name['MiddleName'] = random.choice([random.choice(self.middle_name), name['MiddleName']])
            candidate_name_profiles.append(candidate_name)
        print("Difficult name non-matches created")

        for address in tqdm(self.master_profiles[1]):
            candidate_address = {}
            candidate_address['StateProvince'] = address['StateProvince']
            candidate_address['City'] = address['City']
            candidate_address['Country'] = address['Country']
            candidate_address['AddressLine1'] = random.choice([helper.change_numbers_in_address(address['AddressLine1']),
                                                                helper.randomly_replace_word(address['AddressLine1'], 2),
                                                                helper.randomly_replace_word(address['AddressLine1'], 3)])
            candidate_address['AddressLine2'] = address['AddressLine2']
            candidate_address['AddressType'] = address['AddressType']
            candidate_address['GeoLocation'] = {"Latitude": "", "Longitude": ""}
            candidate_address['Zip'] = {"Zip4": "", "Zip5": ""}
            candidate_address_profiles.append(candidate_address)
        print("Difficult address non-matches created")
            

        for number in tqdm(self.master_profiles[2]):
            candidate_number = {}
            candidate_number['Number'] = random.choice([helper.replace_numbers_in_phone(number['Number']), self.fake.phone_number()])
            candidate_number['Type'] = number['Type']
            candidate_phone_profiles.append(candidate_number)
        print("Difficult number non-matches created")
        
        i = 0
        for _ in tqdm(range(len(self.master_profiles[3]))):
            candidate_email = {'Email': helper.generate_email(candidate_name_profiles[i]['FirstName'], candidate_name_profiles[i]['LastName'])}
            candidate_email['Type'] = ""
            candidate_email_profiles.append(candidate_email)
            i += 1
        print("Difficult email non-matches created")
            
        return [candidate_name_profiles, candidate_address_profiles, candidate_email_profiles, candidate_phone_profiles]