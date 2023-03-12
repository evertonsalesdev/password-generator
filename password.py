import random
import string
import os
from datetime import date

now = date.today()
now_format = now.strftime('%d/%m/%Y')


def password_generator(len_pass = 8):
    number_options = string.digits
    strings_options = string.hexdigits
    options = number_options + strings_options

    password_user = ""

    for i in range(0, len_pass):
        # Criando um array [0, 1 , 2 , 3 , 4 , 5 , 6 , 7]
        digit = random.choice(options)
        password_user = password_user + digit
    return password_user    

choice_user = input('Quantos digitos na senha? ')

if choice_user.isdigit():
    choice_user = int(choice_user)
else:
    print('Inválido!')
    quit()

resposta = password_generator(len_pass = choice_user) 

def save_password():
    with open('password.txt','w',newline='') as save_password:
        for password in resposta:
            save_password.write(password)
    return password

save_arquivo = save_password()

        
print(f'Senha gerada: {resposta}\n\nSua senha foi gerada no dia {now_format}\n\nSenha armazenada no arquivo password.txt')