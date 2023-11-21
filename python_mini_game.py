import random 
import numpy as np
import time
import datetime

def validate(enteredReply):
    enteredReply=enteredReply.lower()                               #make sure input is lower case
    if enteredReply == "yes" or enteredReply=="no":
        return True
    else:
        return False

def endingNoCat():
    print("Walking back to meet Mike.........")
    input(">>>Press enter to continue")
    print("Business Mike: Good to see you again, ",playerName,". Thank God that you are safely back!")
    input(">>>Press enter to continue")
    print("Business Mike: I know that you did not find my cat, it's ok")
    input(">>>Press enter to continue")
    print("Hope you have a nice trip and thanks so much for your try!")
    input(">>>Press enter to end the game")
    
def endingWithCat():
    print("Walking back to meet Mike.........")
    input(">>>Press enter to continue")
    print("Business Mike: Good to see you again, ",playerName,". Thank God that you are safely back!")
    input(">>>Press enter to continue")
    print("Business Mike: Fabulous!!! You have found my cat!!!")
    input(">>>Press enter to continue")
    print("Thank you for your help! As a return I will buy you a lunch!", playerName)
    
    lunch=""
    while(validate(lunch)==False):
        lunch=input("yes/no >>>")
        lunch=lunch.lower()
        if lunch == "yes":
            print("Let's go! I'll let you try out the delicacies of THE BIG ITALY!")
            input(">>>Press any key to end the game")
            break
        elif lunch =="no":
            present = np.array(["1.Gold 100g","2.Cash USD100","3.Flight ticket","4.New handphone"])
            print("Businessman Mike: Hmm..OK...But please take any one of the gifts, as a return for you helped me.")
            print("I have these in my bag: ",present)
            giftChosen=int(input("Please enter the number of the gift>>>"))
            present = np.delete(present,giftChosen-1)
            print("Businessman Mike: Great! Now I got these remained in my bag!",present)
            print("Businessman Mike: Glad that you took it, hope to see you again!",playerName)
            input(">>>Press enter to continue")
            break
        else:
            print("Businessman Mike: Pardon?")
            
def gameFindCatIntro():
    print("------------------------------------------------------")
    print("\n[Finding cat's briefing']\n")
    print("Businessman Mike: My cat ran into a house, but there are 30 houses in this city.")
    print("                 Some houses are empty and safe, Some are mafia's house.")
    print("                 Be careful when choosing the house to look for my cat.")
    print("                 The house number start from 1 to 20.")
    print("                 The challenge is now started.")
    print(" _   _   _   _   _   _   _   _   _    __   __   __   __   __   __   __   __   __   __   __")
    print("/ \\ / \\ / \\ / \\ / \\ / \\ / \\ / \\ / \\  /  \\ /  \\ /  \\ /  \\ /  \\ /  \\ /  \\ /  \\ /  \\ /  \\ /  \\")
    print("|1| |2| |3| |4| |5| |6| |7| |8| |9|  |10| |11| |12| |13| |14| |15| |16| |17| |18| |19| |20|")
    gameFindCat()
    
def guessingGameExample():
    print("------------------------------------------------------")
    print("Mafia:Listen kiddo,I will only give you one example.")
    print("       Let say if I wrote 5234, and you guessed 5346")
    print("       look, 5 is exactly correct with the number and position, so it is 1A")
    print("       Then 3 and 4 is correct number but at wrong position, so there are 2B")
    print("       **A: total of number that is correct and at right place")
    print("       **B: total of correct number but at wrong place")
    print("       So, from the example above, the 5346 you guessed, i will reply you 1A2B.")
    print("       Done for the long explaination, let's start.")
    print("------------------------------------------------------")
    guessingABGame()
    
