patients = []


def patient_intake():
# This will take in user input and check for possible entry errors.
    first_name = input("What is the patients first name?").lower()
# This will test user input for any numbers
    first_name_int_test = any(map(str.isdigit, first_name))
# This will test for input errors such as blanks, no entry, or numbers and loop as long
# as those errors exist
    while first_name.isspace() == True or first_name == "" or first_name[0] == " " or first_name_int_test == True:
        first_name = input("INVALID ENTRY. No blanks, spaces, or numbers. What is the patients first name?").lower()
        first_name_int_test = any(map(str.isdigit, first_name))
# This is the same block of code/tests as first_name but with a different variable name
    middle_initial = input("What is the patients middle initial?").lower()
    middle_initial_int_test = any(map(str.isdigit, middle_initial))
    while middle_initial.isspace() == True or middle_initial == "" or middle_initial[0] == " " or middle_initial_int_test == True:
        middle_initial = input("INVALID ENTRY. No blanks, spaces, or numbers. What is the patients middle initial?").lower()
        middle_initial_int_test = any(map(str.isdigit, middle_initial))
# This is the same block of code/tests as first_name but with a different variable name
    last_name = input("What is the patients last name?").lower()
    last_name_int_test = any(map(str.isdigit, last_name))
    while last_name.isspace() == True or last_name == "" or last_name[0] == " " or last_name_int_test == True:
        last_name = input("INVALID ENTRY. No blanks, spaces, or numbers. What is the patients first name?").lower()
        last_name_int_test = any(map(str.isdigit, last_name))
##########################################################################################################
# This will take user input and run tests of the entry
# The tests include str character and unreasonable numbers
# An example of an unreasonable number is entering 13 for the month or 35 for the day of the month
# The loops will run as as long as the the user input tests return errors
    while ValueError:
        try:
            dob_month = int(input("What month was the patient born in (MM)? "))
            while dob_month > 12:
                dob_month = int(input("""INVALID ENTRY.
Please re-enter patients DOB month in numerical form: """))
            dob_day = int(input("What day is the patient born on (DD)? "))
            while dob_day > 31:
                dob_day = int(input("""INVALID ENTRY.
Please re-enter the numerical day the patient was born on: """))
            if dob_month == 4 or dob_month == 6 or dob_month == 9 or dob_month == 11:
                while dob_day > 30:
                    dob_day = int(input("""INVALID ENTRY. There are only 30 days in this month.
Please re-enter patients DOB day: """))
            if dob_month == 2:
                while dob_day > 29:
                    dob_day = int(input("""INVALID ENTRY. There are only 29 days in this month.
Please re-enter patients DOB day: """))
            dob_year = int(input("What year was the patient born (YYYY)?"))
            while dob_year < 1885 or dob_year > 2021:
                dob_year = int(input("""INVALID ENTRY. Year entered is unreasonable.
Please re-enter year: """))
        except ValueError:
            print("INVALID ENTRY. Must be a numerical entry. Please re-enter:")
        else:
            break
# This will consolidate the variables for clean entry as one list element into a database
    date_of_birth = dob_month + dob_day + dob_year
# This will consolidate all of the user input into what will be stored in the database
    new_patient = [first_name, middle_initial, last_name, date_of_birth]
# this will check the new_patient against elements already in the patients list or db
# If there is a match, the new_patient is not stored in the list or db
# If there is no match, the new_patient will be added to the list or db
    if new_patient in patients:
        print()
        print("%s %s %s is already a patient" % (first_name.title(), middle_initial.title(), last_name.title()))
        print()

    else:
        patients.append(new_patient)
        print()
        print("%s %s %s  has been added as a new patient." % (
        first_name.title(), middle_initial.title(), last_name.title()))
        print()


patient_intake()
print(patients)
patient_intake()
print(patients)
###############################################################################################################
#                             These are just some historical notes
# dob_year = int(input("what year was the patient born"))
# this is checking for entry of string and not integer
# while ValueError:
#     try:
#         dob_year = int(input("What year was the patient born?:"))
#     except ValueError:
#         print("INVALID ENTRY. Must be a numerical entry. Please re-enter:")
#     else:
#         break
# this is checking for unreasonable year AND string entry
# if dob_year < 1885 or dob_year > 2021:
#     while ValueError:
#         try:
#             dob_year = int(input('INVALID ENTRY. Please re-enter year:'))
#         except ValueError:
#             print("INVALID ENTRY. Must be numerical entry. Please re-enter.")
# elif dob_year < 1885 or dob_year > 2021:
#     while ValueError or dob_year < 1885 or dob_year> 2021:
#         try:
#             dob_year = int(input('INVALID ENTRY. Please re-enter year:'))
#         except ValueError:
#             print("INVALID ENTRY. Must be numerical entry. Please re-enter.")
#         else:
#             break
# first_name = input("What is the patients first name?").lower()
# while first_name[0] == "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
#     first_name = input("INVALID ENTRY: ")
# while first_name.isspace() == True or first_name == "" or first_name[0] == " ":
#     first_name = input("INVALID ENTRY. No Blanks or spaces. What is the patients first name?").lower()
# user = input("Enter string: ")
# test = any(map(str.isdigit, user))
#
# while test == True:
#     user = input("INVALID ENTRY. Enter string: ")
#     test = any(map(str.isdigit, user))