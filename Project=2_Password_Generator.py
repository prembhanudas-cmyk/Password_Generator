import random
letter=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
digits=['0','1','2','3','4','5','6','7','8','9']
special_symbol=['!','@','#','$','%','^','&','*','(',')','_','-','+','=']
print("WELCOME TO PASSWORD GENERATOR!!!!!!!!")
n_letter=int(input("Enter the number of letter you want in your password ?\n"))
n_digits=int(input("Enter the number of digits you want in your password ?\n"))
n_special_symbols=int(input("Enter the number of special symbols you want in your password ?\n"))
password_list=[]
for i in range(n_digits):
    char=random.choice(letter)
    password_list+=char
for i in range(n_digits):
    numbers=random.choice(digits)
    password_list+=numbers
for i in range(n_special_symbols):
    symbol=random.choice(special_symbol)
    password_list+=symbol
print(password_list)
random.shuffle(password_list)
password=""
for char in password_list:
    password+=char
print(password)