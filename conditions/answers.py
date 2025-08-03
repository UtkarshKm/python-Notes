def age(age ):
    
    if age < 13:
        print("You are a child")
    elif age >= 13 and age < 18:
        print("You are a teenager")
    elif age >= 18 and age < 65:
        print("You are an adult")
    else:
        print("You are a senior citizen")

# age(5)

def pass_checker(password):
    if len(password) >= 8:
        print("Your password is strong")
    elif len(password) >= 6:
        print("Your password is medium")
    else:
        print("Your password is weak")

pass_checker("123456")