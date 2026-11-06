# Python Mini Projects

A collection of five beginner-friendly Python console applications built
to practise core programming concepts such as variables, data types,
user input, conditional statements, loops, lists, and basic
calculations.

These projects use Python's built-in `input()` and `print()` functions.
They run in the terminal and do not require a frontend or external
Python packages.

## Projects

### 1. Smart Bill Calculator

A simple billing program that accepts the names and prices of three
products, calculates the subtotal, adds 18% GST, and displays the item
details and final bill.

**Features** - Accepts three product names and their prices. -
Calculates the subtotal. - Calculates GST at a fixed rate of 18%. -
Displays the GST amount and final price.

**Python concepts practised:** user input, strings, floating-point
numbers, arithmetic operations, variables, and formatted output.

### 2. Number Challenge

A number-guessing game in which the player tries to guess a predefined
number between 1 and 100. The program gives a hint when the guess is too
low or too high and counts the attempts.

**Features** - Uses a fixed secret number (`18`). - Accepts guesses from
the player. - Gives higher/lower hints. - Counts the number of valid
guesses until the correct number is found.

**Python concepts practised:** `while` loops, `if` / `elif` / `else`,
comparison operators, counters, and user input.

### 3. Smart Mini ATM

A basic ATM simulation. The user enters a PIN and, if it matches the
predefined PIN, can check the balance, withdraw money, or deposit money.

**Features** - Checks a fixed demo PIN (`2008`). - Starts with a sample
balance of 10,000. - Supports balance enquiry, withdrawal, and
deposit. - Checks that withdrawals are positive and do not exceed the
available balance. - Checks that deposits are positive.

**Python concepts practised:** conditional statements, nested
conditions, numeric input, arithmetic operations, and validation.

> This is a learning exercise only. It is not connected to a bank and
> does not provide real account security.

### 4. Smart Shopping Cart

A menu-driven shopping cart program that lets the user add items, remove
items, view the cart, sort the items, and count the total number of
items.

**Features** - Adds items to a list. - Removes a matching item if it
exists. - Displays all items currently in the cart. - Sorts the cart
alphabetically. - Displays the total number of items. - Allows the user
to exit the menu.

**Python concepts practised:** lists, list methods (`append`, `remove`,
and `sort`), loops, conditional statements, and menu-driven programming.

### 5. Smart Text Analyzer

A text-analysis program that accepts a line of text and displays basic
information and text transformations.

**Features** - Counts characters, words, vowels, and spaces. - Converts
the text to uppercase and lowercase. - Reverses the entered text.

**Python concepts practised:** strings, `len()`, `split()`, loops,
conditions, string methods, and slicing.

## Requirements

-   Python 3
-   A terminal or command prompt

No third-party libraries are required.

## How to Run

1.  Clone or download this repository.
2.  Open a terminal in the project folder.
3.  Run the Python file for the project you want to try.

For example:

``` bash
python Smart_bill_calculator.py
```

Use the corresponding filename for the other projects. If your system
uses `python3` to run Python, use:

``` bash
python3 Smart_bill_calculator.py
```

Follow the prompts displayed in the terminal.

## Repository Structure

The repository can be organized like this:

``` text
Python-Mini-Projects/
├── Smart_bill_calculator.py
├── Smart_Game_Challengers.py
├── Smart_mini_atm.py
├── Smart_shopping_cart.py
├── Smart_text_analyzer.py
└── README.md
```

## Learning Purpose

These mini projects are small exercises for strengthening Python
fundamentals. They are intended as console-based beginner projects, with
simple logic and no graphical user interface.

## Future Improvements

Possible improvements as you continue learning Python: - Add input
validation for unexpected or invalid entries. - Allow the bill
calculator to handle a variable number of products. - Let the number
challenge generate a random secret number. - Keep shopping cart data
after the program exits. - Add more text statistics, such as punctuation
and sentence counts.
