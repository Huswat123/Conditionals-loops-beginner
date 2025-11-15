Secret_num = 5

while True:
    guess = int(input("Enter your guess:"))
    if guess == Secret_num:
        print("Corect!")
        guess = input("Enter your guess:")

    else:
        print("Wrong, try again")