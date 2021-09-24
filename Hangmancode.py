import random as r
instructions = '''INSTRUCTIONS:
                 1. The number of letters in the movie will be shown
                 2. Guess your letter
                 3. If the movie contains the guessed letter, you get a point and the placement of the letter will be
                    shown. If not, the game gets a point.
                 4. You get 6 chances in total
                 5. You win when you reach 6 points first. Else, you lose
                 6. Have fun! '''
print(instructions)

def game():
    file = open('Hangman_data.txt','r')
    data = file.readlines()
    number = r.randint(0 , len(data)-1)
    word = data[number]
    lines = [ ]
    for i in word:
        if i == ' ':
            lines.append(' ')
        else: 
            lines.append('_')

    length=len(lines)-1
    lines.pop(length)
    counter = 0
    you=0
    for j in lines:
            print(j,end=' ')
    while True:
        letter = input("\n Guess your letter : ")
        cnt=0
        if letter in word:
            for i in range(0 , len(word)):
                if word[i] == letter:
                    lines[i] = letter
                    you+=1
                    cnt+=1
        if cnt!=0:
            print("the letter", letter, "is in the movie's name")
                
        else:
            print("the letter", letter, "is not in the movie's name")
            counter+=1
        print("scoreboard")
        print("you=",you)
        print("game=",counter)
        space=lines.count(' ')           
        for j in lines:
            print(j,end=' ')
        if you==len(lines)-space:
            print("\n\n\n Well Played , You Won!")
            break
        elif counter >= 6:
            print(" \n\n\n You Lost! try again")
            print(" \n\n\n The movie was :",word)
            break
       

