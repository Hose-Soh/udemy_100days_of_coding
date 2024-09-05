def format_name(f_name, l_name):

    # function will return name if first name or last name provided
    if f_name == "" and l_name=="":
        return "Invalid Input"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name(input("What is your first name?:" ), input("What is your last name?: ")))
