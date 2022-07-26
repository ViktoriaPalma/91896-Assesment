#Get the materials from the txt file 
filename = 'quiz.txt'
f = open(filename,'r')
lines = f.readlines()
f.close()

print(lines)
print(lines[1])

