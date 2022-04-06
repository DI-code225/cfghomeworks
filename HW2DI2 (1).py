#Q1:wrong code
chairs ='15'
nails =4
total_nails = chairs * nails
message ='I need to buy {} nails'.format(total_nails)
print(message)
# The above code will produce the repetition of the string "15"  4 times, as the data type is not right  for the math operation. variable chair should be defined with an integer.
# The right code is below:
chairs = 15
nails = 4
total_nails = chairs * nails
message = 'I need to buy {} nails'.format(total_nails)
print(message)
#Q2: code with mistake:
my_name = Penelope
my_age = 29
message ='My name is {} and I am {} years old'.format(my_name,my_age)
print(message)
# the problem is the missing punctuation marks for the string in "Penelope"
#the correct code is below:
my_name = "Penelope"
my_age =29
message ='My name is {} and I am {} years old'.format(my_name,my_age)
print(message)
#Q3:
boxes = int(input("How many boxes do you have?"))
eggs_per_boxe = 6
total_eggs = boxes * egg_per_boxes
eggs_per_omelette = 4
total_omelettes = total_eggs // eggs_per_omelette
omelettes = int(total_omelettes)
output = 'You can make {} omelettes with {} boxes of eggs'.format(omelettes, boxes)

print(output)




#Q4:
# Task 1 - Replace the (.) character with (!) instead. Output should be “I love coding!”
my_str ="I love coding."
my_str = my_str.replace(".", "!")
print(my_str)
# Task 2 - Reassign str so that all of its characters are lowercase.
my_str_1 ="EVERY Exercise Brings Me Closer to Completingmy GOALS."
my_str_1 = my_str_1.lower()
print(my_str_1)
# Task 3 - Output whether this string starts with an A or not
my_str_2 = "We enjoy travelling"
answer = my_str_2.startswith("A")
print(answer)
# Task4 - What is the length of the given string?
my_str_3="1.458.001"
ans_2 = len(my_str_3)
print(ans_2)
#Q5:
# Question 4

# Task 1 - Slice the word so that you get "thon".
wrd = "Python"
ans_1 = wrd[2:]
print(ans_1)

# Task 2 - Slice the word until "o". (Pyth)
wrd = "Python"
ans_1 = wrd[:4]
print(ans_1)

#Task3- Now try to get "th" only.
wrd = "Python"
ans_1 = wrd[2:4]
print(ans_1)

# Task 4 - Now slice the word with steps of 2, excluding first and last characters
wrd = "Python"
ans_1 = wrd[1:2:len(wrd)-1]
print(ans_1)

#Q6:
fornumberinrange(100):
output ='o'* number
print(output)
#It prints 'o' letter endless number of times, every time starting with the next number

#Q7:
def calculate_vat(amount):
amount *1.2
total = calculate_vat(100)
print(total)
#there's to return statement. Correction below:
def calculate_vat(amount):
    return amount * 1.2
total = calculate_vat(100)
print(total)
#Q8:
