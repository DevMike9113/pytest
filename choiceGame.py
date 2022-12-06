msg = "Hello World"
print(msg)

print("Welcome to the game!")
playing = input("Do you want to play a game?: ")

if playing.lower() != "yes":
    quit()

score = "0"

print("You are standing in a dark room.")

choice1 = input("Do you want to go left or right?: ")
if choice1.lower() == "left":
    print("You are in a room full of treasure!")
    print("You win!")
    score += 1
else:
    print("You fell into a hole!")
    print("You lose!")

choice2 = input("Do you want to go left or right?: ")
if choice2.lower() == "left":
    print("You are in a room full of treasure!")
    print("You win!")
    score += 1
else:
    print("You fell into a hole!")
    print("You lose!")

choice3 = input("Do you want to go left or right?: ")
if choice3.lower() == "left":
    print("You are in a room full of treasure!")
    print("You win!")
    score += 1
else:
    print("You fell into a hole!")
    print("You lose!")

print("Game over! Your score is:" + str(score))