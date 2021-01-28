import random
words = ['Elephant','Banana','Orange']
points = 0

for i in range(len(words)):
    print('Points : ',points)
    random.shuffle(words)
    question = words.pop()

    jumble = dict()
    
    for j in range(len(question)):
        
        if(j==0 or j==1):
            jumble[j] = question[j].lower()
            print('__', end=' ')
        else:
            print(question[j], end=' ')

    
    guess = 4

    print('\nGuess the Word:')
    

    for k in range(guess):
        print('Remaining Guesses: ',guess)
        temp = input()
        temp = temp.lower()
        if(temp in jumble.values()):
            delIndex = None
            for j in jumble.keys():
                if(jumble[j] == temp):
                    delIndex = j
                    break
                
            del jumble[delIndex]
                    
            for p in range(len(question)):
                if(p in jumble.keys()):
                    print('__',end=' ')
                else:
                    print(question[p], end=' ')
               
            print('\nGuessed: ',temp)
            points += 5
           
        else:
            print('Wrong Guess...')

        if(len(jumble) == 0):
            break
        
        guess -= 1

    if(guess == 0):
        con = input('Press y to continue: ')
        if(con == 'y' or con== 'Y'):
            continue
        else:
            break
