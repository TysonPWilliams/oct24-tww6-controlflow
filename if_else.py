is_raining = False

# # Could also say "if is_raining:""
# if is_raining == True: 
#     print("It's raining")

# else:
#     print("It is not raining!")

# if not is_raining:
#     print("It is not raining")

# Ternary
print('I need an umbrella' if is_raining else 'No need for an umbrella')


# Else if

# >80 -> HD
# 70 - 79 -> D
# 60 - 69 -> C
# 50 - 59 -> P
# <49 -> F

marks = 49

if marks >= 80:
    print("HD")
elif marks >= 70:
    print("D")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("P")
else:
    print("Fail!")
     

# Nested if

# 2 states -> State1 and State2
# State1: >=18 can vote
# State2: >=21 can vote

# state = 'State2'
# age = 19

# # Display whether they can vote or not
# # if (state == 'State1' and age >= 18) or (state == 'State2' and age >= 21)
# if  state == "State1":
#     if age >= 18:
#         print('Can vote in State 1')
#     else:
#         print('Cannot vote in State 1')
# else:
#     if age >= 21:
#         print('Can vote in State 2')
#     else:
#         print('Cannot vote in State 2')

day_of_week = 5

# if day_of_week == 1:
#     print('Monday')
# elif day_of_week == 2:
#     print('Tuesday')

# match day_of_week:
#     case 1:
#         print('Monday')
#     case 2:
#         print('Tuesday')
#     case 3:
#         print('Wednesday')
#     case 4:
#         print('Thursday')
#     case 5:
#         print('Friday')
#     case _:
#         print("That is not a weekday!")

# 1-5: Weekday
# 6, 7: Weekend
# Anything else: Error Message
match day_of_week:
    case 1 | 2 | 3 | 4 | 5:
        print('Weekday')
    case 6 | 7:
        print('Weekend')
    case _:
        print('Error: Not a valid day number!')
    