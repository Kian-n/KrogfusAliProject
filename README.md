Ali Ibrahim
Krogfus Taite
CSS 335 Programming Language Paradigms
04/30/2026

Final Project, Building A Computer Language
We modeled the project using the file setup of the previous Calc Ruby DSL as inspiration. To do this, we opened a project using both our last names. The code was made using two main directories: lib and test. In addition, we had three more files, namely: bank. ebnf, banking.py, and AccountCreation.txt.
Ibrahim created the parser and evaluator classes, and the majority of the main program including the admin aspect. Taite created the lexer, token, and AST classes, the account creation text file and the I/O logic in the main program for reading and writing the file, and the specification tests. Together we worked on the EBNF and program structure and purpose
The lib directory contained a directory bank and a BankingAccount.py file. The BankAccount class defined all the variables needed for the project. We initialized the variables and set their access modifiers to ensure they were available to all other files. The bank directory contained our AST, Evaluator, Lexer, Parser, and Token classes.
 The Lexer class is the first step in processing our DSL commands. It reads the user's banking commands and breaks them into tokens. An example of this would be if a user entered a deposit command. The lexer would separate the command, account number, and amount into usable pieces. In doing this, input is checked to ensure it correctly follows the DSL format before parsing. 
The token class defines the different token types used by the banking DSL language. Tokens are created by the lexer and represent important pieces of input such as commands, account numbers, amounts, and keywords. These tokens are then fed to the parser to be parsed into an abstract syntax tree (AST).
The Parser class was used to convert the tokens produced by the Lexer into an Abstract Syntax Tree. It keeps track of the current token by returning and manages the reading of all the other tokens. Moreover, it matches the command to the root node of the AST, ensuring the command that is called is the one that runs.
The ASTNode class represents and creates the abstract syntax tree structure for the banking DSL. Each node stores crucial information on the commands being performed such as operation type and required values. This is then sent to the evaluator for reading and deciding on how the command should be executed.
 The Evaluator class reads the AST produced by the Parser and does the banking command. Using the AST root node, it determines which command to actually run. The evaluator checks the command for validity and either prints the result or a prompt explaining why the command was invalid.
The I/O logic in the main program is made to handle the text file AccountCreation.txt which contains the information for all the accounts used in the project. The file contains first name, last name, and account number all separated by whitespace only. The I/O function reads the file and allows it to be utilized in the program for deposits, withdrawals, and balance look ups. Lastly, it contains a method to write directly to the file when creating a new account. This allows previous entries to be permanently saved in the text file, even after the program concludes.
 To run the code, we used a while loop to navigate the main menu. The options were included: logging in, creating, and displaying accounts.  In addition, you can choose to exit the program or run it as the admin to see all outputs from the lexer and parser. Once a user logs into their account, our logic for display is to have them use their account number, command, and amount (if needed) to execute the DSL. I believe this makes the code easy to understand and use for non-developers.
The specification tests done for this project are located in the spec_test.py file in the test folder. These tests check functionality of the DSL commands used by the banking language. They do this by comparing expected results to the actual value returned by the test. The tests include account creation, deposits, withdrawals, balance checking, and invalid withdrawal attempts. This helps prove that the language follows the expected behavior and handles both successful and failed banking commands correctly. Account RED BULL RB052026 is created and written to the file to perform the create account test. After the test concludes it is removed as to not allow multiple entries to exist in the text file.

Works Cited
“Python Tutorial: Learn Python Programming Language.” GeeksforGeeks, GeeksforGeeks, 21 Apr. 2026, www.geeksforgeeks.org/python/python-programming-language-tutorial/.
“Python Unittest Tutorial: Unit Testing in Python Using UNITTEST Framework.” GeeksforGeeks, GeeksforGeeks, 30 Oct. 2025, www.geeksforgeeks.org/python/unit-testing-python-unittest/.




