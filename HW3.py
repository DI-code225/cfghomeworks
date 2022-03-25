#Task 1 Q1:
#1. Ask you if it is raining using input()
#2. If the input is 'y', it should output 'Take an umbrella'
#3. If the input is 'n', it should output 'You don't need an umbrella'
weather_check = input('Is it raining? y/n ')
if weather_check == 'y':
    print("You should take an umbrella: {}".format(weather_check))
elif weather_check == 'n':
    print("You don't need an umbrella: {}".format(weather_check))
else:
    print("only y or n can help with your umblrella choice")

#Q2:
#mistake 1 boat coast variable is missing underscore. Mistake 2# the last print satement wasn't closed with a brackets)
#m3 it doesn't work with st or int so we need a float
my_money = input('How much money do you have? ')
can_afford = float(my_money) >= 25
if can_afford == True:
    print('You can afford the boat hire')
else:
    print('You cannot afford the board hire')

#Q3:
book_year = int(input('Welcome to our Antique Book Categoriser! Please enter the book publishing year : '))
range_1 = range(1800, 1810)
range_2 = range(1810, 1820)
range_3 = range(1820, 1830)
range_4 = range(1830, 1840)
range_5 = range(1840, 1850)
range_6 = range(1850, 1860)
range_7 = range(1860, 1870)
range_8 = range(1870, 1880)
range_9 = range(1880, 1890)
range_10 = range(1890, 1900)
range_11 = range(1900, 1910)
range_12 = range(1910, 1920)
range_13 = range(1920, 1930)
range_14 = range(1930, 1940)
range_15 = range(1940, 1950)
range_16 = range(1950,1960)

if book_year in range_1:
    print('This book was published in the 18th century,aughts ')
elif book_year in range_2:
    print('This book was published in the 18th century,tens ')
elif book_year in range_3:
    print('This book was published in the 18th century,twenties ')
elif book_year in range_4:
    print('This book was published in the 18th century,thirties ')
elif book_year in range_5:
    print('This book was published in the 18th century,fourties ')
elif book_year in range_6:
    print('This book was published in the 18th century,fifties ')
elif book_year in range_7:
    print('This book was published in the 18th century,sixties ')
elif book_year in range_8:
    print('This book was published in the 18th century,seventies ')
elif book_year in range_9:
    print('This book was published in the 18th century,eighties ')
elif book_year in range_10:
    print('This book was published in the 18th century,nineties ')
elif book_year in range_11:
    print('This book was published in the 19th century,aughts ')
elif book_year in range_12:
    print('This book was published in the 19th century,tens ')
elif book_year in range_13:
    print('This book was published in the 19th century,twenties ')
elif book_year in range_14:
    print('This book was published in the 19th century,thirties ')
elif book_year in range_15:
    print('This book was published in the 19th century,fourties ')
elif book_year in range_16:
    print('This book was published in the 19th century,fifties ')
else:
    print(book_year, 'this is not the applicable year, we only sell 18th and 19th (till50s) centuries books')

#Task 2
#Q1in lists we start counting from zero, so in order to know the value of the first element in the list we need to indicate 0 instead of 1
shopping_list = [
	"oranges",
	"cat food",
	"sponge cake",
	"long-grain rice",
	"cheese board",
]
print(shopping_list[0])
#you'll get oranges

#Q2
chocolates = {

	'white': 1.50,

	'milk': 1.20,

	'dark': 1.80,

	'vegan': 2.00,

}
price_check = input('Check out our chocolate prices! Type one of 4 options: white, milk, dark or vegan and you\'ll see the price. Let\'s go! Type chocolate option: ')
if price_check == 'white':
    print(chocolates['white'])
elif price_check == 'milk':
	print(chocolates['milk'])
elif price_check == 'dark':
	print(chocolates['dark'])
elif price_check == 'vegan':
	print(chocolates['vegan'])
else:
	print(' we don\'t have this chocolate')



#Q3 Lottery game

import random

winning_numbers = random.sample(range(1, 99), 7)
counter = 1

print("")
print("Enter your 7 numbers between 1 and 99 and win our monetary prize today")
print("")
user_nums = []

while counter < 8:
    print("Please type in the ", counter, " number")
    i = input("select number ")
    print('Your selected number is', i)

    if ((i not in user_nums) and (1 <= int(i) <= 99)):
        user_nums.append(i)
        counter += 1
    else:
        print("Please enter a valid, non-duplicate number between 1 and 99!")

print('Your chosen numbers are', user_nums)
print('The winning numbers today are', winning_numbers)

n = 0
for i in user_nums:
    if i in winning_numbers:
        n += 1
        print("You got %d numbers right out of 7" % n)
    if n < 3:
        print("Unfortunately, you did not win this time. Try again")
        break
    elif n == 3:
        print("Yahoo! You won 20£")
    elif n == 4:
        print("Yahoo! You won 40£")
    elif n == 5:
        print("Wow! You won 100£")
    elif n == 6:
        print("OMG! You have won 100000£")
    elif n == 7:
        print("You won\t believe it! You won 10000000£")

#Task3
# Q1 pip-is a python package index. pip helps install and manage packages and libriries in python.
#pip is great because it checks for the latest version automatically and launches the download from a to z without users step by step approvals.

#Q2
#poem = 'I like Python and I am not very good at poems'
#with open('poem.txt', 'r') as poem_file:
	#poem_file.write(poem)

#you are trying to read the file instead of writing into the file. below is the right option:

file = open('poem.txt', 'w')

file.write(" I like Python and I am not very good at poems")
file.close()

#Q3 Elton Song
file = open('elton.txt', 'w')
file.write(
"You could never know what it's like "
"\n Your blood like winter freezes just like ice "
"\n And there's a cold lonely light that shines from you"
"\n You'll wind up like the wreck you hide behind that mask you use"
"\n And did you think this fool could never win? "
"\n Well look at me, I'm coming back again"
"\n I got a taste of love in a simple way"
"\n And if you need to know while I'm still standing, you just fade away"
"\n Don't you know I'm still standing better than I ever did"
"\n Looking like a true survivor, feeling like a little kid"
"\n I'\m still standing after all this time"
"\n Picking up the pieces of my life without you on my mind"
"\n I'\m still standing (Yeah, yeah, yeah)"
"\n I'\m still standing (Yeah, yeah, yeah)")
file.close()

file = open('elton.txt', 'r')
search_word = 'still'

with open('elton.txt', 'r') as text:
    for line in text:
        line = line.strip()
        words = line.split()

        for word in words:
            if (word == search_word):
               print(line)

#pokemons in a separate file
