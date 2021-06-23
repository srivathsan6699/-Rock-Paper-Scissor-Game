import random
print("Rock  Paper : Scissor : ? ")
computer = ''
choice = '-'
count_win= 0
count_loss=0
while choice !=0:
    c = random.randint(1,3)
    choice = input()
    if c == 1:
        computer = 'rock'
    elif c == 2:
        computer ='paper'
    elif c == 3:
        computer = 'scissor'
    if choice == 'rock' and c == 3:
        print("the rock hits the scissor")
        print("you won")
        count_win+=1
    elif choice == 'rock' and c == 2:
        print('The paper catches the rock')
        print("you lost")
        count_loss+=1
    elif choice == 'paper' and c == 3:
        print("The scissor cuts the paper")
        print("you lost")
        count_loss += 1
    elif choice == 'scissor' and c == 1:
        print("the rock hits the scissor")
        print("you lost")
        count_loss += 1
    elif choice == 'scissor' and c==2:
        print("The Scissor cuts the Paper")
        print("You won")
        count_win+=1
    elif choice == 'paper' and c==1:
        print("the paper catches the rock")
        print("you won")
        count_win+=1
    if choice == computer:
        print('Tie !!')
        print()
        print("Rock  Paper : Scissor : ? ")
    elif choice == '0':
        print("Be Back soon !!")
        break
    else:
        print()
        print("Rock  Paper : Scissor : ? ")

print('You have won these {0} time\'s and I have won {1} time\'s '.format(count_win,count_loss))

