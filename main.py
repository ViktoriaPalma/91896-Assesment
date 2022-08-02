#Variables
listMaori = []
listAnswers = []

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
randomtest = []
#Get rid of "\n" in each line due to the nature of the txt file
for aline in quizLines:
  randomtest = aline[5].strip("\n")
  #Seperate Answer title from the rest of the list because I only want the letters 
  if randomtest == "Answer":
    listAnswers.append(randomtest)
  else:
    #Get the alphabetic number
    #Subtract by 64 to make the Ascii into alphabet number
    x = ord(randomtest)-64
    #Ensure my answers are unique before adding it to my listAnswers 
    for quack in aline:
      quack = aline[x]
      if quack not in listAnswers:
        listAnswers.append(quack)
        




 
#Main menu

def main():
  #Title
  print("Maori Multiple choice quiz")
  #Menu 
  userinp = 0
  while userinp != -1:
    userinp = int(input("What would you like to do? 1 for learning, 2 for the quiz.\n"))
    if userinp == 1:
      learnMaori()
      
    elif userinp == 2:
      #will add quiz option later
      pass
    else:
      pass


def learnMaori():
  global listMaori
  #Print the Maori and english words to be learned
  for i in range(len(listMaori)):
    print(listMaori[i].ljust(20),listAnswers[i])

    



  
def quizMaori():
  pass
if __name__ == '__main__':
  main()
 