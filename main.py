#Variables
listMaori = []
listAnswers = []
optionAnswers = []
#imports
import os 
import time
import random

#Get the materials of the quiz from the txt file 
filename = 'quiz.txt'
f = open(filename,'r')
quizLines = f.readlines()
f.close()

#Split each line of the txt into a list and seperate them by comma
#Get the Maori words from the first item in each line and make a list for those Maori words
for i in range(len(quizLines)):
  quizLines[i] = quizLines[i].split(",")
for aline in quizLines:
  listMaori.append(aline[0])
  #print(aline)

#Getting the answers from the txtfile
answerFile = []
#Get rid of "\n" in each line due to the nature of the txt file
for aline in quizLines:
  answerFile = aline[5].strip("\n")
  #Seperate Answer title from the rest of the list because I only want the letters 
  if answerFile == "Answer":
    listAnswers.append(answerFile)
    optionAnswers.append(answerFile)
    
  else:
    #Get the alphabetic number
    #Subtract by 64 to make the Ascii into alphabet number
    x = ord(answerFile)-64
    #Ensure my answers are unique before adding it to my listAnswers 
    for uniqueAnswer in aline:
      uniqueAnswer = aline[x]
      if uniqueAnswer not in listAnswers:
        listAnswers.append(uniqueAnswer)     
        optionAnswers.append(answerFile)

        
        
#Main menu
def main():
  #Title
  print("Maori Multiple choice quiz") 
  userinp = 0
  while userinp != -1:
    userinp = int(input("What would you like to do? 1 for learning, 2 for the quiz.\n"))
    if userinp == 1:
      learnMaori()
      
    elif userinp == 2:
      quizMaori()
      
    else:
      pass


def learnMaori():
  #Print the Maori and english words to be learned
  for i in range(len(listMaori)):
    print(listMaori[i].ljust(20),listAnswers[i])
  time.sleep(8)
  os.system("clear")


def quizMaori():
  #get question randomly in list
  question = random.choice(listMaori)
  print("What is:",question)
  #Get the answer and questions based on the index of the question
  answer = listMaori.index(question)
  quiz = quizLines[answer]
  answer = optionAnswers[answer]

  #Display quiz
  print("A.",quiz[1],"B.",quiz[2],"C.",quiz[3],"D.",quiz[4])
  #Convert answer into uppercase so answer will be the same even if there caps/nocaps
  userAnswer = str(input()).upper()
  #Check if useranswer is correct
  if userAnswer == answer:
    print("correct")
  else:
    print("incorrect")


if __name__ == '__main__':
  main()
 