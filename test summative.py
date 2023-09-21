import tkinter as tk
from tkinter import *

# GUI setup
root = tk.Tk()

root.title("Choose Your Own Adventure")

root.geometry('500x350')

# important variables
a = 0
correct = 0
choicepath = ""

# start button
startbutton = tk.Button(root, text="Start", anchor='center', command=lambda:start())
startbutton.configure(font=("Arial", 50, "bold"))
startbutton.place(x = 250, y = 175, height = 210, width = 300, anchor='center')


# this allows the story to start from a button
def start():
    startbutton.destroy()
    algorithm()


# this giant function gives other smaller functions all the variable data they need to build sections of the story, as well as figuring out where the story should go after an input.
def algorithm():
    global a, choicepath, gobackbutton
    # the if function checks if the choices made match the required choices to display this part of the story
    if choicepath == "":
        # this is the text that will be displayed by the "choice" function
        text1 = "BEEP BEEP BEEP you hear. it's 8am, and\nthe sound of your alarm clock has woken\nyou up on monday for school. you get up,\nget dressed and cleaned up, and then\nyou eat and get on the bus to go to school."
        text2 = "after you get to school and get to math\nclass, you realize that you forgot to do your \nhomework, as you played video games all\nweekend."
        text3 = "you know that your teacher and parents\nhate it when homework isn't done,\nand as the teacher is coming around\nchecking homework, you start panicking,\nas you don't know what to do."
        text4 = "This is your first choice,\nand it will decide how the story\ncontinues from this point on.\nChoose wisely."
        # these are the choice options that will be available for this section of the story
        choicetext1 = "tell the teacher your dog ate your homework"
        choicetext2 = "tell the teacher the truth"
        choicetext3 = "tell the teacher that you didn't do the homework because\nit was too easy"
        choicetext4 = "fight the teacher"
        choicetext5 = "mystery"
        # this is set to "True" if the section of the story is mathematical, and a different function will be used to display the math questions.
        questionchoice = False
        # the questions that will be displayed
        question1 = ""
        question2 = ""
        question3 = ""
        question4 = ""
        question5 = ""
        # the solutions to those questions needed to check if an inputted answer is correct or not.
        solution1 = ""
        solution2 = ""
        solution3 = ""
        solution4 = ""
        solution5 = ""
        # the text that will be displayed if a user gets enough correct answers or not enough correct answers
        win = ""
        lose = ""
        # resetting a variable used to keep track of what text page is being displayed.
        a = 0
        # the function that will take all the above variable data and organize and display it.
        choice(text1, text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)
        
        
    if choicepath == "1":
        text1 = "teacher: Your dog didn't eat your homework.\nyou: I assure you, he did."
        text2 = "teacher: That's impossible!\nThe homework was online!\ndogs don't eat computers!\nYou've made me really angry now.\nI'm calling your parents!"
        text3 = "after realizing your mistake,\nyou start thinking about what you will do.\ndo you:"
        text4 = ""
        choicetext1 = "accept the punishment"
        choicetext2 = "fight the teacher"
        choicetext3 = "tell the teacher you can prove you did your homework\nby answering homework questions"
        choicetext4 = "mystery"
        choicetext5 = ""
        questionchoice = False
        question1 = ""
        question2 = ""
        question3 = ""
        question4 = ""
        question5 = ""
        solution1 = ""
        solution2 = ""
        solution3 = ""
        solution4 = ""
        solution5 = ""
        win = ""
        lose = ""
        a = 0
        choice(text1, text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)


    if choicepath == "11":
        text1 = "the teacher called your parents.\nwhen you get home, you are scolded\nand sent to your room while\nthey think of a punishment.\nwhat will you do?"
        text2 = ""
        text3 = ""
        text4 = ""
        choicetext1 = "accept the punishment"
        choicetext2 = "fight your parents"
        choicetext3 = "mystery"
        choicetext4 = ""
        choicetext5 = ""
        questionchoice = False
        question1 = ""
        question2 = ""
        question3 = ""
        question4 = ""
        question5 = ""
        solution1 = ""
        solution2 = ""
        solution3 = ""
        solution4 = ""
        solution5 = ""
        win = ""
        lose = ""
        a = 0
        choice(text1, text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)


    if choicepath == "111":
        text1 = "you choose to accept the punishment.\nyou are grounded for a month\nwith your devices taken away for 2 months."
        text2 = "YOU LOSE"
        text3 = ""
        text4 = ""
        choicetext1 = ""
        choicetext2 = ""
        choicetext3 = ""
        choicetext4 = ""
        choicetext5 = ""
        questionchoice = False
        question1 = ""
        question2 = ""
        question3 = ""
        question4 = ""
        question5 = ""
        solution1 = ""
        solution2 = ""
        solution3 = ""
        solution4 = ""
        solution5 = ""
        win = ""
        lose = ""
        a = 0
        choice(text1, text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)


    if choicepath == "112":
        text1 = "parents:\nwe're so dissapointed in you.\nnow that we've had time to think\nabout what we will do, we will\nbe grounding you for a month and\ntaking away your computer for 2."
        text2 = "horrified at the thought of this,\nyou decide that you will fight\nyour parents for your freedom.\nyou: I won't let you do that!\nNot without a fight!"
        text3 = "when you say this, your dad\n takes a belt out of the closet\n and starts brandishing it like\n a weapon. still want to fight?\n he says."
        text4 = ""
        choicetext1 = "fight"
        choicetext2 = "don't fight"
        choicetext3 = ""
        choicetext4 = ""
        choicetext5 = ""
        questionchoice = False
        question1 = ""
        question2 = ""
        question3 = ""
        question4 = ""
        question5 = ""
        solution1 = ""
        solution2 = ""
        solution3 = ""
        solution4 = ""
        solution5 = ""
        win = ""
        lose = ""
        a = 0
        choice(text1, text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)


    if choicepath == "1121":
        text1 = "you approach him, chest puffed,\n showing that you want to fight.\n dad: oh, you're approaching me?\n you: I can't kick your ass without\ngetting closer."
        text2 = "you punch him in the face,\nand at the same time he hits\nyou with the belt. your mom\nis too afraid to do anything, choosing\n to stay out of the fight."
        text3 = "with your superior agility,\n you get up faster than your dad\n and take the belt. you hit\n him with it a few times,\n and he surrenders."
        text4 = "YOU WIN"
        choicetext1 = ""
        choicetext2 = ""
        choicetext3 = ""
        choicetext4 = ""
        choicetext5 = ""
        questionchoice = False
        question1 = ""
        question2 = ""
        question3 = ""
        question4 = ""
        question5 = ""
        solution1 = ""
        solution2 = ""
        solution3 = ""
        solution4 = ""
        solution5 = ""
        win = ""
        lose = ""
        a = 0
        choice(text1, text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)


    if choicepath == "1122":
        text1 = "you choose to accept the punishment.\n your dad sneers at you, and says:\n good choice. you wouldn't want\n to fight me.\nyou are grounded for a month,\nand your devices are taken away for 2 months."
        text2 = "YOU LOSE"
        text3 = ""
        text4 = ""
        choicetext1 = ""
        choicetext2 = ""
        choicetext3 = ""
        choicetext4 = ""
        choicetext5 = ""
        questionchoice = False
        question1 = ""
        question2 = ""
        question3 = ""
        question4 = ""
        question5 = ""
        solution1 = ""
        solution2 = ""
        solution3 = ""
        solution4 = ""
        solution5 = ""
        win = ""
        lose = ""
        a = 0
        choice(text1, text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)


    if choicepath == "113":
        text1 = "in a hurry, you flee from the\ncountry and go to the USA.\nwhen you get past the border,\nyou rent an apartment,\nenroll in a new school,\nand start a new life."
        text2 = "a few weeks into school,\nyou forget your homework again.\nthis seems familiar...."
        text3 = "YOU LOSE"
        text4 = ""
        choicetext1 = ""
        choicetext2 = ""
        choicetext3 = ""
        choicetext4 = ""
        choicetext5 = ""
        questionchoice = False
        question1 = ""
        question2 = ""
        question3 = ""
        question4 = ""
        question5 = ""
        solution1 = ""
        solution2 = ""
        solution3 = ""
        solution4 = ""
        solution5 = ""
        win = ""
        lose = ""
        a = 0
        choice(text1, text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)


    if choicepath == "12":
        text1 = "you: get ready,\nbecause I'm about to fight you."
        text2 = "teacher: well this is my class,\nso you're fighting by my rules!\nMath battle!"
        text3 = ""
        text4 = ""
        choicetext1 = "accept fight"
        choicetext2 = "refuse fight"
        choicetext3 = "mystery"
        choicetext4 = ""
        choicetext5 = ""
        questionchoice = False
        question1 = ""
        question2 = ""
        question3 = ""
        question4 = ""
        question5 = ""
        solution1 = ""
        solution2 = ""
        solution3 = ""
        solution4 = ""
        solution5 = ""
        win = ""
        lose = ""
        a = 0
        choice(text1, text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)


    if choicepath == "121":
        text1 = "you choose to accept the fight. but what\nthe teacher doesn't know is that you\nwere lying about accepting it on his terms.\n"
        text2 = "you start attacking the teacher,\ncatching him off guard.\nsince he is old,\nyou easily win the fight.\n"
        text3 = "however, the school board\nends up finding out about this,\nand you are expelled."
        Choice1.place(x = 10000, y = 10000)
        Choice2.place(x = 10000, y = 10000)
        Choice3.place(x = 10000, y = 10000)
        Choice4.place(x = 10000, y = 10000)
        Choice5.place(x = 10000, y = 10000)
        Choice1text.place(x = 10000, y = 10000)
        Choice2text.place(x = 10000, y = 10000)
        Choice3text.place(x = 10000, y = 10000)
        Choice4text.place(x = 10000, y = 10000)
        Choice5text.place(x = 10000, y = 10000)
        text.configure(text= text1 + text2 + text3)
        gobackbutton = tk.Button(root, text="Next", command=lambda:goback())
        gobackbutton.configure(font=("Arial", 20, "bold"))
        gobackbutton.place(x = 250, y = 315, height = 50, width = 100, anchor='center')
        choicepath = "11"


    # this changes the choices given to match what should be displayed to avoid a bunch of repeated code.
    if choicepath == "122":
        choicepath = "11"
        algorithm()


    # this displays text without giving any options, as the section of the story that will follow it has already been determined and will be displayed upon the press of a button.
    if choicepath == "123":
        text1 = "you throw your desk at your teacher.\nit hits him really hard,\nknocking him over with a yelp of pain.\n"
        text2 = "when the ambulance comes,\nyou find out you broke some of his ribs."
        Choice1.place(x = 10000, y = 10000)
        Choice2.place(x = 10000, y = 10000)
        Choice3.place(x = 10000, y = 10000)
        Choice4.place(x = 10000, y = 10000)
        Choice5.place(x = 10000, y = 10000)
        Choice1text.place(x = 10000, y = 10000)
        Choice2text.place(x = 10000, y = 10000)
        Choice3text.place(x = 10000, y = 10000)
        Choice4text.place(x = 10000, y = 10000)
        Choice5text.place(x = 10000, y = 10000)
        text.configure(text= text1 + text2)
        gobackbutton = tk.Button(root, text="Next", command=lambda:goback())
        gobackbutton.configure(font=("Arial", 20, "bold"))
        gobackbutton.place(x = 250, y = 315, height = 50, width = 100, anchor='center')
        choicepath = "11"


    if choicepath == "13":
        text1 = "I can prove that I did my homework,\nand that my dog actually ate my computer,\neven though I don't have my computer."
        text2 = "teacher: and how will you do that?\nyou: by answering some\nquestions from the homework.\nteacher: haha. good luck"
        text3 = ""
        text4 = ""
        choicetext1 = ""
        choicetext2 = ""
        choicetext3 = ""
        choicetext4 = ""
        choicetext5 = ""
        questionchoice = True
        question1 = "if you pick 4 points at random \non the surface of a sphere,\nand draw lines connecting them all\ntogether, making a 3D shape,\nwhat is the probability that the\ncenter of the circle will\nbe within the shape?"
        question2 = "solve: 2 x^2y^11 + 3xy^1 - 15y = 0,\ny(1) = 0 y^1 (1) = 1"
        question3 = "What property of the universe is\nresponsible for making things near\nblack holes experience time slower?"
        question4 = ""
        question5 = ""
        solution1 = "1/8\n"
        solution2 = "y(x) = 0.2x^2.5 - 0.2x^-3\n"
        solution3 = "mass warping space time\n"
        solution4 = ""
        solution5 = ""
        win = "you cheated.\nYOU LOSE"
        lose = "you lied! you didn't do your homework!\nI'm calling your parents to\ntell them you lied to my\nface about doing your homework."
        a = 0
        choice(text1, text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)


    if choicepath == "14":
        text1 = "you take your chewed up, bent\nand broken computer of your bag.\nthe teacher stares at it in confusion\nand awe for a moment, before speaking."
        text2 = "teacher: wow.\nyour dog really did eat your homework.\nI didn't think that was possible.\nsorry for the misunderstanding."
        text3 = "YOU WIN\n you don't get in trouble for\n not doing your homework,\n since you couldn't do it."
        text4 = ""
        choicetext1 = ""
        choicetext2 = ""
        choicetext3 = ""
        choicetext4 = ""
        choicetext5 = ""
        questionchoice = False
        question1 = ""
        question2 = ""
        question3 = ""
        question4 = ""
        question5 = ""
        solution1 = ""
        solution2 = ""
        solution3 = ""
        solution4 = ""
        solution5 = ""
        win = ""
        lose = ""
        a = 0
        choice(text1, text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)


    if choicepath == "2":
        text1 = "teacher: well then how prepared are you\nfor todays pop quiz?"
        text2 = "you realize that you don't know the stuff\non the homework, meaning you will\nmost likely fail the quiz.\nWhat will you do?"
        text3 = ""
        text4 = ""
        choicetext1 = "attempt the quiz"
        choicetext2 = "try to cheat on the quiz"
        choicetext3 = "fight the teacher"
        choicetext4 = "mystery"
        choicetext5 = ""
        questionchoice = False
        question1 = ""
        question2 = ""
        question3 = ""
        question4 = ""
        question5 = ""
        solution1 = ""
        solution2 = ""
        solution3 = ""
        solution4 = ""
        solution5 = ""
        win = ""
        lose = ""
        a = 0
        choice(text1, text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)


    if choicepath == "21":
        text1 = "you try the quiz.\nyou fail the quiz since you didn't\nunderstand the contents of it since\nyou didn't do your homework.\nyour parents find out." # Choice 11
        Choice1.place(x = 10000, y = 10000)
        Choice2.place(x = 10000, y = 10000)
        Choice3.place(x = 10000, y = 10000)
        Choice4.place(x = 10000, y = 10000)
        Choice5.place(x = 10000, y = 10000)
        Choice1text.place(x = 10000, y = 10000)
        Choice2text.place(x = 10000, y = 10000)
        Choice3text.place(x = 10000, y = 10000)
        Choice4text.place(x = 10000, y = 10000)
        Choice5text.place(x = 10000, y = 10000)
        text.configure(text= text1)
        gobackbutton = tk.Button(root, text="Next", command=lambda:goback())
        gobackbutton.configure(font=("Arial", 20, "bold"))
        gobackbutton.place(x = 250, y = 315, height = 50, width = 100, anchor='center')
        choicepath = "11"


    if choicepath == "22":
        text1 = "you try to cheat on the quiz by looking\nover at peope around you. when you\nfinish the quiz, you think that you did\npretty good, and you go to hand it to the\n"
        text2 = "teacher. as soon as you hand it to the\nteacher, he rips it up in front of you. teacher:\n"
        text3 = "I know you cheated! I saw you looking over at\npeople all around you for answers. I dont\nneed to look at this to know your mark.\nit's a 0."
        Choice1.place(x = 10000, y = 10000)
        Choice2.place(x = 10000, y = 10000)
        Choice3.place(x = 10000, y = 10000)
        Choice4.place(x = 10000, y = 10000)
        Choice5.place(x = 10000, y = 10000)
        Choice1text.place(x = 10000, y = 10000)
        Choice2text.place(x = 10000, y = 10000)
        Choice3text.place(x = 10000, y = 10000)
        Choice4text.place(x = 10000, y = 10000)
        Choice5text.place(x = 10000, y = 10000)
        text.configure(text= text1 + text2 + text3)
        gobackbutton = tk.Button(root, text="Next", command=lambda:goback())
        gobackbutton.configure(font=("Arial", 20, "bold"))
        gobackbutton.place(x = 250, y = 315, height = 50, width = 100, anchor='center')
        choicepath = "11"

    
    if choicepath == "23":
        text1 = "you: get ready,\nbecause I'm about to fight you.\nteacher: well this is my class,\nso you're fighting by my rules!\nMath battle!"
        text2 = "being the idiot you are,\nyou blindly accept the fight,\nthinking you will be fine.\nThe teacher hands you a pencil and paper,\nand sits down at a desk next to you."
        text3 = "teacher: the rules are simple.\nwe are both given the same question,\nmand the first to answer it correctly\ngets a point. first to 3 points wins.\ncalculators allowed."
        text4 = ""
        choicetext1 = ""
        choicetext2 = ""
        choicetext3 = ""
        choicetext4 = ""
        choicetext5 = ""
        questionchoice = True
        question1 = "square the number 392."
        question2 = "solve: a^2 + b^2 = 1\nc^2 + d^2 = 2\n(ac + bd)^2 + (ad - bc)^2 = ?"
        question3 = "calculate the minimum number of turns\nneeded to solve every possible scramble\non a standard 3x3x3 rubiks cube."
        question4 = "x = 1, y = 10, solve:\ndy / dx = (10x - 1) / (4 + 3y^2)"
        question5 = "k = 33, solve for x, y, z:\nx^3 + y^3 + z^3 = k"
        solution1 = "153664\n"
        solution2 = "2\n"
        solution3 = "20\n"
        solution4 = "5x^2 - y^3 = 4y + x + A\n"
        solution5 = "\nX = -80538738812075974\nY = 80435758145817515\nZ = 12602123297335631\n"
        win = "you cheated.\nYOU LOSE"
        lose = "teacher: looks like you lose.\nI wonder why.\nyour parents will be finding out soon."
        a = 0
        choice(text1, text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)


    if choicepath == "24":
        text1 = "you: actually,\nI'm going to give you a quiz.\nand if you fail, I'm going to tell\nthe school board that you aren't good\nenough at math to teach this class."
        text2 = "teacher: no thanks.\nyou can't make me do anything,\nso I don't have to do your quiz.\nhowever, you have to do mine, or I\nwill assume you didn't do your homework."
        text3 = ""
        text4 = ""
        choicetext1 = "take the quiz"
        choicetext2 = "don't take the quiz"
        choicetext3 = ""
        choicetext4 = ""
        choicetext5 = ""
        questionchoice = False
        question1 = ""
        question2 = ""
        question3 = ""
        question4 = ""
        question5 = ""
        solution1 = ""
        solution2 = ""
        solution3 = ""
        solution4 = ""
        solution5 = ""
        win = ""
        lose = ""
        a = 0
        choice(text1, text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)


    if choicepath == "241":
        text1 = "you choose to take the teachers quiz."
        text2 = ""
        text3 = ""
        text4 = ""
        choicetext1 = ""
        choicetext2 = ""
        choicetext3 = ""
        choicetext4 = ""
        choicetext5 = ""
        questionchoice = True
        question1 = "if you pick 4 points at random \non the surface of a sphere,\nand draw lines connecting them all\ntogether, making a 3D shape,\nwhat is the probability that the\ncenter of the circle will\nbe within the shape?"
        question2 = "solve: 2 x^2y^11 + 3xy^1 - 15y = 0,\ny(1) = 0 y^1 (1) = 1"
        question3 = "What property of the universe is\nresponsible for making things near\nblack holes experience time slower?"
        question4 = ""
        question5 = ""
        solution1 = "1/8\n"
        solution2 = "y(x) = 0.2x^2.5 - 0.2x^-3\n"
        solution3 = "mass warping space time\n"
        solution4 = ""
        solution5 = ""
        win = "you cheated.\nYOU LOSE"
        lose = "teacher: you failed the quiz.\nI'm sure your parents will be\ndelighted to hear about this."
        a = 0
        choice(text1, text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)


    if choicepath == "242":
        choicepath = "11"
        algorithm()
     

    if choicepath == "3":
        text1 = "teacher: oh, well that's good. Then I\nassume that you wlll be able to ace the\npop quiz today, because if you don't, your\nparents will be delighted to hear that\nyou didn't do your homework\nand failed a quiz because of it."
        text2 = "after realizing what you've gotten yourself into,\nyou must now choose what you will do."
        text3 = ""
        text4 = ""
        choicetext1 = "attempt the quiz"
        choicetext2 = "fight the teacher"
        choicetext3 = "mystery"
        choicetext4 = ""
        choicetext5 = ""
        questionchoice = False
        question1 = ""
        question2 = ""
        question3 = ""
        question4 = ""
        question5 = ""
        solution1 = ""
        solution2 = ""
        solution3 = ""
        solution4 = ""
        solution5 = ""
        win = ""
        lose = ""
        a = 0
        choice(text1, text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)
    

    if choicepath == "31":
        text1 = "you choose to attempt the quiz."
        text2 = ""
        text3 = ""
        text4 = ""
        choicetext1 = ""
        choicetext2 = ""
        choicetext3 = ""
        choicetext4 = ""
        choicetext5 = ""
        questionchoice = True
        question1 = "solve:\n6 / 2(1 + 2)"
        question2 = "1 + 4 = 5\n2 + 5 = 12\n3 + 6 = 21\n8 + 11 = ?"
        question3 = "solve for x:\n3x = (5 + (4^2 + 6^2)) - 5(5! -3)"
        question4 = ""
        question5 = ""
        solution1 = "9\n"
        solution2 = "96\n"
        solution3 = "-176\n"
        solution4 = ""
        solution5 = ""
        win = "teacher: wow. you really are smart\nenough to ace the quiz without doing\nhomework. sorry for bothering you.\nYOU WIN"
        lose = "teacher: well well well.\nyou didn't do good on the quiz.\nI wonder why. I think your parents\nwill be interested to hear about this."
        a = 0
        choice(text1, text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)


    if choicepath == "32":
        text1 = "you: get ready,\nbecause Im' about to fight you."
        text2 = "teacher: well this is my class,\nso you're fighting by my rules!\nMath battle!"
        text3 = ""
        text4 = ""
        choicetext1 = "accept fight"
        choicetext2 = "refuse fight"
        choicetext3 = "mystery"
        choicetext4 = ""
        choicetext5 = ""
        questionchoice = False
        question1 = ""
        question2 = ""
        question3 = ""
        question4 = ""
        question5 = ""
        solution1 = ""
        solution2 = ""
        solution3 = ""
        solution4 = ""
        solution5 = ""
        win = ""
        lose = ""
        a = 0
        choice(text1, text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)


    if choicepath == "321":
        text1 = "teacher: the rules are simple.\nwe are both given the same question,\nmand the first to answer it correctly\ngets a point. first to 3 points wins.\ncalculators allowed."
        text2 = ""
        text3 = ""
        text4 = ""
        choicetext1 = ""
        choicetext2 = ""
        choicetext3 = ""
        choicetext4 = ""
        choicetext5 = ""
        questionchoice = True
        question1 = "find the square root of x:\n3x = 6(5! - 3) - ((3^3)6 - (4^2 + 6^2) + (3^2))"
        question2 = "square the number 392."
        question3 = "simplify:\n(x + 5y)^2"
        question4 = "factor:\n3x^2 - 8x - 3"
        question5 = "factor fully:\n4(x^2 + 10x + 25) - 4x^2 - 24x - 36"
        solution1 = "14\n"
        solution2 = "153664\n"
        solution3 = "x^2 + 10xy + 25y^2\n"
        solution4 = "(x - 3) (3x + 1)\n"
        solution5 = "16(x + 4)"
        win = "teacher: well, you win.\nI guess you didn't need to do your homework.\nYOU WIN"
        lose = "teacher: looks like you lose.\nI guess you should've done your homework.\nyour parents will be finding out soon."
        a = 0
        choice(text1, text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)


    if choicepath == "322":
        Choice1.place(x = 10000, y = 10000)
        Choice2.place(x = 10000, y = 10000)
        Choice3.place(x = 10000, y = 10000)
        Choice4.place(x = 10000, y = 10000)
        Choice5.place(x = 10000, y = 10000)
        Choice1text.place(x = 10000, y = 10000)
        Choice2text.place(x = 10000, y = 10000)
        Choice3text.place(x = 10000, y = 10000)
        Choice4text.place(x = 10000, y = 10000)
        Choice5text.place(x = 10000, y = 10000)
        text1 = "well then I'm going to phone your parents and tell them about this."
        text.configure(text= text1)
        gobackbutton = tk.Button(root, text="Next", command=lambda:goback())
        gobackbutton.configure(font=("Arial", 20, "bold"))
        gobackbutton.place(x = 250, y = 315, height = 50, width = 100, anchor='center')
        choicepath = "11"


    if choicepath == "323":
        text1 = "you choose to beat up the teacher\nwith your fists. since he is in his\nfifties and you are a teen, you\neasily overpower him and beat him.\n"
        text2 = "however, the school board ends\nup finding out, and you get expelled."
        Choice1.place(x = 10000, y = 10000)
        Choice2.place(x = 10000, y = 10000)
        Choice3.place(x = 10000, y = 10000)
        Choice4.place(x = 10000, y = 10000)
        Choice5.place(x = 10000, y = 10000)
        Choice1text.place(x = 10000, y = 10000)
        Choice2text.place(x = 10000, y = 10000)
        Choice3text.place(x = 10000, y = 10000)
        Choice4text.place(x = 10000, y = 10000)
        Choice5text.place(x = 10000, y = 10000)
        text.configure(text= text1 + text2)
        gobackbutton = tk.Button(root, text="Next", command=lambda:goback())
        gobackbutton.configure(font=("Arial", 20, "bold"))
        gobackbutton.place(x = 250, y = 315, height = 50, width = 100, anchor='center')
        choicepath = "11"


    if choicepath == "33":
        text1 = "you: actually,\nI'm going to give you a quiz.\nand if you fail, I'm going to tell\nthe school board that you aren't good\nenough at math to teach this class."
        text2 = "teacher: and if I ace the quiz,\nI get to fail you for this class."
        text3 = ""
        text4 = ""
        choicetext1 = "deal"
        choicetext2 = "no deal"
        choicetext3 = ""
        choicetext4 = ""
        choicetext5 = ""
        questionchoice = False
        question1 = ""
        question2 = ""
        question3 = ""
        question4 = ""
        question5 = ""
        solution1 = ""
        solution2 = ""
        solution3 = ""
        solution4 = ""
        solution5 = ""
        win = ""
        lose = ""
        a = 0
        choice(text1, text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)


    if choicepath == "331":
        text1 = "you:\ndeal."
        text2 = "the teacher, who underestimated\nthe size of your brain,\nended up completely failing the quiz.\nyou: well I wonder what the school\nboard will do when they hear about this."
        text3 = "the school board ended up punishing the\nteacher, however the punishments were\nnot disclosed to the school.\nthe teacher still has his job,\nso most likely docked pay."
        text4 = "YOU WIN"
        choicetext1 = ""
        choicetext2 = ""
        choicetext3 = ""
        choicetext4 = ""
        choicetext5 = ""
        questionchoice = False
        question1 = ""
        question2 = ""
        question3 = ""
        question4 = ""
        question5 = ""
        solution1 = ""
        solution2 = ""
        solution3 = ""
        solution4 = ""
        solution5 = ""
        win = ""
        lose = ""
        a = 0
        choice(text1, text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)


    if choicepath == "332":
        Choice1.place(x = 10000, y = 10000)
        Choice2.place(x = 10000, y = 10000)
        Choice3.place(x = 10000, y = 10000)
        Choice4.place(x = 10000, y = 10000)
        Choice5.place(x = 10000, y = 10000)
        Choice1text.place(x = 10000, y = 10000)
        Choice2text.place(x = 10000, y = 10000)
        Choice3text.place(x = 10000, y = 10000)
        Choice4text.place(x = 10000, y = 10000)
        Choice5text.place(x = 10000, y = 10000)
        text1 = "teacher: well then I'm going to tell\nyour parents about what has happened here\nas you have wasted too much of\nmy time for this to continue."
        text.configure(text= text1)
        gobackbutton = tk.Button(root, text="Next", command=lambda:goback())
        gobackbutton.configure(font=("Arial", 20, "bold"))
        gobackbutton.place(x = 250, y = 315, height = 50, width = 100, anchor='center')
        choicepath = "11"


    if choicepath == "4":
        text1 = "you: get ready,\nbecause I'm about to fight you."
        text2 = "teacher: well this is my class,\nso you're fighting by my rules! Math battle!"
        text3 = "unsure about whether or not you can\nbeat your teacher at his own game,\nyou think about what you will do"
        text4 = ""
        choicetext1 = "accept fight"
        choicetext2 = "refuse fight"
        choicetext3 = "run away"
        choicetext4 = "mystery"
        choicetext5 = ""
        questionchoice = False
        question1 = ""
        question2 = ""
        question3 = ""
        question4 = ""
        question5 = ""
        solution1 = ""
        solution2 = ""
        solution3 = ""
        solution4 = ""
        solution5 = ""
        win = ""
        lose = ""
        a = 0
        choice(text1, text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)

    
    if choicepath == "41":
        text1 = "you: I accept."
        text2 = "teacher: the rules are simple.\nwe are both given the same question,\nmand the first to answer it correctly\ngets a point. first to 3 points wins.\ncalculators allowed."
        text3 = ""
        text4 = ""
        choicetext1 = ""
        choicetext2 = ""
        choicetext3 = ""
        choicetext4 = ""
        choicetext5 = ""
        questionchoice = True
        question1 = "find the square root of x:\n3x = 6(5! - 3) - ((3^3)6 - (4^2 + 6^2) + (3^2))"
        question2 = "square the number 392."
        question3 = "simplify:\n(x + 5y)^2"
        question4 = "factor:\n3x^2 - 8x - 3"
        question5 = "factor fully:\n4(x^2 + 10x + 25) - 4x^2 - 24x - 36"
        solution1 = "14\n"
        solution2 = "153664\n"
        solution3 = "x^2 + 10xy + 25y^2\n"
        solution4 = "(x - 3) (3x + 1)\n"
        solution5 = "16(x + 4)"
        win = "teacher: well, you win.\nI guess you didn't need to do your homework.\nYOU WIN"
        lose = "teacher: looks like you lose.\nI guess you should've done your homework.\nyour parents will be finding out soon."
        a = 0
        choice(text1, text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)


    if choicepath == "42":
      choicepath == "11"
      algorithm()


    if choicepath == "43":
        Choice1.place(x = 10000, y = 10000)
        Choice2.place(x = 10000, y = 10000)
        Choice3.place(x = 10000, y = 10000)
        Choice4.place(x = 10000, y = 10000)
        Choice5.place(x = 10000, y = 10000)
        Choice1text.place(x = 10000, y = 10000)
        Choice2text.place(x = 10000, y = 10000)
        Choice3text.place(x = 10000, y = 10000)
        Choice4text.place(x = 10000, y = 10000)
        Choice5text.place(x = 10000, y = 10000)
        text1 = "you run away. after realizing you\ncan't just sleep on the road,\nyou go back home to angry parents."
        text.configure(text= text1)
        gobackbutton = tk.Button(root, text="Next", command=lambda:goback())
        gobackbutton.configure(font=("Arial", 20, "bold"))
        gobackbutton.place(x = 250, y = 315, height = 50, width = 100, anchor='center')
        choicepath = "11"


    if choicepath == "44":
        Choice1.place(x = 10000, y = 10000)
        Choice2.place(x = 10000, y = 10000)
        Choice3.place(x = 10000, y = 10000)
        Choice4.place(x = 10000, y = 10000)
        Choice5.place(x = 10000, y = 10000)
        Choice1text.place(x = 10000, y = 10000)
        Choice2text.place(x = 10000, y = 10000)
        Choice3text.place(x = 10000, y = 10000)
        Choice4text.place(x = 10000, y = 10000)
        Choice5text.place(x = 10000, y = 10000)
        text1 = "you choose to beat up the teacher\ninstead of playing his math game.\nas a strong teen, you easily beat up\nyour math teacher who is an old man.\n"
        text2 = "\nhowever, the school board finds\nout about this and you are expelled."
        text.configure(text= text1 + text2)
        gobackbutton = tk.Button(root, text="Next", command=lambda:goback())
        gobackbutton.configure(font=("Arial", 20, "bold"))
        gobackbutton.place(x = 250, y = 315, height = 50, width = 100, anchor='center')
        choicepath = "11"


    if choicepath == "5":
        text1 = "you noclip through the floor into the\nworst possible backrooms floor, a massive\nocean filled with man-eating monsters."
        text2 = "you tread water until every muscle\nin your body runs out of strengh,\nand then you sink down to the\nmonsters and get eaten alive."
        text3 = "YOU DIE"
        text4 = ""
        choicetext1 = ""
        choicetext2 = ""
        choicetext3 = ""
        choicetext4 = ""
        choicetext5 = ""
        questionchoice = False
        question1 = ""
        question2 = ""
        question3 = ""
        question4 = ""
        question5 = ""
        solution1 = ""
        solution2 = ""
        solution3 = ""
        solution4 = ""
        solution5 = ""
        win = ""
        lose = ""
        a = 0
        choice(text1, text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)