def guessingABGame():
    input(">>>Press enter to continue")
    print("Mafia writing numbers.......")
    numberMafia = random.sample(range(1, 10), 4)
    print("iilustration purpose:",numberMafia)   
    a,b,num,guessCount = 0,0,0,0          
    while guessCount!=8:
        if a!=4:
            if guessCount<8:                              
                a,b,num = 0,0,0    
                guessNumber = list(input("Your Guess >>> ")) 
                print(len(guessNumber))
                if all([item.isdigit() for item in guessNumber]) and len(guessNumber)==4:
                    guessCount+=1
                    for i in guessNumber:
                        if int(guessNumber[num]) == numberMafia[num]: 
                            a += 1                       
                        else:
                            if int(i) in numberMafia:         
                                b += 1  
                        num += 1           
                    print(f'Mafia: {a}A{b}B')
                    print("Mafia: You left ",8-guessCount," chances to guess")
                elif len(guessNumber)!=4:
                    print("You have entered less than 4 digits")
                else:
                    print("You have entered non-number or more than 4 numbers...")
        else:
            print('Mafia: But Hey Little Kiddo! You got it！ Well done')
            print("       You can leave from the house...")
            print("       Now you can proceed to search for the cat...or not")
            print("------------------------------------------------------")
            print("System: Do you wanna continue to find the cat?")
            ans=""
            while validate(ans)==False:
                ans = input("yes/no>>> ")
                ans = ans.lower()
                if ans=="yes":    
                    print("Mafia: Great! Let's start the game right now.")
                    gameFindCat()
                    break
                elif ans=="no":
                    print("System: Understand, let's go back to Mike and tell him...")
                    input(">>>Press enter to continue")
                    endingNoCat()
                    break
                else:
                    print("System: Sorry, I don't get you.")
            break
    
    if guessCount>=8:
        print("Mafia: You have exceeded the guess limit")
        print("       You gotta stay with me forever here")
        print("=========================================================")
        print("|    |   ____            |        ____   ____  ____")
        print("|    |  |    |  |    |   |       |    | |     |")
        print("|____|  |    |  |    |   |       |    | |____ |____")
        print("     |  |    |  |    |   |       |    |     | | ")
        print("_____|  |____|  |____|   |_____  |____| ____| |____ ")
        print("=========================================================")
        print("Start the game again?")
        startOver="d"
        while(len(startOver)!=0):
            startOver = input("yes/no=> ")
            startOver = startOver.lower()
            if startOver=="yes":    
                print("System: Great! Let's start the game again.")
                gameFindCatIntro()
                break
            elif startOver=="no":
                print("System: Never mind, thanks for your try...")
                break
            else:
                print("System: Sorry, I don't get you.")
    else:
        print('Mafia: But Hey Little Kiddo! You got it！ Well done')
        print("       You can leave from the house...")
        print("       Now you can proceed to search for the cat...or not")
        print("------------------------------------------------------")
        print("System: Do you wanna continue to find the cat?")
        ans=""
        while(ans!="no"):
            ans = input("yes/no>>> ")
            ans = ans.lower()
            if ans=="yes":    
                print("Mafia: Great! Let's start the game right now.")
                gameFindCat()
                break
            elif ans=="no":
                print("System: Understand, let's go back to Mike and tell him...")
                input(">>>Press enter to continue")
                endingNoCat()
                break
            else:
                print("System: Sorry, I don't get you.")
                 
def gameEscapeMafiaIntro():
    print("Mafia: This is not an easy game. You gotta be super careful if you")
    print("       don't wanna stay here FOREVER with me. HAHAHAHHA")
    print("------------------------------------------------------")
    input(">>>Press enter to continue")
    print("[Escape Game Briefing]\n")
    print("System: You only have 8 chances to make the guess.")
    print("Mafia: I will write down a number with 4 figures (xxxx) on this paper.")
    print("       Then you have to guess out what number I have written here.")
    print("       If the number and position both correct, then it is counted as A",)
    print("       If the number is correct but the position is wrong, then is counted as B")
    print("       Got it?")
    print("------------------------------------------------------")
    
    while(1):
        a = input("yes/no >>> ")
        a = a.lower()
        if a=="yes":    
            print("Mafia: Great! Let's start the game right now.")
            guessingABGame()
            break
        elif a=="no":
            guessingGameExample()
            break
        else:
            print("Mafia: Again.")
    
