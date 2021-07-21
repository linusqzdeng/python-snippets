# function that has too many parameters

def print_student_profile(
        name, contact, studentID, 
        gender = 'boy', major = 'Finance'
        ):
    print('My name is ' + name)
    print('I am a ' + gender)
    print('I am studying in ' + major)
    print('Phone number: ' + str(contact) + ' Student ID: ' + str(studentID))

print_student_profile('Linus', 13060762710, 20163604037, 'boy', 'Real estate & Finance')
print_student_profile('Chris', 'unknown', 'unknown')