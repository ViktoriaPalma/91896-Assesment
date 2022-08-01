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

#testing
for aline in quizLines:
  randomtest = aline[5]
  #print(randomtest)
  testvalue = (ord(randomtest)-96)
  print(testvalue)
#print(testvalue)

#Main menu
def main():
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
    print(listMaori[i])
  #print("What would you like to do now?")
    


  
if __name__ == '__main__':
  main()
 