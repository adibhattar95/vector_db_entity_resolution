import string

MALE_SUFFIXES = ['', 'Jr', 'Sr', 'II']
GENDER_FEMALE = ['Female', '']
GENDER_MALE = ['Male', '']
PREFIX_FEMALE = ['Miss.', 'Ms.', 'Mrs.', 'Dr.', '']
PREFIX_MALE = ['Mr.', 'Dr.', '']
MIDDLE_NAME = list(string.ascii_uppercase)
MIDDLE_NAME.append('')
CITIES = {
    'NY': ['New York City', 'Buffalo', 'Rochester', 'Syracuse', 'Albany'],
    'CA': ['Los Angeles', 'San Francisco', 'San Diego', 'Sacramento', 'San Jose'],
    'TX': ['Houston', 'Dallas', 'Austin', 'San Antonio', 'Fort Worth'],
    'FL': ['Miami', 'Orlando', 'Tampa', 'Jacksonville', 'Fort Lauderdale'],
    'IL': ['Chicago', 'Aurora', 'Rockford', 'Naperville', 'Joliet']
}