# buttons that are displayed when a choice needs to be made.
Choice1 = tk.Button(root, text="1", anchor='center', command=lambda:choose1())
Choice1.configure(font=("Arial", 18, "bold"))

Choice2 = tk.Button(root, text="2", anchor='center', command=lambda:choose2())
Choice2.configure(font=("Arial", 18, "bold"))

Choice3 = tk.Button(root, text="3", anchor='center', command=lambda:choose3())
Choice3.configure(font=("Arial", 18, "bold"))

Choice4 = tk.Button(root, text="4", anchor='center', command=lambda:choose4())
Choice4.configure(font=("Arial", 18, "bold"))

Choice5 = tk.Button(root, text="5", anchor='center', command=lambda:choose5())
Choice5.configure(font=("Arial", 18, "bold"))

# text that is displayed when a choice needs to be made.
Choice1text = tk.Label(text = "")
Choice1text.configure(font=("Arial", 12, ""))

Choice2text = tk.Label(text = "")
Choice2text.configure(font=("Arial", 12, ""))

Choice3text = tk.Label(text = "")
Choice3text.configure(font=("Arial", 12, ""))

Choice4text = tk.Label(text = "")
Choice4text.configure(font=("Arial", 12, ""))

Choice5text = tk.Label(text = "")
Choice5text.configure(font=("Arial", 12, ""))

