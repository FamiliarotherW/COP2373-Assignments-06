# WinsonMaProgrammimgExercise06.py

import re

def validate_phone(phone):
    # Validates phone number
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return re.match(pattern, phone) is not None
    
def validate_ssn(ssn):
    # Social Security number
    pattern =  r'^\d{3}-\d{2}-\d{4}$'
    return re.match(pattern, ssn) is not None
    
def validate_zip(zip_code): 
    # Zip code
    pattern = r'^\d{5}(?:-d{4})?$'
    return re.match(pattern, zip_code) is not None
    
def main():
    # Prompt user input and validates phone, zip, and SSN
    phone = input("Enter phone number: (XXX-XXX-XXXX): ")
    ssn = input("Enter SSN (XXX-XX-XXXX): ")
    zip_code = input("Enter Zip code (XXXXX or XXXXX-XXXX): ")
    
    if validate_phone(phone):
        print("Phone number is valid.")
    else:
        print("Phone number is invalid.")
        
    if validate_ssn(ssn):
        print("Social Security Number is valid.")
    else:
        print("Social Security Number is invalid.")
        
    if validate_zip(zip_code):
        print("Zip code is valid.")
    else:
        print("Zip code is invalid.")
        
if __name__ == "__main__":
    main()
    