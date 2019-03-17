while True:
    question_exempt = input('Are you been paid as an exempt? ')
    if question_exempt.lower() == 'no':
        input_pay_rate = input('Please enter ho much you make per hour: ')
        input_hourse = input('Please enter ho many hours you work per week: ')
        break
    elif question_exempt.lower() == 'yes':
        exempt = input('Please enter how much you been paid per week ')
        break
    else:
        print('Invalid input. Please try again.')

if question_exempt.lower() == 'no':
    gros_income = ((int(input_pay_rate)*int(input_hourse))*52)
elif question_exempt.lower() == 'yes':
    gros_income = (int(exempt)*52)

print (gros_income)

if gros_income in range (0,8500):
    state_tax = (gros_income*0.04)
elif gros_income in range (8500,11700):
    state_tax = (gros_income * 0.045)
elif gros_income in range (11700,13900):
    state_tax = (gros_income * 0.0525)
elif gros_income in range (13900,21400):
    state_tax = (gros_income * 0.059)
elif gros_income in range (21400,80650):
    state_tax = (gros_income * 0.0633)
elif gros_income in range (80650,215400):
    state_tax = (gros_income * 0.0657)
elif gros_income in range (215400,1077550):
    state_tax = (gros_income * 0.0685)
elif gros_income in range (1077550,10775500):
    state_tax = (gros_income * 0.0685)

net_income = (gros_income - state_tax)

print('Your net income is: ', net_income)
print('Your state tax is: ', state_tax)
