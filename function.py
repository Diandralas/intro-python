def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input('Whats your name?')
first_name_initial = get_initial(first_name)
print(first_name_initial)