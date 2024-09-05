def format_name(f_name, l_name):
    """

    :param f_name: (string) first name
    :param l_name: (string) last name
    :return: (string) concatenation of f_name and l_name both in title case
    """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)