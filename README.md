# Software Development 1
## Coursework 2
### Last Updated: 15 November 2022 by Skeeper Loyaltie

**The prestigious football club who originally hired our Software Development company is very pleased with the outcome and has requested an extension.** Taking the program that you have crafted for coursework 1, you are asked to add the following functionality (up to 72 points, depending on scoring an “Excellent” score in each rubric component):
1.	Functions (8 points): Split and pack up your coursework 1 code into functions. The program must contain a main() function and at least two other functions called “calculate_rating()” and “calculate_salary()”.Use the main() function to call the other functions to receive the 6 player’s skill ratings, calculate the player’s score and their salary range.
2.	Program expansion (8 points): Adjust your program to ask users to enter a player ID (2 digit number), name and date-of-birth (D.o.B) by sequence, before asking for the 6 skills from coursework 1 (speed, shooting, passing, defending, dribbling, physicality). D.o.B should be in ISO format YEAR-MONTH-DATE.
3.	Loop your code (8 points): Your program should use a loop to ask for the information of three players, or until the input for user ID is “end”. 
4.	Calculate the players' overall ratings and store it for later use (2 points).
5.	Calculate the players' salary ranges and store it for later use (2 points).
6.	Calculate players' ages (8 points): According to each user’s year of birth, your program should calculate the age of the player and store it for later use. Hint: the library datetime can be used here to make your job easier.
7.	Tabulate (8 points): Display a table that summarises the input data (ascending order with user ID) using the tabulate library. 

8.	File writing (8 points): Save the table into a new local file named “players.txt”
9.	Make sure that you a. Implement robust input validation for a player's ID, D.o.B., and ratings. Your program should give a warning that says "The rating you entered was invalid" for any input errors (6 points) b. Display use of appropriate data structures for storing player information (5 points) c. Display use of appropriate code structures for implementing the functionality (5 points)

10.	Distinction Advanced Function: Once everything in requirements 1-9 has been completed, for a distinction grade, extend your program with one more function called advanced(). This function should a.be a complimentary main() method that, instead of taking user input, uses the provided file as input. b.accept in its argument (filename) the name of the text file to read. c. read the user information record from the provided file “PlayerData.txt”, which contains player IDs, names, and date-of-births. The function should then use this data as the input for the program. d. call all the other functions used and produces a text file output (requirement 8).
