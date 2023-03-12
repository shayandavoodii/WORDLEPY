# <a name="WORDLEPY"></a><p align="center">WORDLEPY</p>
<div  align="center">WORDLE Script in Python

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/e607d3cbfd10434383a9cb2d04b530ed)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=shayandavoodii/WORDLEPY&amp;utm_campaign=Badge_Grade)
![commits](https://badgen.net/github/commits/shayandavoodii/WORDLEPY/main)
<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/shayandavoodii/WORDLEPY/main">

</div>

# 🔮Motivation
I got familiar with [WORDLE](https://www.nytimes.com/games/wordle/index.html) through social media a year ago. I used to play it for consecutive days. However, I was unsatisfied with it. The game had limitations in rounds of playing (still has), and it only permits the users to play it once a day. Sometimes I tried it in several browsers to bypass the limit until I found the answer. But that didn't satisfy me because I wanted to play more and guess different words. So I decided to have my own WORDLE game. This is the motivation behind this work, and today (after more than a year), I decided to make this repo public. Maybe one day, I will come up with a lot of code refactoring  or even suitable design material. I'm not an application developer, and in those moments, I just wanted to incorporate features that I wanted into the application and ignored the code's design and maintainability.

# 💻GUI Version
![chrome_DPNUQ2YuKl](https://user-images.githubusercontent.com/52105833/224538209-3cd604f8-d700-48df-825f-24054845014d.png)
The application's functionality is pretty simple. Just run the latest version of the executable file, and you'll be faced with the following screen.
1. To start a game or a new turn, click the "Start" button.
![image](https://user-images.githubusercontent.com/52105833/224539463-21f5e725-dfd6-4e2b-8426-bc37c07f04a7.png)

2. Write a word with five letters in the text box and hit the "Enter" button or press the key shortcut <kbd>Ctrl+Enter</kbd> to see the result of your first guess.
![chrome_LVGa7rNaHS](https://user-images.githubusercontent.com/52105833/224539323-b67dff6a-061a-4270-b57b-72027625ab36.png)
You'll see the following screen after you hit Enter, and I've provided some details about each segment in the following snapshot:
![image](https://user-images.githubusercontent.com/52105833/224539663-7129ce4c-6702-4015-ada3-16c292896408.png)
Continue entering words until you find the chosen word. It's possible to monitor the winner's guess and success rate through the "Stats" button by pressing the key shortcut <kbd>Ctrl+S</kbd> and the history of playing the game by hitting the "History" button or pressing the key shortcut <kbd>Ctrl+H</kbd>.
![8RMckIlUhT](https://user-images.githubusercontent.com/52105833/224540374-478666d6-df2d-48c8-91e1-7509f9b8ae8a.png)
![image](https://user-images.githubusercontent.com/52105833/224540440-b0b34789-5a71-48dd-98e2-54f7804a9682.png)


# REPL version
Make sure to put the `frequent_5_char_words.csv` file in the same directory that the code is in. Also, you need to install the following packages:    
1. numpy: `conda install -c anaconda numpy`
2. pandas: `conda install -c conda-forge pandas`
3. emoji: `conda install -c conda-forge emoji`  

You can make six guesses to infer the chosen word, a 5-letter meaningful English word.
1. Enter `exit` to quit. 
2. you can enter `?` to give up while you have guessed four wrong words
3. enter `cls` to clear output
