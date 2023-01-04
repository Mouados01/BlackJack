#from IPython.display import display, HTML 
#display(HTML("<style>.container { width:100% !important; }</style>")) 


import random
import numpy as np
import pandas as pd
import csv


deck = ['2','3','4','5','6','7','8','9','2','3','4','5','6','7','8','9','2','3','4','5','6','7','8','9','2','3','4','5','6','7','8','9','A','J','Q','K','A','J','Q','K','A','J','Q','K','A','J','Q','K','10','10','10','10']
deckZ = deck
deck = deck *6



def card_value(card):
    if card in {'2','3','4','5','6','7','8','9'}:
        return int(card)
    elif card in {'J','Q','K','10'}:
        return int(10)
    elif card == 'A' :
        return int(11)
    


def sum_cards(player):
    val = []
    n   = 0
    for card in player:
        cardV = card_value(card)
        val.append(cardV)
        n = sum(val)
        
    j = player.count('A')
    
    if 'A' in player and n>21 :
        return n -(10*j)
    else :
        return n


def hit(player):

    card = random.choice(deck)
    player.append(card)
    deck.remove(card)
    

def deal_cards(player,decision,sum_val,bet_val):
    
    #global bet
    #global Bankroll
    
    if decision == "HIT" :
        Player_decision(player,"HIT",sum_val,bet_val)
                
    elif decision == "STAND":
        Player_decision(player,"STAND",sum_val,bet_val)
                
    elif decision == "DOUBLE" and len(player) == 2 :
        Player_decision(player,"DOUBLE",sum_val,bet_val)
                
                
    elif ( decision == "SPLIT" ) and (card_value(player[0]) == card_value(player[1]))  :
            Player_decision(player,"SPLIT",sum_val,bet_val)
            
            
            
    else :
        decision = input("You don't have the right to make this choice..try another option : ")
        sum_play = sum_cards(player)
        deal_cards(player,decision,sum_play,bet_val)
    
     
        
def deal_cardsD():
    global deal_sum 
    deal_sum = sum_cards(dealer)
    while deal_sum <= 16 :
            hit(dealer)
            deal_sum = sum_cards(dealer)
            

def Player_decision(player,arg,sum_val,bet_val):
    #global bet
    global Bankroll
    global cond_data
    global cond
    global bj
    global i
    global player1
    global player2
    #global bet
    global lucky
    #global bet1
    #global bet2
   
    #z = 0
    if arg == "HIT" :
        data_func(i,player,dealer[0],sum_val,int(card_value(dealer[0])),arg,"---",bet_val,"---",Bankroll+bet_val,len(deck))
        hit(player)
        sum_val = sum_cards(player)
        print("your cards : ",player)
        print("dealer cards : ",dealer[0])
        game(player,bet_val)
        
    
    elif arg == "STAND" :
        data_func(i,player,dealer[0],sum_val,int(card_value(dealer[0])),arg,"---",bet_val,"---",Bankroll+bet_val,len(deck))
        sum_val = sum_cards(player)
        
        
    elif arg == "DOUBLE" :
        
        data_func(i,player,dealer[0],sum_val,int(card_value(dealer[0])),arg,"---",bet_val,"---",Bankroll+bet_val,len(deck))
        Bankroll = Bankroll - bet_val
       
        hit(player)
        sum_val = sum_cards(player)
        
        
        #print("your cards : ",playeer)
        
        
        
       
     
    elif arg == "SPLIT" :
        data_func(i,player,dealer[0],sum_val,int(card_value(dealer[0])),arg,"---",bet_val,"---",Bankroll+bet_val,len(deck))
        
        Bankroll = Bankroll - bet_val
        bet1 = bet_val ; bet2 = bet_val
        player1.append(player[0])
        player2.append(player[1])
        hit(player1)
        sum1 = sum_cards(player1)
        data_func(i,player1,dealer[0],sum1,int(card_value(dealer[0])),"---","---",bet_val,"---",Bankroll+bet_val,len(deck))
        hit(player2)
        sum2 = sum_cards(player2)
        data_func(i,player2,dealer[0],sum2,int(card_value(dealer[0])),"---","---",bet_val,"---",Bankroll+bet_val,len(deck))
        
        print("your fisrt hand : ",player1)
        print("your second hand : ",player2)
        print("delear cards : ",dealer[0])  
        
        
        print("for your first hand : ")
        
        game(player1,bet1)
        cond1 = cond_data
        
        
        print("for your second hand : ")
       
        game(player2,bet2)
        cond2 = cond_data
        
        
        if player1 != lucky :
            print("********result for your first hand : ********")
            cond_data = cond1
            sum1 = sum_cards(player1)
            result(player1,sum1,bet1)
        
        if player2 != lucky :
            print("********result for your second hand : ********")
            cond_data = cond2
            sum2 = sum_cards(player2)
            result(player2,sum2,bet2)
            
        
        
        
        print ("rest of deck : ",len(deck))
       
        cond = "SPLIT"
        
        
