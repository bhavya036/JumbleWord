import random
def choose():
    words=['banana','apple','school','player','wow','amazing','amazon']
    pick=random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def thank(p1name,p2name,pp1,pp2):
    print(p1name,'Your score is :',p1)
    print(p1name,'Your score is :',p1)
    print('Thanks for playing')
    print('Have a wonderful day')
    
    
def play():
    p1name = input("player 1 : Write your name Here :")
    p2name = input("player 2 : Write your name Here :")
    pp1 = 0 #point of player 1 is initially = 0
    pp2 = 0
    turn = 0 #no one is playing initially
while(1):
    picked_word = choose()
    qn = jumble(picked_word)
    print(qn)
    #player 1 = odd numbber player 2 = even
if turn%2 == 0:
    print(p1name,'Your turn :')
    ans = input('gess which word computer has picked :')
if ans == picked_word:
    pp1 = pp1+1
    print('Your score is :',pp1)
else:
    print('Bette lusk.computer thinked word is :',picked_word)
    c = input('press 1 to continue and o to quit here :')
if c==0:
    thank(p1name,p2name,pp1,pp2)
    break
    
else:
    print(p1name,'Your turn :')
    ans = input('gess which word computer has picked :')
if ans == picked_word:
    pp1 = pp1+1
    print('Your score is :',pp1)
else:
    print('Bette lusk.computer thinked word is :',picked_word)
    c = input('press 1 to continue and o to quit here :')
if c==0:
    thank(p1name.p2name,pp1,pp2)
    break
turn = turn+1
play()

        
    