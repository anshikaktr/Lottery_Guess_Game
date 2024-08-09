"""
We are making a lottery ticket number guess game
there are a million no of possiblities for a 6-digit no.
so u will be allowed to use hint
BUT prize money will be deducted
for correctly guessed no., prize money == $1,000,000
"""

import random
#Generate a unique lottery number on every output
lottery_lst= random.choices(range(0,10),k=6)
lottery_number = ''.join([str(num) for num in lottery_lst])
print(lottery_number)


print("Guess the ticket number.\nReward Money is 1000000 USD.\nWith every Hint some amount will be deducted from the cash prize ")

#Prize Amount
prize_amount= 1000000

#HINT1
def hint1():
    global prize_amount
    prize_amount -= 1000
    if lottery_number[i] > usr_input:
        print('Try a number greater than given input')
    elif lottery_number[i] < usr_input:
        print('Try a number smaller than given input')
    else:
        pass
    print("prize amount deducted to:",prize_amount)

##HINT2
def hint2():
    global prize_amount
    prize_amount -= 2000
    if lottery_number[i] in ['0','2','4','6','8']:
        print('Try a even number')
    elif lottery_number[i] in ['1','3','5','7','9']:
        print('Try a odd number')
    else:
        pass
    print("prize amount deducted to:",prize_amount)


#Take input from user
for i in range(0,6):
    usr_input= input('Guess a number between 0 to 9: ')
    if usr_input in ['0','1','2','3','4','5','6','7','8','9']:
        check = lambda a,b : a==b[i]
        # print(check(usr_input,lottery_number))
        if check(usr_input,lottery_number) == True:
            ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
            print('True')
            print(ordinal(i),'digit is ',lottery_number[i])
        else:
            use_hint=input('Use hint? Y/N: ')
            if use_hint=='Y' or use_hint=='y':
                hint1()
                usr_input = input("Enter a number between 0 to 9: ")
                print(check(usr_input,lottery_number))
                if check(usr_input,lottery_number) != True:
                    use_hint=input('Use hint Again? Y/N: ')
                    if use_hint=='Y' or use_hint=='y':
                        hint2()
                        usr_input = input("Enter a number between 0 to 9: ")
                        print(check(usr_input,lottery_number))
                        if check(usr_input,lottery_number) != True:
                                print('YOU LOST')
                                break
                    else:
                        print('End of the Game')
                        break
            else:
                print('End of the Game')
                break

        print("YOUR final prize amount is $",prize_amount)

    else:
        print("ERROR!! ")
        break

print("Visit here to claim your reward: https://xkcd.com/353/#:~:text=https%3A//xkcd.com/353/")