def result(player,sum_val,bet_val):

    global Bankroll
    global data
    global cond_data
    
    #global bet
    #global bet1
    #global bet2
    
    

    
    print("Results : ")
    k = 0
    
    if sum_val > 21 :

        print("your cards : ",player)
        print("You Bust ... :/ ")
        k = bet_val
        bet_val = 0
        print("your new bet is : ",bet_val)
        
        print("your new Bankroll = ",Bankroll)
        deal_cardsD()
        data_func(i,player,dealer,sum_val,deal_sum,"---","Loss",k,bet_val,Bankroll,len(deck))
  
    else :
        
        deal_cardsD()
        
        if deal_sum > 21 :
            
            print("your cards : ",player)
            print("dealer cards : ",dealer)
            print("Dealer Bust ... Congratulation you win !! ")
            k = bet_val
            
            if cond_data == "DOUBLE" :
                bet_val = 4 * bet_val
                k = k * 2
            else :
                bet_val = 2 * bet_val
            
            print("your new bet is : ",bet_val)
            Bankroll = Bankroll + bet_val
            print("your new Bankroll = ",Bankroll)
            data_func(i,player,dealer,sum_val,deal_sum,"---","Win",k,bet_val,Bankroll,len(deck))
            
    
        elif sum_val > deal_sum :
            
            print("your cards : ",player)
            print("dealer cards : ",dealer)
            print("You win")
            
            
            
            if cond_data == "DOUBLE" :
                k = bet_val * 2
                bet_val = 4 * bet_val
            else :
                k = bet_val
                bet_val = 2 * bet_val
            
            
            print("your new bet is : ",k)
            Bankroll = Bankroll + bet_val
            print("your new Bankroll = ",Bankroll)
            data_func(i,player,dealer,sum_val,deal_sum,"---","Win",k,bet_val,Bankroll,len(deck))
    
        
        elif sum_val < deal_sum :
            
            print("your cards : ",player)
            print("dealer cards : ",dealer)
            print("You lose ")
            
            if cond_data == "DOUBLE" :
                k = bet_val * 2
            else :
                K = bet_val
                
            bet_val = 0
            print("your new bet is : ",bet_val)
            
            print("your new Bankroll = ",Bankroll)
            data_func(i,player,dealer,sum_val,deal_sum,"---","Loss",k,bet_val,Bankroll,len(deck))
            
        elif sum_val == deal_sum :
            
            print("your cards : ",player)
            print("dealer cards : ",dealer)
            print("Push")
            
            if cond_data == "DOUBLE" :
                k = bet_val * 2
                Bankroll = Bankroll + k
            else :
                K = bet_val
                Bankroll = Bankroll + k
                
            print("your new bet is : ",bet_val)
            print("your new Bankroll = ",Bankroll)
            data_func(i,player,dealer,sum_val,deal_sum,"---","Draw",k,bet_val,Bankroll,len(deck))
        
        cond_data = ""
            
            

    
    
#def prinread(arg):
    #global decision 
    
    #if arg = "decision":
        #print("make your decision ... Hit , Stand , Double or Split : ")
        #decision = input()
    
    
def dist_card1(player):
    if player == [] :
        for i in range (2):
            hit(player)
        print("your cards : ",player)
    if dealer == [] :
        for i in range (2):
            hit(dealer)
        print("dealer cards : ",dealer[0])
        

    
    
#def advice_choice(player):
    
    



def random_choice(player,dealer,choix) :

  
    
    if len(player)<= 2 and player[0] == player[1] and cond != "SPLIT":
                choix = random.choice(["HIT","STAND","DOUBLE","SPLIT"])
            
    elif len(player)<=2 and cond !="SPLIT" :
                choix = random.choice(["HIT","STAND","DOUBLE"])
            
    else :
                choix = random.choice(["HIT","STAND"])
    
    
    return choix
    
 
            