# functions attached to the buttons above to allow them to change the path of the story by concatenating numbers on to a variable to keep track of the choices made.
def choose1():
    global choicepath
    choicepath += "1"
    back.place(x = 10000, y = 10000)
    print(choicepath)
    algorithm()

def choose2():
    global choicepath
    choicepath += "2"
    back.place(x = 10000, y = 10000)
    print(choicepath)
    algorithm()

def choose3():
    global choicepath
    choicepath += "3"
    back.place(x = 10000, y = 10000)
    print(choicepath)
    algorithm()

def choose4():
    global choicepath
    choicepath += "4"
    back.place(x = 10000, y = 10000)
    print(choicepath)
    algorithm()

def choose5():
    global choicepath
    choicepath += "5"
    back.place(x = 10000, y = 10000)
    print(choicepath)
    algorithm()

# a large function that uses variable data given to it to build and display different sections of the story depending on what info is given to it.
def choice(text1, text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose):
    global text, next, back
    
    # displaying a few buttons to progress through the section and the story.
    next = tk.Button(root, text="-->", anchor='center', bg='gainsboro', command=lambda:nextpage(text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose))
    next.configure(font=("Arial", 20, "bold"))
    next.place(x = 450, y = 315, height = 50, width = 80, anchor='center')

    text = tk.Label(root, text = text1)
    text.configure(font=("Arial", 18, ""))
    text.place(x = 250, y = 0, anchor='n')

    back = tk.Button(root, text="<--", anchor='center', bg='gainsboro', command=lambda:backpage(text1, text2, text3, text4))
    back.configure(font=("Arial", 20, "bold"))
    back.place(x = 10000, y = 10000)

    # moving unused stuff out of the way.
    Choice1.place(x = 10000, y = 10000)
    Choice2.place(x = 10000, y = 10000)
    Choice3.place(x = 10000, y = 10000)
    Choice4.place(x = 10000, y = 10000)
    Choice5.place(x = 10000, y = 10000)
    Choice1text.place(x = 10000, y = 10000)
    Choice2text.place(x = 10000, y = 10000)
    Choice3text.place(x = 10000, y = 10000)
    Choice4text.place(x = 10000, y = 10000)
    Choice5text.place(x = 10000, y = 10000)

