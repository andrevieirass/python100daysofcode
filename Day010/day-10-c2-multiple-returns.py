# Functions with outputs - Multiple returns
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    
    if f_name == "" or l_name == "":
        return "You didn't provided valid inputs."
    else:
        return f"{formated_f_name} {formated_l_name}"

print(format_name(
    input("What is your first name? "),
    input("What is your last name? ")
))
