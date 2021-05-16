#unique but easy to remember password generator based on what site you're on
import getpass

#customization
new = input("new password (y/n): ")
password_seed = getpass.getpass("Enter your usual password as a seed: ")
site_name = input("name of website: ")
#ending = input("trailing chars/nums (s to skip): ")
#for extra customization add you're own dictionary
symbol_dict = {
    'a' : '@',
    'h' : '#',
    'e' : '3',
    'i' : '!',
    'o' : '0',
    'b' : '6',
    's' : '$',
    't' : '+'
}

#encoding magic
# if ending == 's':
#     ending = ""
ending = "$!"
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