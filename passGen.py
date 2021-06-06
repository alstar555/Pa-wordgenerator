#unique but easy to remember password generator based on what site you're on

import getpass
#customization
new = input("new password (y/n): ")
password_seed = getpass.getpass("Enter your usual password as a seed: ")
site_name = input("name of website: ")
ending = input("trailing chars/nums (s to skip): ")

print("***for security customize the encoding symbols in the code***")
#for security add you're own dictionary or change the symbols in this symbol_dict 
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
# ^^^ customize the symbol_dict

#encoding magic
if ending == 'ending = "$!"s':
     ending = ""
password_seed = password_seed.capitalize()
password = site_name + password_seed + ending
password = password[:1].upper() + password[1:]
for letter in password:
    if letter in symbol_dict:
        password = password.replace(letter, symbol_dict[letter])

#stores sites in text doc to remember
if new == "y":
    mysites = open("siteList.txt", "a+")
    mysites.write(site_name + "\n")

print("Generated Pa$$woRd: ", password)
