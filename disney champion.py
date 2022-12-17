

import time

print("Which Disney Champion are you?")

time.sleep(3)
print("           HAJIME!")

time.sleep(2)
print(("\n"*100) + "Type which answer best suits you")

time.sleep(1)
print("dark or black")

dark = "dark"
black = "black"
if input() == dark:
    score = 0
    print("\n" * 100)
else:
    print("\n"*100)
    score = 2

time.sleep(1)
print("life or death")

life = "life"
death = "death"
if input() == life:
    score2 = (score)
    print("\n" * 100)
else:
    print("\n" *100)
    score2 = score + 1

time.sleep(1)
print("hot or cold")

hot = "hot"
cold = "cold"

if input() == hot:
    score3 = score2
    print("\n" * 100)
else:
    print("\n"*100)
    score3 = score2 + 1

time.sleep(1)
print("true or false")

true = "true"
false= "false"

if input() == true:
    score4 = score3
    print("\n" * 100)
else:
    print("\n"*100)
    score4 = score3 + 1

time.sleep(1)
print("beyonce or taylor")

beyonce = "beyonce"
taylor= "taylor"

if input() == beyonce:
    score5 = score4
    print("\n" * 100)
else:
    print("\n"*100)
    score5 = score4 + 1

time.sleep(1)
print("fat or poor")

fat = "fat"
poor= "poor"
if input() == fat:
    final = score5
    print("\n"*100)
else:
    print("\n"*100)
    final = score5 + 1

time.sleep(1)

def message(string):
    for x in string:
        print(x, end="")
        time.sleep(.1)

if __name__ == '__main__':
    msg = "Gumbo... Gumbo, in the pot. We need a Princess" + "\n" + " WHAT YOU GOT"
    message(msg)

print("\n"*100)
print(final)
print("enter the score above")
input()

if final == 6:
    print("you are a bad bitch")
elif  final == 5:
    print(" Congrats You are GOLLUM")
elif final == 4:
    print("You are Neeko")
elif final == 3:
    print("Basic Bitch")
elif final == 2:
    print(" You are a elf")
elif final == 1:
    print(" You are Sally")
elif final == 0:
    print("")

pass