import random

def guessing_game ():
    answer = random.randint (0,100) #busca entre el 0 al 100
    while True:
        user_guess = int(input("cual es el numero? : "))
        if answer==user_guess:
            print("adivinaste!!")
            break
        elif answer<user_guess:
            print("el numero suyo es mayor")
        else:
            print("el numero suyo es menor")
guessing_game() #invocando la funcion 