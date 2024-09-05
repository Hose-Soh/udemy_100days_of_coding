def format_name(f_name, l_name):
    f_name_title = f_name.title()
    l_name_title = l_name.title()
    return f_name_title, l_name_title

output_1, output_2 = format_name("jorge mendes", "how are you?")

print(output_1, output_2)