# a function that goes one page forwards when the story text doesn't all fit on the screen at once.
def nextpage(text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose):
    global a
    print(a)
    # this first part goes one page forwards in the text when it is pressed.
    if a == 0:
        # if second text variable has no data, don't display it, start function again and skip this check.
        if text2 == "":
            a += 1
            nextpage(text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)
        # if second text variable has data, display it, start function again and skip this check.
        else:
            a += 1
            text.configure(text= text2)
            back.place(x = 50, y = 315, height = 50, width = 80, anchor='center')
    elif a == 1:
        if text3 == "":
            a += 1
            nextpage(text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)
        else:
            a += 1
            text.configure(text= text3)
    elif a == 2:
        if text4 == "":
            a += 1
            nextpage(text2, text3, text4, choicetext1, choicetext2, choicetext3, choicetext4, choicetext5, questionchoice, question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)
        else:
            a += 1
            text.configure(text= text4)
    # this part displays the choice options when all the text has been displayed.
    elif a == 3:
        a += 1
        text.configure(text="")
        # if choice text variable has data, display it. if it doesn't have data, skip the all the checks to display them
        if choicetext1 != "":
            Choice1.place(x = 50, y = 50, anchor='center')
            Choice1text.configure(text = choicetext1)
            Choice1text.place(x = 75, y = 50, anchor='w')

        if choicetext2 != "":
            Choice2.place(x = 50, y = 100, anchor='center')
            Choice2text.configure(text = choicetext2)
            Choice2text.place(x = 75, y = 100, anchor='w')

        if choicetext3 != "":
            Choice3.place(x = 50, y = 150, anchor='center')
            Choice3text.configure(text = choicetext3)
            Choice3text.place(x = 75, y = 150, anchor='w')

        if choicetext4 != "":
            Choice4.place(x = 50, y = 200, anchor='center')
            Choice4text.configure(text = choicetext4)
            Choice4text.place(x = 75, y = 200, anchor='w')

        if choicetext5 != "":
            Choice5.place(x = 50, y = 250, anchor='center')
            Choice5text.configure(text = choicetext5)
            Choice5text.place(x = 75, y = 250, anchor='w')
        
        # this will run the question function when a question is mathematical, as the question function is built to display mathematical sections.
        if questionchoice == True:
            a = -1
            question(question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)
        next.place(x = 10000, y = 10000)

