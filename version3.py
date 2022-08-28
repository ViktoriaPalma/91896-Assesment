#Variables
listMaori = []
listAnswers = []
optionAnswers = []
listTitle = []
counterCorrect = 0
incorrectAnswer = []
learnAnswer = []
incorrectQuestion = []
#imports
#to clear console
import os
#To delay os and allow user to read results before clearing
import time
#randomise the question so
import random
#for asthetic purposes
import fontstyle

#Get the materials of the quiz from the txt file
filename = 'quiz.txt'
f = open(filename, 'r')
quizLines = f.readlines()
f.close()

#Split each line of the txt into a list and seperate them by comma
#Get the Maori words from the first item in each line and make a list for those Maori words
for i in range(len(quizLines)):
    quizLines[i] = quizLines[i].split(",")

for aline in quizLines:
    listMaori.append(aline[0])

#Seperating "Maori Word" from Maori list and putting it into another list
listTitle.append(listMaori[0])
del listMaori[0]
#Getting the answers from the txtfile
answerFile = []
#Get rid of "\n" in each line due to the nature of the txt file
for aline in quizLines:
    answerFile = aline[5].strip("\n")
    #Seperate Answer title from the rest of the list because I only want the letters
    if answerFile == "Answer":
        listTitle.append(answerFile)
        del answerFile
    else:
        #Get the alphabetic number
        #Subtract by 64 to make the Ascii into alphabet number
        x = ord(answerFile) - 64
        #Ensure my answers are unique before adding it to my listAnswers
        for uniqueAnswer in aline:
            uniqueAnswer = aline[x]
            if uniqueAnswer not in listAnswers:
                listAnswers.append(uniqueAnswer)
                optionAnswers.append(answerFile)


#Main menu
def main():
    #Title
    print(fontstyle.apply("Maori Multiple choice quiz", 'bold/underline'))
    userinp = 0
    while userinp != -1:
        #input is not int(input()) so the program doesnt crash if user inputs a non numerical character
        userinp = input(
            "What would you like to do? 1 for learning, 2 for the quiz, 3 for the results.\n"
        )
        if userinp == "1":
            learnMaori()

        elif userinp == "2":
            quizMaori()

        elif userinp == "3":
            quizResults()


def learnMaori():
    #Print the titles of the two lists
    print(listTitle[0].ljust(20), listTitle[1])
    #Print the Maori and english words to be learned
    for i in range(len(listMaori)):
        print(listMaori[i].ljust(20), listAnswers[i])
    #when user is finished learning, they input any character to continue
    print("Enter anything when you are done learning")
    userinp = input()
    if userinp == userinp:
        time.sleep(2)
        os.system("clear")


def quizMaori():
    global counterCorrect
    questionUnique = []
    while len(questionUnique) < 8:
        #get question randomly in list
        question = random.choice(listMaori)
        if question not in questionUnique:
            questionUnique.append(question)
            print("What is:", fontstyle.apply(question, 'bold'))
            #Get the answer and questions based on the index of the question
            answer = listMaori.index(question)
            #quizoptions has a +1 as its first item is not needed
            quizoptions = answer + 1
            quiz = quizLines[quizoptions]
            answer = optionAnswers[answer]

            #Display quiz
            print("A.", quiz[1], "B.", quiz[2], "C.", quiz[3], "D.", quiz[4])
            #Convert answer into uppercase so answer will be the same even if user inputs in caps/lowercase
            userAnswer = str(input()).upper()
            #Check if useranswer is correct
            if userAnswer == answer:
                print(fontstyle.apply("correct", 'green/italic/green_bg'))
                time.sleep(2)
                os.system("clear")
                #Counter to keep track how many they have gotten correct
                counterCorrect += 1
            else:
                print(fontstyle.apply("incorrect", 'red/italic/red_bg'))
                #Add userinp, the correct option and question to an empty list for results
                incorrectAnswer.append(userAnswer)
                incorrectQuestion.append(question)
                learnAnswer.append(answer)
                time.sleep(2)
                os.system("clear")
    #once all questions have been asked, will go to main menu
    if len(questionUnique) == 8:
        main()


def quizResults():
    global counterCorrect
    print("This is how many you have gotten correct:", counterCorrect)
    #if the user has gotten a question or more wrong, it will print the correct answser, question and the useranswer
    if counterCorrect < 8:
      print("These are the questions you got wrong")
      print("Question".ljust(20),"Correct Answer".ljust(20), "Your Answer".ljust(20))
      for i in range(len(learnAnswer)):
          print(incorrectQuestion[i].ljust(20),learnAnswer[i].ljust(20), incorrectAnswer[i].ljust(20))

    #Check if user has passed the test
    #Resets counter to 0 if the user wants to redo the quiz
    if counterCorrect >= 4:
        print("Achieved")
        counterCorrect = 0
    else:
        print("Not Achieved")
        counterCorrect = 0


if __name__ == '__main__':
    main()
