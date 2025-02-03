#Magic8Ball.py
#Name:Antonio PEREZ
#Date:JAN 29 2025
#Assignment:LAB 2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.  
  print("Magic 8 Ball")
  #Prompt the user for their question.

  
answers = ["yes", "no", "maybe","the end is near", "you will be rich","its going to rain "] 
  # Each item must be in quotes, separated by a comma.
  
  #Answer question randomly with one of the options from your earlier list.
length = len (answers)
r = random. random () * length
r = int(r) #cut off any decimal values

num = random.randint(0,6)



print(r)
response = answers [r]
print (response)

if __name__ == '__main__':
  main()