# this function goes one page back in text when it is pressed.
def backpage(text1, text2, text3, text4):
    global a
    if a == 4:
        if text4 == "":
            a = 3
            backpage(text1, text2, text3, text4)
        else: 
            a -= 1
            text.configure(text= text4)
        next.place(x = 450, y = 315, height = 50, width = 80, anchor='center')
    elif a == 3:
        if text3 == "":
            a = 2
            backpage(text1, text2, text3, text4)
        else:
            a -= 1
            text.configure(text= text3)
    elif a == 2:
        if text2 == "":
            a = 1
            backpage(text1, text2, text3, text4)
        else:
            a -= 1
            text.configure(text= text2)
    elif a == 1:
        if text1 == "":
            a = 0
            backpage(text1, text2, text3, text4)
        else:
            a -= 1
            text.configure(text= text1)
        back.place(x = 10000, y = 10000)
    # this next part moves the choices out of the way when the user goes back a page to read the text again.
    Choice1.place(x = 10000, y = 10000)
    Choice2.place(x = 10000, y = 10000)
    Choice3.place(x = 10000, y = 10000)
    Choice4.place(x = 10000, y = 10000)
    Choice5.place(x = 10000, y = 10000)
    Choice1text.place(x = 10000, y = 10000)
    Choice2text.place(x = 10000, y = 10000)
    Choice3text.place(x = 10000, y = 10000)
    Choice4text.place(x = 10000, y = 10000)
    Choice5text.place(x = 10000, y = 10000)

