import time
import hmdraw
import hmdictionary
import hmtop_update

def pick_secret():
    '''bez argumentów
        wybiera randomowo słow0
        return str: word'''
    import random
    temp_lista = []
    with open('capitals.txt') as file:
        for line in file:
            line = line.strip()
            temp_lista.append(line)
    return random.choice(temp_lista)


def get_hashed(sentence):
    ''' arg: word
        zamienia word na  _ _
        zatrzymuje spacje jako spacje
        return str: hashed_password'''
    wordh = ""
    for i in range(len(sentence)):
        if sentence[i] == chr(32):
            wordh += " "
        else:
            wordh += "."
    return wordh


def uncover(hash_passw, passw, lett):
    ''' arg: jak wyżej
        zamiania odgadnieta na literę
        return: zmodyfikowane hashed_password'''
    temporary = ""
    for i in range(len(passw)):
        if lett == passw[i] and not(hash_passw[i].isalpha()):
            temporary += passw[i]
        else:
            if passw[i] == chr(32):
               temporary += ' '
            else:
                temporary += hash_passw[i]
    return temporary


def update(used_lett, lett):
    ''' dodaje litery do used_letters
        return: updated used_letters'''
    used_lett.append(lett)
    print("list of used letters:", end = " ")
    for item in used_lett:
        print( item, end = " ")
    print("")


def is_win(hash_passw, passw):
    ''' sprawdza czy są identyczne
        zwraca: TRUE'''
    if hash_passw == passw:
        return False
    else:
        return True


def is_loose(life):
    ''' if life_points == 0
        return: bool (TRUE)'''
    if life == 0:
        return False
    else:
        return True


def get_input():
    '''reads user input until only letters
        return: str (validated input)'''
    print("\nInput a whole name of the coded capitol (attn: mistake cost 2 turns !!!)")
    wsad = input("or choose one letter:")
    wsad = wsad.upper()
    return wsad


def total_score (time_score, mistakes):
    tscore = 200 - int(time_score)
    tmistakes =  50 * (5 - mistakes)
    return tscore + tmistakes  

# ===========


password = ""
hashed_password = ""
used_letters = []
life_points = 5
player_in = ""      
start_game = ""

password = pick_secret().upper()
hashed_password = get_hashed(password)
print("\nTry to uncode the European Capital (only 5 mistakes allowed)")
start_game = input("Your guessing time will be measured. If ready press Y: ")
print(" ")
start_game = start_game.upper()
if start_game == 'Y':
    t0 = time.time()

print(hashed_password)

print('')
while is_loose(life_points) and is_win(hashed_password, password):
    player_in = get_input()
    if len(player_in) == 1:
        if password.find(player_in) < 0:
            life_points -= 1
            hmdraw.hangdraw(5-life_points)
            print(hashed_password)
            print("You may still make " + str(life_points) + " mistakes")
            update(used_letters, player_in)
        else:
            hashed_password = uncover(hashed_password, password, player_in)
            print(hashed_password)
            update(used_letters, player_in)
    else:
        if player_in != password:
            life_points -= 2
            hmdraw.hangdraw(5-life_points)
            if life_points < 0: life_points = 0
            print(hashed_password)
            if life_points > 0:
                print("You may still make " + str(life_points) + " mistakes")
        else:
            hashed_password = ""
            for i in range(len(password)):
                hashed_password += password[i]
            print(hashed_password)
t1 = time.time()
total = round(t1 - t0)
print("\nTotal time: " + str(total) + " seconds")
if life_points == 0:
    nation = hmdictionary.capital_nation[password]
    print("\nUnfortunately, you are the looser. Game Over. The salution was: ", end =" ")
    print(password + " capital of " + nation)
else:
    prob = 5 - life_points
    nation = hmdictionary.capital_nation[password]
    print("\nCongratulation!!! You make " + str(prob) + " mistakes to guess coded capital :", end = " ")
    print(password + " capital of " + nation)
    result = total_score(total, prob)
    print("Your final score is: " + str(result) + " points")
    print("")
    hmtop_update.hmtopfive_update(result)