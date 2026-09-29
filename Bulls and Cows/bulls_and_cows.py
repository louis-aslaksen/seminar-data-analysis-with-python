import random

# Random Varibale




rndm = []

"""
for i in range(4):
    rndm.append(str(random.randint(0,9)))
"""
rndm= ["1","2","2","4"]
ingame = True
tries = 0

def delete_cow_candidate(number_list, number):
    for i in range(len(number_list)):
        if number_list[i] == number:
            number_list[i] = "x"
            return number_list

def check_input(input):
    if len(input) != 4:
        return False
    for i in input:
        if not i.isdigit():
            return False
    return True

def check_bulls_cows(rndm, guess):
    tmp_rndm = rndm.copy()
    tmp_guess = guess.copy()
    bulls = 0
    cows = 0

    for i in range(len(rndm)):
        if rndm[i] == guess[i]:
            tmp_rndm[i] = "x"
            tmp_guess[i] = "x"
            bulls += 1

    for i in range(len(rndm)):
        if guess[i] in tmp_rndm:
            delete_cow_tmp = tmp_rndm.copy()
            tmp_rndm = delete_cow_candidate(delete_cow_tmp,tmp_guess[i])
            cows += 1
    return bulls, cows


#Game loop

if __name__ == '__main__':

    while ingame:
        guess = list(input("Enter your number: "))

        while not check_input(guess):
            print("Your input must consist of 4 Integers written like this: 1234")
            guess = list(input("Enter your number: "))

        bulls, cows = check_bulls_cows(rndm, guess)

        print("Bulls: " + str(bulls) + " and Cows: " + str(cows))
        tries += 1
        if bulls == 4:
            ingame = False

    print("You won!")
    if tries == 1:
        print("The secret number was " + "".join(rndm) + ". And it took you 1 try. Well done!")
    else:
        print("The secret number was " + "".join(rndm) + ". And it took you " + str(tries) + " tries. Well done!")
