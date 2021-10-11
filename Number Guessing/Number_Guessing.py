import random 

num = 0
att = 0
bes = 0

inp = ""
data = ""

def highestscore():
    global data
    global bes

    with open("Data.txt", "r+") as f:
        data = f.read()
        f.seek(0)
        
        if int(data) >= att:
            bes = att
            f.write(str(att))
        else:
            bes = int(data)

def game():
    global num
    global inp 
    global att
    global bes

    inp = input("")

    if inp == str(num):
        att += 1
        highestscore()
        print("Well done! You completed this in "+str(att)+" attempts! Your current highscore is "+str(bes)+" attempts!")
        num = random.randint(0,50)
        print("Guess a number between 1 - 50!")
        att = 0
        game()
    else:
        att += 1
        print("Wrong! Try again!")
        game()

num = random.randint(0,50)
print("Guess a number between 1 - 50!")
game()