def gameFindCat():
    house=[]
    count=0
    #Assigning types of houses
    while count!=20 :
        r = random.randint(-5,15)
        if r not in house:
            house.append(r)
            count+=1
    print("Illustration purpose: ",house)
    #hint for user to be alert about mafia's house
    countMafia=0
    mafiaHouseIndex = []
    #check total number of the mafia's house
    for numMafia in house:
        if numMafia<0:
            mafiaHouseIndex.append(numMafia)
            countMafia+=1
    print("\nHints: [There are ",countMafia," mafia's house.]\n")
    #house with max number has the cat 
    cat = max(house)
    catHouse = house.index(cat)
    #Game started here
    print("System: Please enter the house number you wanna check:")
    while(1):
        inputHouse = input()
        #check if input is number
        if inputHouse.isnumeric():
            inputHouse=int(inputHouse)
            #validate input
            if inputHouse >20 or inputHouse<1:
                print("System: The house number input is invalid.")
            else:
                #if house[x] is negative number means its mafia's house
                if house[inputHouse-1] <0:
                    print("<<<<<<<<<<    ALERT    >>>>>>>>>>>>>")
                    print("Oh no! You have chosen a mafia's house...")
                    print("Now you have to escape from the mafia.")
                    print("------------------------------------------------------")
                    print("Mafia: Hey, little kiddo, I will play a game with you,")
                    print("       If you won, you can go, otherwise, you gotta stay here...")
                    print("       Understand?")
                    print("------------------------------------------------------")
                    attempt = " "
                    while(1):
                        attempt = input("yes/no>>>").lower()
                        if attempt == "yes":
                            gameEscapeMafiaIntro()
                            break
                        elif attempt =="no":
                            print("------------------------------------------------------")
                            print("Mafia: I don't care you understand or not,")
                            print("       You only can say yes.")
                            print("       Get ready, little kiddo.")
                            gameEscapeMafiaIntro()
                            break
                        else:
                            print("Mafia: Again?")
                    break
                elif inputHouse-1 == catHouse:
                    print("System: Congratulations! You have found the house that the cat in it!")
                    print("        Let's return the cat to its owner.")
                    while(1):
                        contNext = input("yes/no >>>").lower()
                        if contNext == "yes":
                            endingWithCat()
                            break
                        elif contNext == "no":
                            print("System: IF you do not return the cat, you are not allowed to leave ITALY, my dear...")
                        else:
                            print("System: I don't get you...")
                    break
                else:
                    print("Safe and sound...")
                    print("But no cat in this house, check the next one")
        else:
            print("System: You did not enter any number...Please reenter")




def reconfirmGame():
    print("Are you very busy at the moment?")
    option = ""
    while option != "yes" or option != "no":
        option = input("yes or no >>>")          
        option=option.lower()                               #make sure input is lower case
        if option =="yes":
            print("Businessman Mike: Really? But it will only cost you few minutes...")
            print("                  Would you help me?")
            ans = ""
            while ans != "yes" or ans != "no":
                ans = input("yes or no >>>")          
                ans=ans.lower()                               #make sure input is lower case
                if ans =="yes":
                    print("Businessman Mike: Thanks for willing to help me out.")
                    gameFindCatIntro()
                    break
                
                elif ans == "no":
                    print("Businessman Mike: Okay....See you next time")
                    break
                    
                else:
                    print("Businessman Mike: Sorry, I don't get you.")
            break
        elif option == "no":
            print("Businessman Mike: If you are not busy, I really need your help,",playerName,".")
            print("YES TO PLAY, NO TO LEAVE THE GAME.")
            nbusy = ""
            while nbusy != "yes" or nbusy != "no":
                nbusy = input("yes or no >>>") 
                print(nbusy)
                nbusy=nbusy.lower()                               #make sure input is lower case
                if nbusy == "yes":
                    print("Businessman Mike: Thanks for willing to help me out.")
                    gameFindCatIntro()
                    break
                
                elif nbusy == "no":
                    print("Businessman Mike: Okay....See you next time1")
                    break
                    
                else:
                    print("Businessman Mike: Sorry, I don't get you.")
            break
            
        else:
            print("Businessman Mike: Sorry, I don't get you.")



def gameIntro():
    option = ""
    while validate(option)==False:
        option = input("yes or no >>>")   
        option=option.lower()
        if option =="yes":
            print("Businessman Mike: Thanks for willing to help me out.")
            gameFindCatIntro()
            break
        
        elif option == "no":
            print("Businessman Mike: But...")
            reconfirmGame()
            break
        
        else:
            print("Businessman Mike: Sorry, I don't get you.")

#main function

startTime = time.time()
#get today date and day
todate = datetime.datetime.now().strftime("%x")         #local version of date
day = datetime.datetime.now().strftime("%A")            #weekday, full version
#tuple to store different weather
weather=('rainy day','sunny day','windy day','cloudy day','snowy day')
climate = random.choice(weather)
#story introduction
print(f"Today is {todate},{day}, a {climate}. \nYou are walking on the Via Palmiro Togliatti street in Italy.")
print("You planned to stay in Italy for 9 days,")
print("This is the 8th day of the trip, soon you are going back to your country")
input(">>>Press enter to continue")
print("[You taking photo of the street...]")
print("[suddenly someone approching...]")
input(">>>Press enter to continue")
print("Businessman Mike: Excuse me, nice to meet you! How should I call you?")
while(1):
    playerName = input("Your name>>> ")
    if(playerName.isnumeric()==False and len(playerName)!=0):
        print("Hi "+playerName+", I am Mike, would you like to do me a favour?")
        break
    else:
        print("Businessman Mike: Hmm, I need your name, not number or ...")
    

gameIntro()
#Calculating duration
endTime = time.time()
difference = endTime - startTime
difference = "{:.2f}".format(difference)
print("Your play time:",float(difference), " seconds")

    