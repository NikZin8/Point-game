import random

condition = True
while condition == True:
    d = ['six', 'seven', 'eight', 'nine', 'ten', 'jack of Knave', 'queen', 'king', 'ace']
    c = ['6', '7', '8', '9', '10', '8', '9', '10', '11']
    you = random.choice(d)
    comp = random.choice(d)
    your_list = int(c[d.index(you)])
    comp_list = int(c[d.index(comp)])
    print('Your first card is', you)
    print('More card? press "Yes" or "No"')
    answer = input()
    while answer == 'Yes':
        card = random.choice(d)
        print('Your card is', card)
        your_list += int(c[d.index(card)])
        print('Total score is', your_list)
        print('More card? press "Yes" or "No"')
        answer = input()
    while comp_list <= 21:
        comp_list += int(c[d.index(random.choice(d))])

    if (comp_list == 21) or (comp_list > 21 and comp_list < your_list):
        print('You lose!')
    else:
        print('You win!!! Your enemy score is', comp_list)

    print('Another try? Print "Yes" or "No"')
    answer_2 = input()
    if answer_2 == 'No':
        condition = False

