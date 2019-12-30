from datetime import datetime

current_date = datetime.now()
print(current_date)

birthdate = input('whats is your birthday?')

birthday = datetime.strptime(birthdate, '%d/%m/%Y')
print(birthday)

