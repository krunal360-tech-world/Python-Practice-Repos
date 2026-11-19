# Python-Practice-Repos
A collection of beginner-friendly Python projects built to practice programming fundamentals, strengthen problem-solving skills, and gain hands-on coding experience.

📌 About

This repository contains small Python projects developed as part of my programming journey. Each project focuses on applying core Python concepts through practical implementation.
1. Simple_Calculator

A simple calculator program created using Python as part of my Python practice projects.

Features:
- Takes two numbers as input from the user.
- Performs addition, subtraction, multiplication, and division.
- Allows users to select an operation using menu options.
- Uses `match-case` to perform the selected operation.
- Handles invalid input using `try-except`.

Concepts Used:

- Variables
- User Input
- Type Conversion (`int()`)
- Arithmetic Operators
- `match-case` Statements
- Exception Handling (`try-except`)
- F-Strings



2. rock_paper-scissors

A simple Rock Paper Scissors game created using Python as part of my Python practice projects.

Features:
- Choose Rock, Paper, or Scissor.
- Computer randomly selects its choice.
- Displays ASCII art for both choices.
- Declares the result as Win, Lose, or Draw.
- Checks for invalid input.

Concepts Used:
- Variables and Lists
- User Input
- Conditional Statements (`if`, `elif`, `else`)
- Random Module
- ASCII Art
- F-Strings

### 3. Password Generator 🔐

A simple password generator built using Python as part of my Python practice projects.

**Features:**

- Allows users to choose the number of letters, numbers, and symbols.
- Generates random letters, numbers, and symbols.
- Shuffles the generated characters to create a mixed password.
- Displays the generated password.

**Concepts Used:**

- Variables and Lists
- User Input (`input()`)
- Type Conversion (`int()`)
- For Loops
- Random Module (`random.choice()`, `random.shuffle()`)
- String Concatenation
- List Conversion (`list()`)
- String Joining (`join()`)

### 4. Caesar Cipher 🔐

A simple text encryption and decryption program built using Python as part of my Python practice projects.

**Features:**

- Encrypts text using a shift key.
- Decrypts encrypted text using the same shift key.
- Preserves spaces and special characters.
- Uses a looping mechanism to allow users to perform multiple operations.
- Allows users to continue or exit the program.

**Concepts Used:**

- Variables and Lists
- Functions
- User Input (`input()`)
- Conditional Statements (`if`, `else`, `elif`)
- For Loops and While Loops
- String Concatenation
- List Methods (`index()`)
- Membership Operator (`in`)
- Modulo Operator (`%`)
- Boolean Values (`True`, `False`)

### 5. Blind Auction Program

## Description
This is a simple Python-based Blind Auction Program where multiple bidders can enter their names and bid prices. The program determines the highest bidder and announces the winner after all bidding participants have entered their bids.

## Concepts Used
- Dictionaries
- `while` loop
- `for` loop
- Conditional statements (`if-elif`)
- Functions
- User input (`input()`)
- Type conversion (`int()`)
- `os` module for clearing the terminal screen

## How It Works
1. An empty dictionary named `data` is created to store bidder names and their bid prices.
2. The `check()` function takes the dictionary as an argument.
3. Inside the function:
   - `highest` is initialized to `0`.
   - `winner` is initialized as an empty string.
   - A `for` loop iterates through all bidders.
   - The bid price of each bidder is compared with the current highest bid.
   - If the current bid is higher, `highest` and `winner` are updated.
4. A `while` loop allows multiple users to enter their names and bid prices.
5. After each bid, the user is asked whether another person wants to bid.
6. If the answer is `yes`, the terminal screen is cleared using `os.system('cls')`.
7. If the answer is `no`, the bidding process stops and the `check()` function announces the winner.

## How to Run
1. Make sure Python is installed on your system.
2. Clone this repository or download the project file.
3. Open the terminal in the project directory.
4. Run the following command:

```bash
python blind_auction.py
```

## Note
- This program uses `os.system('cls')`, which works on Windows terminals.
- If two bidders enter the same highest bid, the first bidder with that amount is considered the winner.
- Enter valid integer values for bid prices.
