# PCC_Day3

Chapter 4 is an extension of Chapter 3 where it defined list and provided syntax to use them, chapter 4 focuses on working with list, such as looping through them, using range function, min/max/sum, slicing, looping through slice .

### Chapter 4 Notes: 

Looping allows the same action or set of actions with every item in the list 

for loop: 

steps of using for loop: 
1. defining a list
    - movies = ["Inception", "Killers of The Floor Moon", "Wolf Of Wall Street"]
2. define for loop
    - for movie in movies: tells Python to retrieve the first value from the list <singular variable> and associate it with the <plur variable>.
       - `for` activates the loop 
       - insert singular version of list. (movie is a singular from movies) 
       - in tells Python which list
       - must end with a colon. 
3. Give the loop an action (must be indented after the colon. it's called inside the loop)
    - print(movie) –– prints out every movie on a single line

movies = ["Shutter Island", "Killers of The Floor Moon", "Wolf Of Wall Street"]

for movie in movies: 
    print(f"{movie.title()}: staring Leonard Dicaprio")

You can use as many lines as you like in for loops (anything indented inside the loop)
 - for movie in movies: 
    print(f"{movie.title()}: staring Leonard Dicaprio\n")
    print(f"{movie.title()}: directed by:martin scorsese)

• working with set of numbers, range() function generates a series of numbers. 
• Python uses off-by-one behavior where range() function causes Python to start counting at the first value, and it stops when it reaches the second value you.
 - for value in range(1,5) –– 1 through 4 would be printed. to print 1 - 5 range(1,6)
 -  for value in range(6) – one argument can be passed in range if starting list from 0. 

a list of numbers can be created with range
- rankings = list(range(1,6)) 
- print(rankings) – results: [1,2,3,4,5,]

a third argument in range would skip numbers in a given range
 - double = list(range(2, 11,2)) - 2 to 10 of only even numbers. 

 use separate variables for the loop counter and calculations to keep your code clear and avoid overwriting the loop variable.
 
 multiplied = []

 for number in range(1,11): – number = loop variable
    multiplied.append(number * 2) – append calculations directly into list
    print(number)

minimum, maximum, and sum of a list of numbers can easily be found using min,max and sum. 
digits = [222,333,444,555,777,888,999,000]
- min(digits) – results of smallest number
- max(digits) – results of highest number
- sum(digits) – results of numbers added together

slicing: working with a specific group of items inside a list (instead of 1 element multiple)
slicing requires specifying the index of first and last elements to be used  (similar to range(), Python stops one item before the second index)
- players = ["Lebron James", "Luka Donic", "Austin Reaves", "Christian Wood", "Dalton Knnect", "Jared Vando"]
- print(players[0:3]) - results ["Lebron James","Luka Donic","Austin Reaves]

omit the first index in a slice, Python automatically starts slice at the beginning of the list
- print(players[:4])

omit the second index in a slice, Python automatically starts slice at the idex start to the end of the list
- print(players[1:])

negative index returns an element a certain distance from the end of a list
- print(players[-3:]) - results: output the last three players on the roster. 

for loops can be used to slice through elements in a list
for player in players[:3]: – Python doesn't loop through entire list of elements, but only the first 3.
    print(player)