import random

names=['cat','dog','snakes','tiger','elephant','dear']

def random_name_selector():
    return random.choice(names)

def game():
    alphabet='abcdefghijklmnopqrstuvwxyz'
    animal_name=''
    animal_name= random_name_selector()
    guess=''
    gussed_Letter=[]
    
    chances= 10
    guessed= False

    print(f'\n\nThe lenght of word is {len(animal_name)} \n\n')
    print(f'\n\nYou have {chances} to enter\n\n')
    while guessed==False:
        name='' 
        guess=input('Enter a character or full name: ').lower()

        #1.if the gussed one is a letter i.e whose lenght=1

        if len(guess)==1:
            if guess in alphabet:
                if guess in gussed_Letter:
                    print('\n\nYou have already gussed that letter')
                if guess in animal_name:
                    print('\n\nGood Going . Rigth guess')
                    gussed_Letter.append(guess)
                
                elif guess not in animal_name:
                    print('\n\nWrong guess.Too Bad shame on you\n\n')
                    chances-=1
                    print(f'\nYou have left with {chances} chances')

                else:
                    print("\n\nDon't know why this option appeared. Will work on  it") 


            else:
                print('\n\nSuch world or character does not exist\n\n')  

        #2. when the len of the word is equal to the length of the guessed word

        if len(animal_name)==len(guess):
            if guess== animal_name:
                print('\n\nCongractulation you have guessed the correct word\n\nThank You for playing')
                guessed=True
            else:
                print('\n\nWrong guess. Shame on You')
                chances-=1
                print(f'\nYou have left with {chances} chances')

        #3. when the lenght of the gussed word is greater than the random selected number

        if len(guess)>len(animal_name):
            print("\n\nSuch word dosen't exist.")
            chances-=1
            print(f'\nYou have left with {chances} chances')


         
         
        for letter in animal_name:
            if letter in gussed_Letter:
                 name=name+letter
            else:
                name +='*'

        if guessed==False:
             print(f'\n\n{name}\n\n')


       
        if name==animal_name:
            print(f'\n\nCongractulation you have guessed the correct word\n\n')
            guessed=True
        

        if chances==0:
            print(f'\n\nYou are out of chances. You are an as*hole\n\n')

        

game()