"""
4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should have one line of output containing a simple statement like I like pep- peroni pizza.
• Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!

"""

pizzas = ["meat lovers", "cheese", "peperoni" ]
for pizza in pizzas:
    print(f"{pizza} is one of my favorite pizzas.\n")
print("i really enjoy pizza.")

"""
4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
• Modify your program to print a statement about each animal, such as A dog would make a great pet.
• Add a line at the end of your program, stating what these animals have in common. You could print a sentence, such as Any of these animals would make a great pet!

"""

pets = ["dog", "cat", "hamster"]

for pet in pets: 
    print(f"a {pet} would be a good addition to the family.\n")
print("all these animals would make a great pet.")

squares = [] #empty list 

for number in range(1,10): # loops through 1 - 9
    square = number ** 2 #calculates square number 
    squares.append(square) #add squared numbers to the list
    print(square) # prints results of square roots 

multiplied = []

for number in range(1,20):
    multiplied.append(number * 2)
    print(number)

print("\n")

digits = [222,333,444,555,777,888,999]
print(f"minimum: {min(digits)}")
print(f"maximum: {max(digits)}")
print(f"sum: {sum(digits)}")

print("\n")

"""
4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.

"""

for number in range(1,21):
    print(number)

print("\n")

"""
4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
(If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)

"""

millionList = []

for number in range(1,1000001):
    millionList.append(number)
    #print(number)

print("\n")

"""
4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. 
Also, use the sum() function to see how quickly Python can add a million numbers.

"""
print(min(millionList))
print(max(millionList))
print(sum(millionList))

print("\n")

"""
4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.

"""

for odd in range(1,21,2):
    print(odd)

"""
4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.

"""

for triples in range(1,31,3):
    print(triples)

print("\n")

"""
4-8. Cubes: A number raised to the third power is called a cube. 
For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.

"""

for cubes in range(1,11):
    print(cubes**3)

print("\n")

"""
4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

"""

cubeList = []
for cubie in range(1,11):
    cubeList.append(cubie**3)
    print(cubeList)

#from notes: slicing (test)
players = ["Lebron James", "Luka Donic", "Austin Reaves", "Christian Wood", "Dalton Knnect", "Jared Vando"]
print(players[0:3])

print("\n")

#from notes: lopping through slicking
for player in players[:3]:
    print(player)
    

print("\n")

"""
4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.

"""

print(f"the first three items in the list are: {players[:3]} ")
print(f"three items from the middle of the list are: {players[:]} ")
print(f"the last three items in the the list are: {players[-3:]}\n")

"""
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite piz- zas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.

"""

newPizza = ["cheese", "sausage", "pepperoni", "meat lovers"]
friendPizza = newPizza[:]

newPizza.append("supreme")
friendPizza.append("buffalo")

print("\n")

print("My favorite pizzas are:")
for pizza in newPizza:
    print(pizza)

print("\n")

print("my friends favorite pizza are:")
for pizza in friendPizza:
    print(pizza)

print("\n")

"""
4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
• Use a for loop to print each food the restaurant offers.
• Try to modify one of the items, and make sure that Python rejects the
change.
• The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

"""

hometownBuffet = ("chicken", "mash potatoes","mac & cheese","corn bread", "green beans")
