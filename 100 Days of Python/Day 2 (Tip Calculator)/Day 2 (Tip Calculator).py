print('Welcome to the tip calculator.')
total_bill = float(input('What was the total bill?\n$'))
tip_percentage = int(input('What percentage tip would you like to give? 10, 12, or 15?\n'))
final_tip_percentage = total_bill * (1 + tip_percentage / 100)
total_people = int(input('How many people to split the bill?\n'))
result = final_tip_percentage/total_people
print(f'Each person should pay: ${result}')
