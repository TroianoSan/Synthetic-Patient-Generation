import random
from data.identification import female_names, male_names, surnames, dni_letters, medical_signs


def generate_gender():
    '''
    Generates a random gender
    '''
    return random.choice(["H", "M"])

def generate_name(gender):
    '''
    Generates a random name based on the gender
    '''
    name = random.choice(female_names) if (gender == "M") else random.choice(male_names)
    surname1 = random.choice(surnames)
    surname2 = random.choice(surnames)
    return name, surname1, surname2

def generate_dni():
    '''
    Generates a random DNI where the number is random and the letter is calculated
    '''
    number_dni = random.randint(10000000, 99999999)
    letter_dni = dni_letters[number_dni % 23]
    return f"{number_dni}{letter_dni}"

def generate_birthdate():
    '''
    Generates a random birthdate
    '''
    return f"{random.randint(1, 31):02}/{random.randint(1, 12):02}/{random.randint(1950, 2000)}"

def generate_medical_registration_number():
    '''
    Generates a random medical registration number
    '''
    return f'{random.choice(medical_signs)} {random.randint(100000000, 999999999):09}'

def generate_identification_person():
    '''
    Return the gender and a string with the following fields:
    - Name, surname1 and surname2
    - DNI
    - Birthdate
    - Gender
    '''

    gender = generate_gender()
    name, surname1, surname2 = generate_name(gender)
    dni = generate_dni()
    birthdate = generate_birthdate()

    return name, surname1, surname2, dni, birthdate, gender

def generate_identification_doctor():
    '''
    Return the gender and a string with the following fields:
    - Name, surname1 and surname2
    - Gender
    - Medical registration number
    '''

    gender = generate_gender()
    name, surname1, surname2 = generate_name(gender)
    medical_registration_number = generate_medical_registration_number()
    

    return name, surname1, surname2, gender, medical_registration_number