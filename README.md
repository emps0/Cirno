Cirno Language
  Cirno is a simple interpreted language designed for educational purposes. It is inspired by stack-based languages and has basic functionality for input/output and stack manipulation. This language was inspired by the character Cirno (チルノ) from the game Touhou.

Features
  Stack-based: Cirno operates on a stack data structure, allowing users to push and pop values onto/from the stack.
  Input/Output: Cirno supports simple input/output operations, allowing you to print messages and receive user input. 
  Functions: Cirno has basic functions for printing (say), receiving input (hear), and performing multiplication (multiply).

Syntax
Printing a message
  The say function is used to print messages. Messages should be enclosed in single quotes.
  Example:
    say 'Hello, world!'
    
Receiving Input
  The hear function is used to receive input from the user. Input can be either a string or an integer. It stores the information in the stack.
  
Multiplying
  The multiply function is used to multiply values on the stack. It takes an integer argument specifying the number of arguments to multiply from the stack.
  The result is also stored in the stack

Usage 
  Write your Cirno code in a text file, e.g., program.cirno.
  Run the Cirno interpreter with your code file as an argument:
  example:
    cirno.py program.cirno