def game(player,bet_val):
    global bj
    global Bankroll
    global cond_data
    global bet
    global lucky
    global bet1
    global bet2
  
    
    decision = "NULL"
    
    
    ###### BlackJack case :
    if ( 'A' in player ) and (('J'in player) or ('Q'in player) or ('K'in player) or ('10'in player)) and ( len(player)== 2 ) :
        if ( 'A' in dealer ) and (('J'in dealer) or ('Q'in dealer) or ('K'in dealer) or ('10'in dealer)) and ( len(dealer)== 2 ) :
            print("push")
            
        else:
            k = bet_val
            bet_val = bet_val * 2.5
            lucky = player
            Bankroll = Bankroll + bet_val
            deal_sum = sum_cards(dealer)
            sum_play = sum_cards(player)
            data_func(i,player,dealer,sum_play,deal_sum,"---","Blackjack",k,bet_val,Bankroll,len(deck))
            print("Congratulation you get a BlackJack !! ")
            print("your new bet is : ",bet_val)
            print("your new Bankroll = ",Bankroll)
            print ("rest of deck : ",len(deck))
    #######        
            
    
    else:
        
        sum_play = sum_cards(player)
        deal_sum = sum_cards(dealer)
        
        if sum_play <= 21 and char == "randoma" :
            
            random_choice(player,dealer,decision)
            decision = random_choice(player,dealer,decision)
            
            cond_data = decision
            deal_cards(player,decision,sum_play,bet_val)
             
                
        elif sum_play <= 21 and char == "user_play" :
                
            decision = input("make your decision ... HIT , STAND , DOUBLE or SPLIT ")
            
            cond_data = decision
            deal_cards(player,decision,sum_play,bet_val)

        
            
def data_func(gameZ,playerZ,dealerZ,play_sumZ,deal_sumZ,decisionZ,win_or_lossZ,betZ,new_betZ,bankrollZ,deck_restZ) :
    xdata   = idata.copy()
    xdata["game"] = gameZ
    xdata["player"] = playerZ.copy()
    xdata["dealer"] = dealerZ
    xdata["play_sum"] = int(play_sumZ)
    xdata["deal_sum"] = int(deal_sumZ)
    xdata["decision"] = decisionZ
    xdata["Win_or_Loss"] = win_or_lossZ
    xdata["bet"] = int(betZ)
    xdata["new_bet"] = new_betZ
    
    bank1 = bankrollZ
    
    xdata["Bankroll"] = int(bank1)
    xdata["Deck_rest"] = int(deck_restZ)
    data.append(xdata)



data  = []
idata = {"game": [],"player": [],"dealer": [],"play_sum": [],"deal_sum": [],"decision": [],"Win_or_Loss": [],"bet": [],"new_bet": [],"Bankroll": [],"Deck_rest": []}

dealer    = []
gambler   = []
deal_sum  = 0
#bet = 0

cond      = "" 
bj = 0
bet = 0

path = r'/home/bob/Documents/bj/blackjack.csv'
path2 = r'/home/bob/Documents/bj/blackjack_user.csv'
allbet = pd.read_csv(path)
i= int(list(allbet['game'])[-1])
cond_data = ""
Bankroll  = int(list(allbet['Bankroll'])[-1])


def BlackJack(player):
    
    global Bankroll
    global bet
    global i
    global cond
    bet = 0
    i = i+1
    player_test = []
    dealer_test = []
    
    if char == "randoma" :
        bet = 20
    else :
        bet   = int(input("enter your bet : "))
    
    Bankroll  = Bankroll - bet
    
    

    dist_card1(player)
    
   
    
    

    
    
    game(player,bet)
   
    
    if cond != "SPLIT" and lucky == [] :
        sum_play = sum_cards(player)
        result(player,sum_play,bet)

        
        print ("rest of deck : ",len(deck))
        
      
        
    
      
    
  
    cond = ""    
    
    
           
        
print("**** Welcome to BlackJack Game **** \n Would you like to play the game yourself,please answer with 1 or you'de prefer to run the program play with it self,please answer with 2  ")

char = int(input())

if char == 1 :
    char = "user_play"
    dealer   = []
    gambler  = []
    lucky    = []
    player1  = []
    player2  = []

    deal_sum = 0
    bet1     = 0
    bet2     = 0
    bj = 0
    
    
    BlackJack(gambler)
    
    
elif char == 2 :
    char = "randoma"
    
    p = int(input('enter the number of self-play games'))
    
    for t in range (p) :
        dealer   = []
        gambler  = []
        lucky    = []
        player1  = []
        player2  = []

        deal_sum = 0
        bet1     = 0
        bet2     = 0
        bj       = 0
        deck = deckZ*6
    


        BlackJack(gambler)

else :
    print('you made a wrong choice,please restart the game')

df = pd.DataFrame(data)
allbet = pd.concat([allbet,df]).reset_index(drop= True)
allbet.to_csv(path,index = False)
data = []

allbet = pd.read_csv(path)


if 0:
    path = r'/home/hello/Documents/bj/blackjack.csv'
    allbet = pd.read_csv(path) 
    df = pd.DataFrame(data)
    allbet = pd.concat([allbet,df]).reset_index(drop= True)
    #allbet = pd.concat([df,allbet]).reset_index(drop= True)
    allbet.to_csv(path,index = False)
    