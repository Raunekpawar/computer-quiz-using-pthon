print("Welcome to my computer Quiz!")

playing = input("Do you want to play..?")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input(" What is the full form of RAM..?")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what is the full form of ROM..?")
if answer.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer =input("What is the full form if IDE..?")
if answer.lower() == "integrated development environment":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("you got" +str(score) +"questions correct !")
print("you got" +str((score/3) *100) +"%.")

 