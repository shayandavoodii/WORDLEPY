from os import system
import numpy as np
import random
import pandas as pd
import emoji
import sys
import datetime
import re

def myWORDLE_Game():
    words = pd.read_csv("frequent_5_char_words.csv").iloc[: , 1].to_list()
    chosen_word = random.choice(words).lower()
    chosen_word_frequency = {char:chosen_word.count(char) for char in list(chosen_word)}
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    show = np.zeros((6,1) , dtype=[('x', '<U6')])
    tries = []
    print("Hint: Enter 'cls' to clear the board\nEnter '?' if you want to give up\nEnter 'exit' if you want to quit.")
    for j in range(6):
        b = 0
        while not b:
            a = input("enter a word:\n")
            
            if a.lower()=='exit': sys.exit()
            
            elif a=="?" and j>4:
                print(" !! Never Give Up !!")
                print("it was '{}'.".format(chosen_word))

                with open("My WORDLE Log.txt" , 'a+') as txt_file:
                    txt_file.write("{} {} {}\n".format(str(datetime.date.today()) , "None" , chosen_word))
                    txt_file.close()
                
                sys.exit()

            elif a.lower()=='cls' and j>0:
                system('cls')
                print("\n{}/6".format(j))
                for row in range(len(tries)):
                    if row==len(tries)-1:
                        print(show[row][0][0] , tries[row] ,end='     ')
                    else:
                        print(show[row][0][0] , tries[row])

                
                f = 0
                for k in range(4):
                    if k ==0:
                        print(" ".join(map(str , letters[f:f+8])).center(15))
                    else:
                        print("       \t\t    " , " ".join(map(str , letters[f:f+8])))
                    f += 8

                print("\n")                                

            
            elif a.lower() in words:
                if a.lower() in tries:
                    b = False
                else: 
                    b = True;  a = a.lower()
            
            else: b=False
            
        tries.append(a)

        if a == chosen_word:
            show[j , :] = emoji.emojize(":green_square::green_square::green_square::green_square::green_square:")
            print(emoji.emojize("\n{}/6        Congrats!:tada: its true : {}".format(j+1 , chosen_word) , use_aliases=True))
            for row in range(j+1):
                print(show[row][0][0] , tries[row])

            with open("My WORDLE Log.txt" , 'a+') as txt_file:
                txt_file.write("{} {} {}\n".format(str(datetime.date.today()) , j+1 , chosen_word))
                txt_file.close()
            sys.exit()
        
        counts = {item:a.count(item) for item in set(a)}
        info = {item:0 for item in set(a)}
        res = ""
        for i in range(len(list(a))):
            if a[i] in chosen_word:
                if a[i] == chosen_word[i]:
                    res += emoji.emojize(':green_square:')
                    info[a[i]] = True
# ======================================== yellow area ========================================
                else:
                    if counts[a[i]]>1 and chosen_word_frequency[a[i]]==1 and info[a[i]] ==True:
                        res += emoji.emojize(':red_square:')
                        if a[i] in letters:
                            letters.remove(a[i])

                    elif counts[a[i]]>1 and chosen_word_frequency[a[i]]==1 and info[a[i]] ==False:
                        if chosen_word.index(a[i]) in [i.start() for i in re.finditer(a[i], a)]:
                            res += emoji.emojize(':red_square:')
                            
                        else:
                            res += emoji.emojize(':yellow_square:')

                    elif counts[a[i]]>1 and chosen_word_frequency[a[i]]>1 and info[a[i]] ==True:
                        res += emoji.emojize(':yellow_square:')

                    else: 
                        res += emoji.emojize(':yellow_square:')
# ======================================== yellow area ========================================
            
            else:
                res += emoji.emojize(':red_square:')
                if a[i] in letters:
                    letters.remove(a[i])

        

        show[j , :] = res
        print("\n{}/6".format(j+1))
        for row in range(j+1):
            if row==j:
                print(show[row][0][0] , tries[row] ,end='     ')
            else:
                print(show[row][0][0] , tries[row])

        
        f = 0
        for k in range(4):
            if k ==0:
                print(" ".join(map(str , letters[f:f+8])).center(15))
            else:
                print("       \t\t    " , " ".join(map(str , letters[f:f+8])))
            f += 8

        print("\n")
        
    print(" !! FAILED !!")
    print("it was '{}'.".format(chosen_word))

    with open("My WORDLE Log.txt" , 'a+') as txt_file:
        txt_file.write("{} {} {}\n".format(str(datetime.date.today()) , "None" , chosen_word))
        txt_file.close()


class WORDLE:
    def start():
        """
        Start the game. Enjoy!
        """
        myWORDLE_Game()

    def stats():
        """
        statistical analysis of historical results.
        """
        import matplotlib.pyplot as plt
        df = pd.read_csv("My WORDLE Log.txt" , sep=" " , header=None)
        pairs = sorted(df[df.iloc[:,1]!='None'][1].value_counts().to_dict().items())
        fig, ax = plt.subplots()
        fig1 = ax.bar([value[0] for value in pairs], height= [value[1] for value in pairs])
        plt.title("Success rate = {}, Played = {}, Max Streak = {} , Current Streak = {}".format(round(len(df[df.iloc[:,1]!='None'][1])/len(df) , 2) , len(df) , np.diff(np.where(df.iloc[: , 1] == "None")).max()-1 , len(df) - np.where(df.iloc[: , 1] == "None")[0].max() - 1) , color = 'g')
        
        plt.xlabel("i'th guess" , size = 12)
        plt.ylabel("ّFrequency" , size = 12)
        plt.suptitle("stats of success" , size = 20)
        ax.bar_label(fig1, label_type='edge')
        plt.show()

    def history():
        """
        Historical plot of gaming.
        """
        import matplotlib.pyplot as plt
        df = pd.read_csv("My WORDLE Log.txt" , sep=" " , header=None)
        fig, ax = plt.subplots()
        sorted_dates = sorted(df.iloc[:,0].value_counts().to_dict().keys())
        fig1 = ax.bar(sorted_dates , [df.iloc[:,0].value_counts().to_dict()[value] for value in sorted_dates])
        plt.title("Gaming History" , size = 20)
        plt.xlabel("Dates" , size = 13)
        plt.ylabel("Frequency" , size = 13)
        plt.xticks(rotation=30 , size = 8)
        ax.bar_label(fig1, label_type='edge')
        plt.show();

WORDLE.start()
