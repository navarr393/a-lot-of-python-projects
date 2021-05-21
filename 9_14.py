from random import choice
def get_winning_ticket_number():
    series = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D"]
    number_choice = series[0:10]
    letter_choice = series[10:14]

    num_sec = (choice(number_choice) + choice(number_choice) + choice(number_choice) + choice(number_choice))
    lett_sec = (choice(letter_choice) + choice(letter_choice) + choice(letter_choice) + choice(letter_choice))

    win_ticket = num_sec + lett_sec
    return win_ticket

winning_ticket_list = []

for i in range(10):
    winning_ticket_list.append(get_winning_ticket_number())

print(winning_ticket_list)