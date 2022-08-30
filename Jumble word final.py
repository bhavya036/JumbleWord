import random
def choose():
    words=['banana','apple','school','player','wow','amazing','amazon']
    pick=random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def thank(p1name,p2name,pp1,pp2):
    print(p1name,'Your score is :',pp1)
    print(p2name,'Your score is :',pp2)
    print('Thanks for playing')
    print('Have a wonderful day')
    
    
def play():
    p1name = input("player 1 : Write your name Here :")
    p2name = input("player 2 : Write your name Here :")
    pp1 = 0 #point of player 1 is initially = 0
    pp2 = 0
    turn = 0 #no one is playing initially
    while(1):
        print("=================================================")
        picked_word = choose()
        qn = jumble(picked_word)
        print(qn)
        print("=================================================")
        
        #player 1 = odd numbber player 2 = even
        if turn%2 == 0:
            print(p1name,'Your turn :', end="")
            ans = input('guess which word computer has picked :')
            if ans == picked_word:
                pp1 = pp1+1
                print('Your score is :',pp1)
            else:
                print('Better lusk.computer thinked word is :',picked_word)
            
            
        else:
            print(p2name,'Your turn :', end="")
            ans = input('guess which word computer has picked :')
            if ans == picked_word:
                pp2 = pp2+1
                print('Your score is :',pp2)
            else:
                print('Better lusk.computer thinked word is :',picked_word)
            
        turn = turn+1
        #print(turn)
        
        c = int(input('press 1 to change turn and 0 to quit here :'))
        if c==0:
            thank(p1name,p2name,pp1,pp2)
            break
        
        


play()
    