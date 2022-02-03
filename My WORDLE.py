from os import system
import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd
import emoji
import sys
import datetime
import re

def myWORDLE_Game():
    words = pd.read_csv("frequent_5_char_words.csv").iloc[: , 1].to_list()
    chosen_word = random.choice(words)
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
                else: b = True
            
            else: b=False
            
        tries.append(a)

        if a.lower() == chosen_word:
            show[j , :] = emoji.emojize(":green_square::green_square::green_square::green_square::green_square:")
            print("\n{}/6    Congrats! its true : {}".format(j+1 , chosen_word))
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
        plt.bar(list(df[df.iloc[:,1]!='None'][1].value_counts(ascending = True).to_dict().keys()), height= list(df[df.iloc[:,1]!='None'][1].value_counts(ascending = True).to_dict().values()))
        plt.title("stats of success" , size = 20)
        plt.xlabel("i'th guess" , size = 12)
        plt.ylabel("ّFrequency" , size = 12)
        plt.suptitle("Success rate = {}".format(round(len(df[df.iloc[:,1]!='None'][1])/len(df) , 2)) , color = 'g')
        plt.show()

    def history():
        """
        Historical plot of gaming.
        """
        import matplotlib.pyplot as plt
        df = pd.read_csv("My WORDLE Log.txt" , sep=" " , header=None)
        plt.figure(figsize=(12,5))
        fig, ax = plt.subplots()
        fig1 = ax.bar(list(df.iloc[:,0].value_counts().to_dict().keys()) , list(df.iloc[:,0].value_counts().to_dict().values()))
        plt.title("Gaming History" , size = 20)
        plt.xlabel("Dates" , size = 13)
        plt.ylabel("Frequency" , size = 13)
        plt.xticks(rotation=30 , size = 8)
        ax.bar_label(fig1, label_type='edge')
        plt.show();

WORDLE.start()