# this is a function that sets up the "nextquestion" function, which has a similar purpose to the previous "choice" function, except this displays questions that involve mathematical questions and answers.
def question(question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose):
    global text, next, back, submit

    text.configure(text= "")

    submit = tk.Button(root, text="Start", anchor='center', command=lambda:nextquestion(question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose))
    submit.configure(font=("Arial", 20, "bold"))
    submit.place(x = 250, y = 175, height = 100, width = 160, anchor='center')

    # move unused buttons out of the way
    Choice1.place(x = 10000, y = 10000)
    Choice2.place(x = 10000, y = 10000)
    Choice3.place(x = 10000, y = 10000)
    Choice4.place(x = 10000, y = 10000)
    Choice5.place(x = 10000, y = 10000)
    Choice1text.place(x = 10000, y = 10000)
    Choice2text.place(x = 10000, y = 10000)
    Choice3text.place(x = 10000, y = 10000)
    Choice4text.place(x = 10000, y = 10000)
    Choice5text.place(x = 10000, y = 10000)
    back.place(x = 10000, y = 10000)
    next.place(x = 10000, y = 10000)\

questionbox = tk.Text(root, height = 1, width = 30, bg='white')

# this function is specifically designed to be able to display mathematical sections, as the "choice" function isn't able to.
def nextquestion(question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose):
    global a, questionbox, check, choicepath
    # this import is to help with math, as it is a calculator I made for fun that can be used to help during math questions.
    import Calculator
    submit.place(x = 10000, y = 10000)

    # this section figures out which question needs to be displayed, and it displays it along with an input box and a submit button to input answers.
    if a == -1:
        a += 1
        check = tk.Button(root, text="Submit", command=lambda:answercheck(solution1, solution2, solution3, solution4, solution5))
        check.configure(font=("Arial", 20, "bold"))
        check.place(x = 250, y = 315, height = 50, width = 120, anchor='center')
        text.configure(text= question1)
        questionbox.place(x = 250, y = 260, anchor='center')

    elif a == 0:
        a += 1
        # if second question variable doesnt' have data, don't display it and skip checks for all following questions.
        if question2 == "":
            a == 10
            nextquestion(question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)
        # if second question has data, display it
        else:
            check = tk.Button(root, text="Submit", command=lambda:answercheck(solution1, solution2, solution3, solution4, solution5))
            check.configure(font=("Arial", 20, "bold"))
            check.place(x = 250, y = 315, height = 50, width = 120, anchor='center')
            text.configure(text= question2)

    elif a == 1:
        a += 1
        if question3 == "":
            a == 10
            nextquestion(question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)
        else:
            check = tk.Button(root, text="Submit", command=lambda:answercheck(solution1, solution2, solution3, solution4, solution5))
            check.configure(font=("Arial", 20, "bold"))
            check.place(x = 250, y = 315, height = 50, width = 120, anchor='center')
            text.configure(text= question3)

    elif a == 2:
        a += 1
        if question4 == "":
            a == 10
            nextquestion(question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)
        else:
            check = tk.Button(root, text="Submit", command=lambda:answercheck(solution1, solution2, solution3, solution4, solution5))
            check.configure(font=("Arial", 20, "bold"))
            check.place(x = 250, y = 315, height = 50, width = 120, anchor='center')
            text.configure(text= question4)

    elif a == 3:
        a += 1
        if question5 == "":
            a == 10
            nextquestion(question1, question2, question3, question4, question5, solution1, solution2, solution3, solution4, solution5, win, lose)
        else:
            check = tk.Button(root, text="Submit", command=lambda:answercheck(solution1, solution2, solution3, solution4, solution5))
            check.configure(font=("Arial", 20, "bold"))
            check.place(x = 250, y = 315, height = 50, width = 120, anchor='center')
            text.configure(text= question5)
    
    # this last part ends the "nextquestion" function when all the questions have been displayed, and it displays different text depending on whether you got enough correct answers or not.
    else:
        questionbox.destroy()
        del questionbox
        # if three or more corret answers are given, display corresponding text and continue story if possible.
        if correct >= 3:
            text.configure(text= win)
        # if less than three correct answers are given, display corresponding text and continue story if possible.
        elif correct < 3:
            global gobackbutton
            text.configure(text= lose)
            gobackbutton = tk.Button(root, text="Next", command=lambda:goback())
            gobackbutton.configure(font=("Arial", 20, "bold"))
            gobackbutton.place(x = 250, y = 315, height = 50, width = 100, anchor='center')
            choicepath = "11"

