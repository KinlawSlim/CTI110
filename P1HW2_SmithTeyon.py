# Total amount of expenses
# 9/26/2022
# CTI-110 P1HW2 - Travel Expense
# Teyon Smith
budget = 1200
desto = 'Asheville'
gas = 250
hotel = 300
food = 200
totalCost = 0
print('This program calculates and displays travel expenses')
print('Enter Budget:',budget)
print('Enter your travel destonation:',desto)
print('How much do you think you will spend on gas?',gas)
print('Approximately, how much will you need for accomodation/hotel?',hotel)
print('Last, how much do you need for food?',food)
totalCost = (gas + hotel + food)
print('Total Expenses:$', f'{totalCost:.2f}')
balance = (budget - totalCost)
print('Remaining Balance:$', f'{balance:.2f}')