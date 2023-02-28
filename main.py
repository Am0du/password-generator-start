#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#picks random alphabets, numbers, symbols
pass_alp = []
for letter in range(0, nr_letters ):
  random_alp = random.randint(0,25)
  pass_alp.append(letters[random_alp])

pass_num = []
for number in range(0, nr_symbols):
  random_num = random.randint(0, 9)
  pass_num.append(numbers[random_num])

pass_sym =[]
for symbol in range(0, nr_numbers):
  random_sym = random.randint(0,8)
  pass_sym.append(symbols[random_sym])

#joins the generated password
password = []
password.extend(pass_alp)
password.extend(pass_num)
password.extend(pass_sym)

#Shuffles the password
random.shuffle(password)

#converts to strings
final_password = "".join(password)
print(f"Your password is: {final_password}")
  


                              