# this returns to the "algorithm" function when a section of the story is completed.
def goback():
    text.configure(text= "")
    gobackbutton.destroy()
    algorithm()

# this checks if the answer inputted with the "questionchoice" function is correct or not, and it displays whether the answer is correct or not. it also adds to a variable to keep track of correct answers when a correct answer is given.
def answercheck(solution1, solution2, solution3, solution4, solution5):
    global correct
    # this checks if the answer is correct or not, and depending if it is "True" or "False" it will display that you gave a correct or incorrect answer.
    if a == 0:
        # if input equals correct answer, display that a correct answer was inputted and add to correct answer counter variable.
        if questionbox.get(1.0, tk.END) == solution1:
            text.configure(text= "Correct!")
            questionbox.delete(1.0, tk.END)
            check.place(x = 10000, y = 10000)
            submit.configure(text= "Next")
            submit.place(x = 250, y = 315, height = 50, width = 100, anchor='center')
            correct += 1
        
        # if input doesn't equal correct answer, display that an incorrect answer was inputted.
        elif questionbox.get(1.0, tk.END) != solution1:
            text.configure(text= "wrong\nSolution: " + str(solution1))
            questionbox.delete(1.0, tk.END)
            check.place(x = 10000, y = 10000)
            submit.configure(text= "Next")
            submit.place(x = 250, y = 315, height = 50, width = 100, anchor='center')

    elif a == 1:
        if questionbox.get(1.0, tk.END) == solution2:
            text.configure(text= "Correct!")
            questionbox.delete(1.0, tk.END)
            check.place(x = 10000, y = 10000)
            submit.configure(text= "Next")
            submit.place(x = 250, y = 315, height = 50, width = 100, anchor='center')
            correct += 1
        
        elif questionbox.get(1.0, tk.END) != solution2:
            text.configure(text= "wrong\nSolution: " + str(solution2))
            questionbox.delete(1.0, tk.END)
            check.place(x = 10000, y = 10000)
            submit.configure(text= "Next")
            submit.place(x = 250, y = 315, height = 50, width = 100, anchor='center')
    
    elif a == 2:
        if questionbox.get(1.0, tk.END) == solution3:
            text.configure(text= "Correct!")
            questionbox.delete(1.0, tk.END)
            check.place(x = 10000, y = 10000)
            submit.configure(text= "Next")
            submit.place(x = 250, y = 315, height = 50, width = 100, anchor='center')
            correct += 1
        
        elif questionbox.get(1.0, tk.END) != solution3:
            text.configure(text= "wrong\nSolution: " + str(solution3))
            questionbox.delete(1.0, tk.END)
            check.place(x = 10000, y = 10000)
            submit.configure(text= "Next")
            submit.place(x = 250, y = 315, height = 50, width = 100, anchor='center')

    elif a == 3:
        if questionbox.get(1.0, tk.END) == solution4:
            text.configure(text= "Correct!")
            questionbox.delete(1.0, tk.END)
            check.place(x = 10000, y = 10000)
            submit.configure(text= "Next")
            submit.place(x = 250, y = 315, height = 50, width = 100, anchor='center')
            correct += 1
        
        elif questionbox.get(1.0, tk.END) != solution4:
            text.configure(text= "wrong\nSolution: " + str(solution4))
            questionbox.delete(1.0, tk.END)
            check.place(x = 10000, y = 10000)
            submit.configure(text= "Next")
            submit.place(x = 250, y = 315, height = 50, width = 100, anchor='center')

    elif a == 4:
        if questionbox.get(1.0, tk.END) == solution5:
            text.configure(text= "Correct!")
            questionbox.delete(1.0, tk.END)
            check.place(x = 10000, y = 10000)
            submit.configure(text= "Next")
            submit.place(x = 250, y = 315, height = 50, width = 100, anchor='center')
            correct += 1
        
        elif questionbox.get(1.0, tk.END) != solution5:
            text.configure(text= "wrong\nSolution: " + str(solution5))
            questionbox.delete(1.0, tk.END)
            check.place(x = 10000, y = 10000)
            submit.configure(text= "Next")
            submit.place(x = 250, y = 315, height = 50, width = 100, anchor='center')





# this creates the GUI and makes it so that the size can't be changed.
root.resizable(False, False)
root.mainloop()