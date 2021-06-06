# PasswordGenerator
Generates unique and easy to remember passwords based on what site you're on.

The program can and should be customized to use your own symbols dictionary to avoid creating guessable passwords

# Set Up
python 3.8 is required

cd into directory where program is installed 

run passGen.py from terminal with "python passGen.py"

code should be customized on line 12:

symbol_dict = {

    'a' : '&',
    'b' : '*',
    'p' : 'd',
    'l' : '7',
    'o' : 'oo',
    'c' : '(',
    's' : '5',
    'g' : '9',
    'x' : '><'
    
}

The symbol_dict represents what each charecter will be translated to.

Currently a becomes &, b become *, etc. Replace each letter and special charecter with your own that you can remember.
