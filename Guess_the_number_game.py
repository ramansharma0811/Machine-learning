#!/usr/bin/env python
# coding: utf-8

# # Game - Guess the number

# In[ ]:


import random
acc_bal = int(input('enter the account balance:- ' )) #asking user to input the account balance
wallet_bal = int(input('enter the wallet balance:- ' )) #wallet balance from where we will tranfer our money to account balance
new_acc_bal = game_fees(acc_bal,wallet_bal) #this the game fees function checking whether the user has min 500 balance in his account
print('The final account balance :- ', new_acc_bal) #it is after the whole game,it will tell the final balance in account


# In[ ]:


def game_fees(acc_bal,wallet_bal):
    play_again = True 
    lost_count = 0 #how many times we have lost the game counter

    while play_again:    
        if acc_bal+wallet_bal >= 500 : #will check whether the account balance and wallet balance is more than 500(1st condition of the game)
            if acc_bal <500:   #will check whether account has the min entry fees 
                temp = 500 - acc_bal #if not it will add the deficiet to the account balance from wallet balance
                wallet_bal -= temp
                acc_bal += temp
                print('You do not have enough money in account to start playing.Recharging your account\n')
                print('Now your e-wallet balance:-',wallet_bal ,'Account balance:-',acc_bal)

            print('Now, you are ready to play the game')
            win_amount = guess_game() #will call the game function and will stores the winning amount
            acc_bal += win_amount     #winning amount will be added to the account balance
            if(win_amount > 0):       #if it is greater than 0 it will tell how much we have won
                print('Congo!! You Won: ', win_amount)
            elif(win_amount < 0):     #if it is less than 0 it will tell we lost 500 in the game
                print('So Sad!! You Lost: ', 500)
            print('The account balance after this game:- ', acc_bal)
            play_again = play_rep()  #it will call the function to ask whether we want to play again or not
        if acc_bal+wallet_bal<500:   #will check whether the account balance and wallet balance is less than 500
            print('You do not have enough money in e-wallet or in your account.')
            print('Your e-wallet balance:-',wallet_bal ,'Account balance:-',acc_bal)
            break
    return(acc_bal) #if amount is less than 500 will return to the main function


# In[ ]:


#in this function will play the game of guessing
#if we won in first chance we will win 5000 or in second chance 1000 or in third chance zero rs 
#but will if lost all  the chances then we will loose 500

def guess_game():
    random_number = random.randint(1,10)
    lost_count = 0
    while lost_count < 3:
        number = input('Guess the number: ')
        if number.casefold() == 'exit':
            print('Enjoy your day!')
            return(0)  
        elif number.isdigit():
            if int(number) == random_number :
                if lost_count == 0:  #if wins in first chance 5000
                    print('Hurray!,You won 5000')
                    return(5000)
                elif lost_count == 1: 
                    print('Hurray!,You won 1000')
                    return(1000)    #if wins in second chance 1000
                elif lost_count == 2:
                    print('Hurray!,You won')
                    return(0)       #if wins in third chance 0
            elif int(number) < random_number:
                print('Too Low')    #for hint
                lost_count += 1
            elif int(number) > random_number:
                print('Too High')   #for hint
                lost_count += 1
        else:
            number = print('Not a valid value')
    print('sorry! You lost.The number was:-',random_number)
    return(-500)                   #if losses,lost 500


# In[ ]:


#this function will ask user,will he/she play again or not?

def play_rep():
    game_rep = input('Do you want to play one more time:-')
    while True:
        if game_rep.casefold() == 'no': 
            print('Have a wonderful day!')
            return(False) #return to the main function
        elif game_rep.casefold() == 'yes':
             return(True)
        else:
            game_rep = input('You entered a wrong choice.Please enter YES or NO:-')
           

